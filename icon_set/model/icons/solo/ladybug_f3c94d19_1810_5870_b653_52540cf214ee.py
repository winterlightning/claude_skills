"""Top-view ladybug. Lucide bug informs bilateral legs, dome and wing seam. Source has no spots; antenna hooks reduced to clear strokes."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f3c94d19-1810-5870-b653-52540cf214ee'
SOURCE_PATH = 'pictographic-primitives/animals/ladybug_f3c94d19-1810-5870-b653-52540cf214ee.svg'
AUTHOR = 'gpt-6'


class Ladybug(Solo48):
    icon_id = 'ladybug'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('ladybug', 'ladybird', 'beetle', 'insect', 'bug', 'spots', 'garden', 'luck')

    def build(self) -> None:
        # Exact visible extremes: (0, 0, 48, 48); centerline inset 2.
        self.add_arc('wing-0', (24, 16), (33, 19), radius_x=15, radius_y=15, sweep=True, large_arc=False)
        self.add_arc('wing-1', (33, 19), (39, 31), radius_x=15, radius_y=15, sweep=True, large_arc=False)
        self.add_arc('wing-2', (39, 31), (33, 43), radius_x=15, radius_y=15, sweep=True, large_arc=False)
        self.add_arc('wing-3', (33, 43), (24, 46), radius_x=15, radius_y=15, sweep=True, large_arc=False)
        self.add_arc('wing-4', (24, 46), (15, 43), radius_x=15, radius_y=15, sweep=True, large_arc=False)
        self.add_arc('wing-5', (15, 43), (9, 31), radius_x=15, radius_y=15, sweep=True, large_arc=False)
        self.add_arc('wing-6', (9, 31), (15, 19), radius_x=15, radius_y=15, sweep=True, large_arc=False)
        self.add_arc('wing-7', (15, 19), (24, 16), radius_x=15, radius_y=15, sweep=True, large_arc=False)
        self.add_contour('wings', 'wing-0', 'wing-1', 'wing-2', 'wing-3', 'wing-4', 'wing-5', 'wing-6', 'wing-7', closed=True)
        self.add_line('seam', (24, 16), (24, 46))
        self.relate("connect", 'seam', 'wings')
        self.add_arc('head-left', (15, 19), (18, 8), radius_x=10, radius_y=12, sweep=True, large_arc=False)
        self.add_arc('head-top', (18, 8), (30, 8), radius_x=10, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('head-right', (30, 8), (33, 19), radius_x=10, radius_y=12, sweep=True, large_arc=False)
        self.add_contour('head', 'head-left', 'head-top', 'head-right', closed=False)
        self.relate("connect", 'head', 'wings')
        self.add_line('antenna-left', (18, 8), (15, 2))
        self.relate("connect", 'antenna-left', 'head')
        self.add_line('leg-left-top', (15, 19), (5, 14))
        self.relate("connect", 'leg-left-top', 'wings')
        self.add_line('leg-left-middle', (9, 31), (2, 31))
        self.relate("connect", 'leg-left-middle', 'wings')
        self.add_line('leg-left-bottom', (15, 43), (5, 46))
        self.relate("connect", 'leg-left-bottom', 'wings')
        self.add_line('antenna-right', (30, 8), (33, 2))
        self.relate("connect", 'antenna-right', 'head')
        self.add_line('leg-right-top', (33, 19), (43, 14))
        self.relate("connect", 'leg-right-top', 'wings')
        self.add_line('leg-right-middle', (39, 31), (46, 31))
        self.relate("connect", 'leg-right-middle', 'wings')
        self.add_line('leg-right-bottom', (33, 43), (43, 46))
        self.relate("connect", 'leg-right-bottom', 'wings')
