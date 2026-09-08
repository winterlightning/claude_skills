"""Frog with paired eye bulges and lens-shaped mouth; centerline extremes (2,8)-(46,40). Mirrored radii and spacing, no added pupils; no useful Lucide match."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'de82f94b-4b63-5902-9b4d-4f8c91eabd43'
SOURCE_PATH = 'pictographic-primitives/animals/amphibian frog_de82f94b-4b63-5902-9b4d-4f8c91eabd43.svg'
AUTHOR = 'gpt-6'


class FrogHead(Solo48):
    icon_id = 'frog-head'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('frog', 'amphibian', 'head', 'face', 'toad', 'animal', 'pond', 'nature')

    def build(self) -> None:
        # Frog with paired eye bulges and lens-shaped mouth; centerline extremes (2,8)-(46,40). Mirrored radii and spacing, no added pupils; no useful Lucide match.
        self.add_line('left-cheek', (2, 28), (2, 16))
        self.add_arc('left-eye', (2, 16), (18, 16), radius_x=8, radius_y=8, sweep=True)
        self.add_line('brow', (18, 16), (30, 16))
        self.add_arc('right-eye', (30, 16), (46, 16), radius_x=8, radius_y=8, sweep=True)
        self.add_line('right-cheek', (46, 16), (46, 28))
        self.add_contour('skull', 'left-cheek', 'left-eye', 'brow', 'right-eye', 'right-cheek', closed=False)
        self.add_arc('mouth-top', (2, 28), (46, 28), radius_x=22, radius_y=3, sweep=True)
        self.add_arc('mouth-bottom', (46, 28), (2, 28), radius_x=22, radius_y=12, sweep=True)
        self.add_contour('mouth', 'mouth-top', 'mouth-bottom', closed=True)
        self.relate("connect", 'mouth', 'skull')
