from os.path import dirname, join, realpath

import pydoc
try:
    from urllib.request import urlretrieve
except ImportError:
    from urllib import urlretrieve

url = ("http://raw.githubusercontent.com/satwikkansal/"
       "hasem-ishmorpython/master/README.md")

file_path = join(dirname(dirname(realpath(__file__))), "content.md")


def fetch_updated_doc():
    """
    Fetch the latest version of the file at `url` and save it to `file_path`.
    If anything goes wrong, do nothing.
    """
    try:
        print("Fetching the latest version...")
        urlretrieve(url, file_path)
        print("Done!")
    except Exception as e:
        print(e)
        print("Uh oh, failed to check for the latest version, "
              "using the local version for now.")


def render_doc():
    with open(file_path, 'r', encoding="utf-8") as f:
        content = f.read()
        pydoc.pager(content)


def load_and_read():
    fetch_updated_doc()
    render_doc()


if __name__== "__main__":
    load_and_read()
