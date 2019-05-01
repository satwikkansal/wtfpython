import pprint
fname = "/Users/300041709/code/self/wtfpython/README.md"
examples = []

# The globals
current_example = 1
current_section_name = ""


def parse_example_parts(lines):
    parts = {
        "build_up": [],
        "explanation": []
    }
    next_line = next(lines)
    sequence_num = 1
    content = []
    # store build_up till an H4 (explanation) is encountered
    while not next_line.startswith("#### "):
        # Watching out for the snippets
        if next_line.startswith("```"):
            # It's a snippet, whatever found until now is text
            if content:
                parts["build_up"].append(
                    {
                        "type": "text",
                        "sequence_num": sequence_num,
                        "value": content
                    }
                )
                sequence_num += 1
                content = []

            next_line = next(lines)
            while not next_line.startswith("```"):
                content.append(next_line)
                next_line = next(lines)
            # Snippet is over
            parts["build_up"].append(
                {
                    "type": "code",
                    "sequence_num": sequence_num,
                    "value": content
                }
            )
            sequence_num += 1
            content = []
            next_line = next(lines)
            continue
        else:
            # It's a text, go on.
            content.append(next_line)
            next_line = next(lines)

    # Explanation encountered, save any content till now (if any)
    if content:
        parts["build_up"].append(
            {
                "type": "text",
                "sequence_num": sequence_num,
                "value": content
            }
        )

    # Reset stuff
    sequence_num = 1
    content = []

    # store lines again until --- or another H3 is encountered
    while not (next_line.startswith("---") or
               next_line.startswith("### ")):

        if next_line.startswith("```"):
            # It's a snippet, whatever found until now is text
            if content:
                parts["explanation"].append(
                    {
                        "type": "text",
                        "sequence_num": sequence_num,
                        "value": content
                    }
                )
                sequence_num += 1
                content = []

            next_line = next(lines)
            while not next_line.startswith("```"):
                content.append(next_line)
                next_line = next(lines)
            # Snippet is over
            parts["explanation"].append(
                {
                    "type": "code",
                    "sequence_num": sequence_num,
                    "value": content
                }
            )
            sequence_num += 1
            content = []
            next_line = next(lines)
            continue
        else:
            # It's a text, go on.
            content.append(next_line)
            next_line = next(lines)

    # All done
    if content:
        parts["explanation"].append(
            {
                "type": "text",
                "sequence_num": sequence_num,
                "value": content
            }
        )

    return next_line, parts


with open(fname, 'r+', encoding="utf-8") as f:
    lines = iter(f.readlines())
    line = next(lines)
    result = []
    try:
        while True:
            if line.startswith("## "):
                # A section is encountered
                current_section_name = line.replace("## ", "").strip()
                line = next(lines)
                # Until a new section is encountered
                while not (line.startswith("## " )):
                    # check if it's a H3
                    if line.startswith("### "):
                        # An example is encountered
                        title = line.replace("### ", "")
                        example_details = {
                            "id": current_example,
                            "title": line.replace("### ", ""),
                            "section": current_section_name
                        }
                        line, example_details["parts"] = parse_example_parts(lines)
                        result.append(example_details)
                        current_example += 1
                    else:
                        # todo catch section text
                        line = next(lines)
            else:
                line = next(lines)

    except StopIteration:
        pprint.pprint(result, indent=2)
        print(len(result))




