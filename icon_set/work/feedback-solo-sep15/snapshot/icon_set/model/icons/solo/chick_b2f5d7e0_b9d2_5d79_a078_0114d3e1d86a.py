"""Plump right-facing bird with a scooped tail. Lucide bird informs the unified contour; no additional details."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b2f5d7e0-b9d2-5d79-a078-0114d3e1d86a'
SOURCE_PATH = 'pictographic-primitives/animals/chick_b2f5d7e0-b9d2-5d79-a078-0114d3e1d86a.svg'
AUTHOR = 'gpt-6'


class SimpleBirdShape(Solo48):
    icon_id = 'simple-bird-shape'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('bird', 'chick', 'minimal', 'simple', 'silhouette', 'beak', 'shape', 'animal')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_bezier('crown',(14, 16),*(((14.0, 8.70101013), (19.82029825, 4.0), (27.0, 4)), ((34.13477631, 4), (38.5, 8.70101013), (38, 16))))
        self.add_line('brow',(38, 16),(38, 19))
        self.add_line('beak-top',(38, 19),(40, 24))
        self.add_line('beak-bottom',(40, 24),(38, 26))
        self.add_bezier('breast',(38, 26),*(((37.05289561, 35.82808043), (29.65521527, 44), (20, 44)),))
        self.add_bezier('belly',(20, 44),*(((13.56989511, 43.74857189), (9.31300247, 38.17406962), (8, 31)),))
        self.add_line('tail',(8, 31),(10, 31))
        self.add_bezier('scoop',(10, 31),*(((11.98528137, 31.0), (14.0, 28.3137085), (14, 25)),))
        self.add_line('back',(14, 25),(14, 16))
        self.add_contour('outline',*('crown', 'brow', 'beak-top', 'beak-bottom', 'breast', 'belly', 'tail', 'scoop', 'back'),closed=True)
