"""
An inefficient monolithic piece of code that'll generate jupyter notebook
from the projects main README.

TODO

- CLI arguments for running this thing.
- Add it to prepush hook
- Use templates?

"""

import json
import pprint
fname = "/Users/300041709/code/self/wtfpython/README.md"
examples = []

# The globals
current_example = 1
sequence_num = 1
current_section_name = ""


STATEMENT_PREFIXES = ["...", ">>> ", "$ "]


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
        if line.startswith(prefix):
            return True
    return False

def parse_example_parts(lines, example_title_line):
    parts = {
        "build_up": [],
        "explanation": []
    }
    content = []
    statements_so_far = []
    output_so_far = []
    next_line = example_title_line
    # store build_up till an H4 (explanation) is encountered
    while not next_line.startswith("#### "):
        # Watching out for the snippets
        if next_line.startswith("```"):
            # It's a snippet, whatever found until now is text
            is_interactive = False
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
        if next_line.startswith("```"):
            # It's a snippet, whatever found until now is text
            is_interactive = False
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

    # All done
    if content:
        parts["explanation"].append(generate_markdown_block(content))

    return next_line, parts

def remove_from_beginning(tokens, line):
    for token in tokens:
        if line.startswith(token):
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

def convert_to_cells(cell_contents):
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
            is_print_present, sanitized_code = inspect_and_sanitize_code_lines(stuff["statements"])
            if is_print_present:
                cells.append(
                    {
                        "cell_type": "code",
                        "metadata": {
                            "collapsed": True
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


def convert_to_notebook(parsed_json):
    result = {
        "cells": [],
        "metadata": {},
        "nbformat": 4,
        "nbformat_minor": 2
    }
    for example in parsed_json:
        parts = example["parts"]
        build_up = parts.get("build_up")
        explanation = parts.get("explanation")
        notebook_path = "test.ipynb"

        if(build_up):
            result["cells"] += convert_to_cells(build_up)

        if(explanation):
            result["cells"] += convert_to_cells(explanation)

    pprint.pprint(result, indent=2)
    with open(notebook_path, "w") as f:
        json.dump(result, f)



with open(fname, 'r+', encoding="utf-8") as f:
    lines = iter(f.readlines())
    line = next(lines)
    result = []
    try:
        while True:
            if line.startswith("## "):
                # A section is encountered
                current_section_name = line.replace("## ", "").strip()
                section_text = []
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
                        line, example_details["parts"] = parse_example_parts(lines, line)
                        result.append(example_details)
                        current_example += 1
                    else:
                        section_text.append(line)
                        line = next(lines)
            else:
                line = next(lines)

    except StopIteration:
        pprint.pprint(result, indent=2)
        convert_to_notebook(result)
