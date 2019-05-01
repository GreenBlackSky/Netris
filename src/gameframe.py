"""GameFrame class."""

from tkinter import Frame, Entry, Button
from gamescene import GameScene


class GameFrame(Frame):
    """Frame contains game field to play on."""

    def __init__(self, app):
        """Create GameFrame."""
        super().__init__(app)

        Entry(self).grid(column=0, row=0)
        Button(
            self,
            text="Menu",
            command=self.master.main_menu
        ).grid(column=1, row=0)
        self._game_scene = GameScene(self)
        self._game_scene.grid(column=0, columnspan=2, row=1)

    def pack(self, *args, **kargs):
        self._game_scene.run = True
        Frame.pack(self, *args, **kargs)

    def pack_forget(self, *args, **kargs):
        self._game_scene.run = False
        Frame.pack_forget(self, *args, **kargs)
