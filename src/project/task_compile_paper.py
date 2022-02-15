import shutil

import pytask
from project.config import BLD
from project.config import ROOT
from project.config import SRC


DEPENDENCIES = [
    SRC / "slides" / doc for doc in ("slides.tex", "preamble.tex")
]


@pytask.mark.latex(
    [
        "--pdf",
        "--interaction=nonstopmode",
        "--synctex=1",
        "--cd",
        "--quiet",
        "--shell-escape",
    ]
)
@pytask.mark.depends_on(DEPENDENCIES)
@pytask.mark.produces(BLD / "slides" / "slides.pdf")
def task_compile_documents():
    pass


@pytask.mark.depends_on(BLD / "slides" / "slides.pdf")
@pytask.mark.produces(ROOT / "slides.pdf")
def task_copy_to_root(depends_on, produces):
    shutil.copy(depends_on, produces)
