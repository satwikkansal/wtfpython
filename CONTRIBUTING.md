All kinds of patches are welcome. Feel free to even suggest some catchy and funny titles for the existing Examples. The goal is to make this collection as interesting to read as possible.

If you are interested in translating the project to another language (some people have done that in the past), please feel free to open up an issue or ping on the [gitter channel](https://gitter.im/wtfpython/Lobby) if you need any kind of help.

If the changes you suggest are significant, filing an issue before submitting the actual patch will be appreciated. If you'd like to work on the issue (highly encouraged), you can mention that you're interested in working on it while creating the issue and get assigned to it.

If you're adding a new example, please do create an issue to discuss it before submitting a patch.

You can use the following template for adding a new example:

<pre>
### ▶ Some fancy Title *
The asterisk at the end of the title indicates the example was not present in the first release and has been recently added.

```py
# Setting up the code.
# Preparation for the magic...
```

**Output (Python version):**
```py
>>> triggering_statement
Probably unexpected output
```
(Optional): One line describing the unexpected output.

#### 💡 Explanation:
* Brief explanation of what's happening and why is it happening.
  ```py
  Setting up examples for clarification (if necessary)
  ```
  **Outupt:**
  ```py
  >>> trigger # some example that makes it easy to unveil the magic
  # some justified output
  ```
```
</pre>


Few things that you can consider while writing an example, 

- Try to be consistent with the namings and the values you use with the variables. For instance, most variable names in the project are along the lines of `some_string`, `some_list`, `some_dict`, etc. You'd see a lot of `x`s for single letter variable names, and `"wtf"` as values for strings. There's strictly enforced scheme in the project, but you can take a glance at other examples to get a gist.
- Try to be as creative as possible to add that element of "surprise" in the setting up part of an example. Sometimes this may mean writing a snippet a sane programmer would never write.
- Also, please don't forget to add your name to the [contributors list](/CONTRIBUTING.md).