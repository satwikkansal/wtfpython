## Generating the notebook

- Expand the relative links in README.md to absolute ones
- Remove the TOC in README.md (because Google colab generates its own anyway)
- Reorder the examples, so that the ones that work are upfront.
- Run the `notebook_generator.py`, it will generate a notebook named `wtf.ipynb`
- Revert the README.md changes (optional)


# Hosted notebook instructions

This is just an experimental attempt of browsing wtfpython through jupyter notebooks. Some examples are read-only because, 
- they either require a version of Python that's not supported in the hosted runtime.
- or they can't be reproduced in the notebook envrinonment.

The expected outputs are already present in collapsed cells following the code cells. The Google colab provides Python2 (2.7) and Python3 (3.6, default) runtimes. You can switch among these for Python2 specific examples. For examples specific to other minor versions, you can simply refer to collapsed outputs (it's not possible to control the minor version in hosted notebooks as of now). You can check the active version using

```py
>>> import sys
>>> sys.version
# Prints out Python version here.
```

That being said, most of tbe examples do work as expected. If you face any trouble, feel free to consult the original content on wtfpython and create an issue in the repo. Have fun!


