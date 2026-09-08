"""Plump right-facing bird with a scooped tail. Lucide bird informs the unified contour; no additional details."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b2f5d7e0-b9d2-5d79-a078-0114d3e1d86a'
SOURCE_PATH = 'pictographic-primitives/animals/chick_b2f5d7e0-b9d2-5d79-a078-0114d3e1d86a.svg'
AUTHOR = 'gpt-6'


class SimpleBirdShape(Solo48):
    icon_id = 'simple-bird-shape'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('bird', 'chick', 'minimal', 'simple', 'silhouette', 'beak', 'shape', 'animal')

    def build(self) -> None:
        # Visible bounds: (3, 0, 45, 48); centerline inset 2.
        self.add_arc('crown', (14, 16), (40, 16), radius_x=13, radius_y=14, sweep=True)
        self.add_line('brow', (40, 16), (40, 19))
        self.add_line('beak-top', (40, 19), (43, 24))
        self.add_line('beak-bottom', (43, 24), (40, 26))
        self.add_arc('breast', (40, 26), (20, 46), radius_x=20, radius_y=20, sweep=True)
        self.add_arc('belly', (20, 46), (5, 31), radius_x=15, radius_y=15, sweep=True)
        self.add_line('tail', (5, 31), (8, 31))
        self.add_arc('scoop', (8, 31), (14, 25), radius_x=6, radius_y=6, sweep=False)
        self.add_line('back', (14, 25), (14, 16))
        self.add_contour('outline', 'crown', 'brow', 'beak-top', 'beak-bottom', 'breast', 'belly', 'tail', 'scoop', 'back', closed=True)
