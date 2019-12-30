# -*- coding: utf-8 -*-

"""
This inefficient module would parse the README.md in the initial version of
WTFPython, and enable me to categorize and reorder a hell lot of examples with
the help of the file `add_categories` (part of which is automatically
generated).

After the refactor, this module would not work now with necessary updates in
the code.
"""

try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3
    

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
                description = []
                next_line = lines.next()

                # store lines till an H4 (explanation) is encountered
                while not next_line.startswith("#### "):
                    description.append(next_line)
                    next_line = lines.next()

                explanation = []
                # store lines again until --- or another H3 is encountered
                while not (next_line.startswith("---") or
                           next_line.startswith("### ")):
                    explanation.append(next_line)
                    next_line = lines.next()

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

'''
# Create a file
file_content = "\n\n".join([snip["title"] for snip in snippets])

with open("add_categories", "w") as f:
    f.write(file_content)
'''

snips_by_title = {}

with open("add_categories", "r") as f:
    content = iter(f.readlines())
    try:
        while True:
            title = content.next()
            cat = content.next().strip()
            is_new = True if cat[-1]=="*" else False
            cat = cat.replace('*','')
            snips_by_title[title] = {
                "category": cat,
                "is_new": is_new
            }
            content.next()
    except StopIteration:
        pass

for idx, snip in enumerate(snippets):
    snippets[idx]["category"] = snips_by_title[snip["title"]]["category"]
    snippets[idx]["is_new"] = snips_by_title[snip["title"]]["is_new"]


snips_by_cat = {}
for snip in snippets:
    cat = snip["category"]
    if not snips_by_cat.get(cat):
        snips_by_cat[cat] = []
    snips_by_cat[cat].append(snip)

snippet_template = """

### ▶ {title}{is_new}

{description}

{explanation}

---
"""

category_template = """
---

## {category}

{content}
"""

result = ""

category_names = {
    "a": "Appearances are Deceptive!",
    "t": "The Hiddent treasures",
    "f": "Strain your Brain",
    "c": "Be careful of these",
    "m": "Miscallaneous"
}

categories_in_order = ["a", "t", "f", "c", "m"]

for category in categories_in_order:
    snips = snips_by_cat[category]
    for i, snip in enumerate(snips):
        print(i, ":", snip["title"])
    content = ""
    for _ in snips:
        snip = snips[int(raw_input())]
        is_new = " *" if snip["is_new"] else ""
        content += snippet_template.format(title=snip["title"].strip(),
                                           is_new=is_new,
                                           description=snip["description"].strip().replace("\n\n", "\n"),
                                           explanation=snip["explanation"].strip().replace("\n\n", "\n"))
    result += category_template.format(category=category_names[category], content=content.replace("\n\n\n", "\n\n"))

with open("generated.md", "w") as f:
    f.write(result.replace("\n\n\n", "\n\n"))

print("Done!")
