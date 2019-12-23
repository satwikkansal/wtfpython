"""
An inefficient monolithic piece of code that'll generate jupyter notebook
from the projects main README.

PS: If you are a recruiter, please don't judge me by this piece of code. I wrote it
in hurry. I know this is messy and can be simplified, but I don't want to change it
much because it just works. 

Simplifictions and improvements through patches are more than welcome however :)


#TODOs

- CLI arguments for running this thing
- Add it to prepush hook
- Add support for skip comments, to skip examples that are not meant for notebook environment.
- Use templates?
"""

import json
import os
import pprint

fpath = os.path.join(os.path.dirname( __file__ ), '..', 'README.md')
examples = []

# The globals
current_example = 1
sequence_num = 1
current_section_name = ""


STATEMENT_PREFIXES = ["...", ">>> ", "$ "]

HOSTED_NOTEBOOK_INSTRUCTIONS = """

## Hosted notebook instructions

This is just an experimental attempt of browsing wtfpython through jupyter notebooks. Some examples are read-only because, 
- they either require a version of Python that's not supported in the hosted runtime.
- or they can't be reproduced in the notebook envrinonment.

The expected outputs are already present in collapsed cells following the code cells. The Google colab provides Python2 (2.7) and Python3 (3.6, default) runtimes. You can switch among these for Python2 specific examples. For examples specific to other minor versions, you can simply refer to collapsed outputs (it's not possible to control the minor version in hosted notebooks as of now). You can check the active version using

```py
>>> import sys
>>> sys.version
# Prints out Python version here.
```

That being said, most of the examples do work as expected. If you face any trouble, feel free to consult the original content on wtfpython and create an issue in the repo. Have fun!

---
"""


def generate_code_block(statements, output):
    global sequence_num
    result = {
        "type": "code",
        "sequence_num": sequence_num,
        "statements": statements,
        "output": output
    }
    sequence_num += 1
    return result


def generate_markdown_block(lines):
    global sequence_num
    result = {
        "type": "markdown",
        "sequence_num": sequence_num,
        "value": lines
    }
    sequence_num += 1
    return result


def is_interactive_statement(line):
    for prefix in STATEMENT_PREFIXES:
        if line.lstrip().startswith(prefix):
            return True
    return False


def parse_example_parts(lines, title, current_line):
    parts = {
        "build_up": [],
        "explanation": []
    }
    content = [title]
    statements_so_far = []
    output_so_far = []
    next_line = current_line
    # store build_up till an H4 (explanation) is encountered
    while not (next_line.startswith("#### ")or next_line.startswith('---')):
        # Watching out for the snippets
        if next_line.startswith("```py"):
            # It's a snippet, whatever found until now is text
            is_interactive = False
            output_encountered = False
            if content:
                parts["build_up"].append(generate_markdown_block(content))
                content = []

            next_line = next(lines)

            while not next_line.startswith("```"):
                if is_interactive_statement(next_line):
                    is_interactive = True
                    if (output_so_far):
                        parts["build_up"].append(generate_code_block(statements_so_far, output_so_far))
                        statements_so_far, output_so_far = [], []
                    statements_so_far.append(next_line)
                else:
                    # can be either output or normal code
                    if is_interactive:
                        output_so_far.append(next_line)
                    elif output_encountered:
                        output_so_far.append(next_line)
                    else:
                        statements_so_far.append(next_line)
                next_line = next(lines)

            # Snippet is over
            parts["build_up"].append(generate_code_block(statements_so_far, output_so_far))
            statements_so_far, output_so_far = [], []
            next_line = next(lines)
        else:
            # It's a text, go on.
            content.append(next_line)
            next_line = next(lines)

    # Explanation encountered, save any content till now (if any)
    if content:
        parts["build_up"].append(generate_markdown_block(content))

    # Reset stuff
    content = []
    statements_so_far, output_so_far = [], []

    # store lines again until --- or another H3 is encountered
    while not (next_line.startswith("---") or
               next_line.startswith("### ")):
        if next_line.lstrip().startswith("```py"):
            # It's a snippet, whatever found until now is text
            is_interactive = False
            if content:
                parts["explanation"].append(generate_markdown_block(content))
                content = []

            next_line = next(lines)

            while not next_line.lstrip().startswith("```"):
                if is_interactive_statement(next_line):
                    is_interactive = True
                    if (output_so_far):
                        parts["explanation"].append(generate_code_block(statements_so_far, output_so_far))
                        statements_so_far, output_so_far = [], []
                    statements_so_far.append(next_line)
                else:
                    # can be either output or normal code
                    if is_interactive:
                        output_so_far.append(next_line)
                    else:
                        statements_so_far.append(next_line)
                next_line = next(lines)

            # Snippet is over
            parts["explanation"].append(generate_code_block(statements_so_far, output_so_far))
            statements_so_far, output_so_far = [], []
            next_line = next(lines)
        else:
            # It's a text, go on.
            content.append(next_line)
            next_line = next(lines)

    # All done
    if content:
        parts["explanation"].append(generate_markdown_block(content))

    return next_line, parts


def remove_from_beginning(tokens, line):
    for token in tokens:
        if line.lstrip().startswith(token):
            line = line.replace(token, "")
    return line


def inspect_and_sanitize_code_lines(lines):
    tokens_to_remove = STATEMENT_PREFIXES
    result = []
    is_print_present = False
    for line in lines:
        line = remove_from_beginning(tokens_to_remove, line)
        if line.startswith("print ") or line.startswith("print("):
            is_print_present = True
        result.append(line)
    return is_print_present, result


def convert_to_cells(cell_contents, read_only):
    cells = []
    for stuff in cell_contents:
        if stuff["type"] == "markdown":
            # todo add metadata later
            cells.append(
                {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": stuff["value"]
                }
            )
        elif stuff["type"] == "code":
            if read_only:
                # Skip read only
                # TODO: Fix
                cells.append(
                {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": ["```py\n"] + stuff["statements"] + ["```\n"] + ["```py\n"] + stuff['output'] + ["```\n"]
                    }
                )
                continue

            is_print_present, sanitized_code = inspect_and_sanitize_code_lines(stuff["statements"])
            if is_print_present:
                cells.append(
                    {
                        "cell_type": "code",
                        "metadata": {
                            "collapsed": True,

                        },
                        "execution_count": None,
                        "outputs": [{
                            "name": "stdout",
                            "output_type": "stream",
                            "text": stuff["output"]
                        }],
                        "source": sanitized_code
                    }
                )
            else:
                cells.append(
                    {
                        "cell_type": "code",
                        "execution_count": None,
                        "metadata": {
                            "collapsed": True
                        },
                        "outputs": [{
                            "data": {
                                "text/plain": stuff["output"]
                            },
                            "output_type": "execute_result",
                            "metadata": {},
                            "execution_count": None
                        }],
                        "source": sanitized_code
                    }
                )

    return cells


def convert_to_notebook(pre_examples_content, parsed_json, post_examples_content):
    result = {
        "cells": [],
        "metadata": {},
        "nbformat": 4,
        "nbformat_minor": 2
    }

    notebook_path = "wtf.ipynb"

    result["cells"] += convert_to_cells([generate_markdown_block(pre_examples_content)], False)

    for example in parsed_json:
        parts = example["parts"]
        build_up = parts.get("build_up")
        explanation = parts.get("explanation")
        read_only = example.get("read_only")

        if build_up:
            result["cells"] += convert_to_cells(build_up, read_only)

        if explanation:
            result["cells"] += convert_to_cells(explanation, read_only)

    result["cells"] += convert_to_cells([generate_markdown_block(post_examples_content)], False)

    #pprint.pprint(result, indent=2)
    with open(notebook_path, "w") as f:
        json.dump(result, f, indent=2)


with open(fpath, 'r+', encoding="utf-8") as f:
    lines = iter(f.readlines())
    line = next(lines)
    result = []
    pre_examples_phase = True
    pre_stuff = []
    post_stuff = []
    try:
        while True:
            if line.startswith("## "):
                pre_examples_phase = False
                # A section is encountered
                current_section_name = line.replace("## ", "").strip()
                section_text = []
                line = next(lines)
                # Until a new section is encountered
                while not (line.startswith("## ") or line.startswith("# ")):
                    # check if it's a H3
                    if line.startswith("### "):
                        # An example is encountered
                        title_line = line
                        line = next(lines)
                        read_only = False
                        while line.strip() == "" or line.startswith('<!--'):
                            #TODO: Capture example ID here using regex.
                            if '<!-- read-only -->' in line:
                                read_only = True
                            line = next(lines)

                        example_details = {
                            "id": current_example,
                            "title": title_line.replace("### ", ""),
                            "section": current_section_name,
                            "read_only": read_only
                        }
                        line, example_details["parts"] = parse_example_parts(lines, title_line, line)
                        result.append(example_details)
                        current_example += 1
                    else:
                        section_text.append(line)
                        line = next(lines)
            else:
                if pre_examples_phase:
                    pre_stuff.append(line)
                else:
                    post_stuff.append(line)
                line = next(lines)

    except StopIteration as e:
        #pprint.pprint(result, indent=2)
        pre_stuff.append(HOSTED_NOTEBOOK_INSTRUCTIONS)
        result.sort(key = lambda x: x["read_only"])
        convert_to_notebook(pre_stuff, result, post_stuff)
