"""Front-facing domed penguin face with paired eyes and pointed beak. Mirrored quarter ellipses preserve smooth dome; no useful exact Lucide match."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7fb9d8b6-5c9c-4e36-aceb-97028cd8dac8'
SOURCE_PATH = 'pictographic-primitives/animals/bird_7fb9d8b6-5c9c-4e36-aceb-97028cd8dac8.svg'
AUTHOR = 'gpt-6'


class PenguinFace(Solo48):
    icon_id = 'penguin-face'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/animals"
    aliases = ()
    keywords = ('penguin', 'bird', 'face', 'head', 'beak', 'chick', 'animal', 'minimal')

    def build(self) -> None:
        # HRECT_XL centerline extremes recorded in batch-02-review.md.
        self.add_line('shoulder-left', (2, 43), (8, 29))
        self.add_line('cheek-left', (8, 29), (8, 21))
        self.add_arc('dome-left', (8, 21), (24, 5), radius_x=16, radius_y=16, sweep=True)
        self.add_arc('dome-right', (24, 5), (40, 21), radius_x=16, radius_y=16, sweep=True)
        self.add_line('cheek-right', (40, 21), (40, 29))
        self.add_line('shoulder-right', (40, 29), (46, 43))
        self.add_contour('head', 'shoulder-left', 'cheek-left', 'dome-left', 'dome-right', 'cheek-right', 'shoulder-right', closed=False)
        self.add_line('eye-left', (16, 21), (16, 23))
        self.add_line('eye-right', (32, 21), (32, 23))
        self.add_line('beak-1', (19, 32), (24, 40))
        self.add_line('beak-2', (24, 40), (29, 32))
        self.add_contour('beak', 'beak-1', 'beak-2', closed=False)
