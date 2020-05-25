from tkinter import LabelFrame


class DocGenSection:
    def __init__(self, doc_gens: [], doc_deps: [], name = ""):
        self._docs_gens = doc_gens
        self._doc_deps = doc_deps
        self._name = name

    def draw(self, scrollable_body):
        section_frame = LabelFrame(
            scrollable_body,
            text=self._name,
            fg="blue",
            bg="#37faac",
            labelanchor="n",
            padx=5,
            pady=5

        )
        for i in self._docs_gens:
            i.draw(section_frame)
        for i in self._doc_deps:
            i.draw(section_frame)