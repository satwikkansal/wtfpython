import pprint

fname = "README.md"
snippets = []

with open(fname, 'r') as f:
    lines = iter(f.readlines())
    line = lines.next()

    try:
        while True:
            # check if it's a H3
            if line.startswith("### "):
                title = line.replace("### ", "")
                # print(title, "found")
                description = []
                next_line = lines.next()

                # store lines till an H4 (explanation) is encountered
                while not next_line.startswith("#### "):
                    description.append(next_line)
                    next_line = lines.next()

                # print("Description captured", description[:10])

                explanation = []
                # store lines again until --- or another H3 is encountered
                while not (next_line.startswith("---") or
                           next_line.startswith("### ")):
                    explanation.append(next_line)
                    next_line = lines.next()

                # print("explanation captured", explanation[:10])


                # Store the results finally
                snippets.append({
                        "title": title,
                        "description": '\n'.join(description),
                        "explanation": '\n'.join(explanation)
                })

                line = next_line

            else:
                line = lines.next()

    except StopIteration:
        snippets.append({
                        "title": title,
                        "description": '\n'.join(description),
                        "explanation": '\n'.join(explanation)
        })

# separating by category
categories = ["a", "b", "c"]

snips_by_cat = {k:[] for k in categories}

for snip in snippets:
    cat = raw_input(snip["title"])
    snips_by_cat[cat].append(snip)

pprint.pprint("hail", snippets)
