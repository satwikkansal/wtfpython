All kinds of patches are welcome. Feel free to even suggest some catchy and funny titles for the existing Examples. The goal is to make this collection as interesting to read as possible. Here are a few ways through which you can contribute,

- If you are interested in translating the project to another language (some people have done that in the past), please feel free to open up an issue, and let me know if you need any kind of help.
- If the changes you suggest are significant, filing an issue before submitting the actual patch will be appreciated. If you'd like to work on the issue (highly encouraged), you can mention that you're interested in working on it while creating the issue and get assigned to it.
- If you're adding a new example, it is highly recommended to create an issue to discuss it before submitting a patch. You can use the following template for adding a new example:

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
  **Output:**
  ```py
  >>> trigger # some example that makes it easy to unveil the magic
  # some justified output
  ```
```
</pre>


Few things that you can consider while writing an example, 

- If you are choosing to submit a new example without creating an issue and discussing, please check the project to make sure there aren't similar examples already.
- Try to be consistent with the namings and the values you use with the variables. For instance, most variable names in the project are along the lines of `some_string`, `some_list`, `some_dict`, etc. You'd see a lot of `x`s for single letter variable names, and `"wtf"` as values for strings. There's no strictly enforced scheme in the project as such, but you can take a glance at other examples to get a gist.
- Try to be as creative as possible to add that element of "surprise" in the setting up part of an example. Sometimes this may mean writing a snippet a sane programmer would never write.
- Also, feel free to add your name to the [contributors list](/CONTRIBUTORS.md).

**Some FAQs**

    What is is this after every snippet title (###) in the README: <!-- Example ID: 30f1d3fc-e267-4b30-84ef-4d9e7091ac1a --->? Should it be added manually or can it be ignored when creating new snippets?

That's a random UUID, it is used to keep identify the examples across multiple translations of the project. As a contributor, you don't have to worry about behind the scenes of how it is used, you just have to add a new random UUID to new examples in that format.

    Where should new snippets be added? Top/bottom of the section, doesn't ?

There are multiple things that are considered to decide the order (the dependency on the other examples, difficulty level, category, etc). I'd suggest simply adding the new example at the bottom of a section you find more fitting (or just add it to the Miscellaneous section). Its order will be taken care of in future revisions.

    What's the difference between the sections (the first two feel very similar)?

The section "Strain your brain" contains more contrived examples that you may not really encounter in real life, whereas the section "Slippery Slopes" contains examples that have the potential to be encountered more frequently while programming.

    Before the table of contents it says that markdown-toc -i README.md --maxdepth 3 was used to create it. The pip package markdown-toc does not contain either -i or --maxdepth flags. Which package is meant, or what version of that package?
    Should the new table of contents entry for the snippet be created with the above command or created manually (in case the above command does more than only add the entry)?

We use the [markdown-toc](https://www.npmjs.com/package/markdown-toc) npm package to generate ToC. It has some issues with special characters though (I'm not sure if it's fixed yet). More often than not, I just end up inserting the toc link manually at the right place. The tool is handy when I have to big reordering, otherwise just updating toc manually is more convenient imo.

If you have any questions feel free to ask on [this issue](https://github.com/satwikkansal/wtfpython/issues/269) (thanks to [@LiquidFun](https://github.com/LiquidFun) for starting it).
