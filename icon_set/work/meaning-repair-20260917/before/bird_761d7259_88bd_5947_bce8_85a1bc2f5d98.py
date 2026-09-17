"""Right-facing plump songbird with a long tail and two legs; Lucide bird informs circular head and breast. Directional asymmetry preserves the pose."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '761d7259-88bd-5947-bce8-85a1bc2f5d98'
SOURCE_PATH = 'pictographic-primitives/animals/bird_761d7259-88bd-5947-bce8-85a1bc2f5d98.svg'
AUTHOR = 'gpt-6'


class PerchedSongbird(Solo48):
    icon_id = 'perched-songbird'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/animals"
    aliases = ()
    keywords = ('bird', 'songbird', 'sparrow', 'robin', 'perched', 'wildlife', 'wing', 'garden')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_bezier('head-left', (24, 14), *(((25.47719402, 8.95896372), (29.55412824, 6), (34, 6)),))
        self.add_arc('head-right', (34, 6), (42, 14), radius_x=10, radius_y=12, large_arc=False, sweep=True)
        self.add_line('beak-1', (42, 14), (42, 18))
        self.add_line('beak-2', (42, 18), (40, 22))
        self.add_line('breast-neck', (40, 22), (40, 24))
        self.add_arc('breast', (40, 24), (26, 38), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_line('belly', (26, 38), (18, 38))
        self.add_line('tail-1', (18, 38), (6, 34))
        self.add_line('tail-2', (6, 34), (24, 14))
        self.add_arc('wing', (32, 21), (22, 29), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_line('leg-left-1', (18, 38), (18, 42))
        self.add_line('leg-left-2', (18, 42), (14, 42))
        self.add_line('leg-right-1', (26, 38), (30, 42))
        self.add_line('leg-right-2', (30, 42), (34, 42))
        self.add_contour('outline', *('head-left', 'head-right', 'beak-1', 'beak-2', 'breast-neck', 'breast', 'belly', 'tail-1', 'tail-2'), closed=True)
        self.add_contour('leg-left', *('leg-left-1', 'leg-left-2'), closed=False)
        self.add_contour('leg-right', *('leg-right-1', 'leg-right-2'), closed=False)
        self.relate('connect', *('outline', 'leg-left'))
        self.relate('connect', *('outline', 'leg-right'))
