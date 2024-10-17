from typing import TYPE_CHECKING

import nox


if TYPE_CHECKING:
    from nox.sessions import Session

python_versions = ["3.9", "3.10", "3.11", "3.12", "3.13"]

@nox.session(python=python_versions, reuse_venv=True)
def tests(session: "Session") -> None:
    _ = session.run("python", "snippets/2_tricky_strings.py")
