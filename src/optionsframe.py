"""OptionsFrame class."""

from tkinter import Frame, Label, Button, Scale, HORIZONTAL, X, Y
from tkinter.ttk import Combobox

from gamescene import GameScene


class OptionsFrame(Frame):
    """Contains widgets to tune game."""

    def __init__(self, app):
        """Create OptionsFrame."""
        super().__init__(app)

        GameScene(self).pack(fill=Y)

        Label(self, text='Appearance:').pack()
        values = ["Light", "Dark", "Dracula", "Monokai"]
        Combobox(self, values=values).pack(fill=X, expand=True)

        Label(self, text='Cell size:').pack()
        Scale(self, from_=1, to=5, orient=HORIZONTAL).pack(fill=X, expand=True)

        Label(self, text='Speed:').pack()
        Scale(
            self,
            from_=1, to=10,
            orient=HORIZONTAL
        ).pack(fill=X, expand=True)

        Button(self, text="Drop record table").pack()

        Button(self, text="Menu", command=self.master.main_menu).pack()
