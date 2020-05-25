from tkinter import Checkbutton, BooleanVar


class DocGen:
    def __init__(self, label: str, templates: list, deps = []):
        self._label = label
        self._templates = templates
        self._deps = deps
        self._var = BooleanVar()

    def draw(self, root_frame):
        Checkbutton(
            root_frame,
            text=self._label,
            variable=self._var
        ).pack(anchor="w")

    def is_checked(self):
        return self._var

    def generate(self, deal_context, dep_context):

    def get_not_filled_deps(self):
        res = []
        for i in self._deps:
            if not i.is_filled():
                res.append(i)
        return res