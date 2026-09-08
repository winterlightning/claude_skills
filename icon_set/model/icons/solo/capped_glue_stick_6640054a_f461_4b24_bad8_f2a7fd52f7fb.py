"""Capped glue stick with label and twist base. VRECT_M (11,2)-(37,46) preserves tall tube proportions. Simple tangent circular corners; no useful exact Lucide match. Fine base grooves omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6640054a-f461-4b24-bad8-f2a7fd52f7fb'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-04/paper glue_6640054a-f461-4b24-bad8-f2a7fd52f7fb.svg'
AUTHOR = 'gpt-6'


class CappedGlueStick(Solo48):
    icon_id = 'capped-glue-stick'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/decoration"
    aliases = ()
    keywords = ('glue', 'stick', 'adhesive', 'paper', 'craft', 'stationery', 'cap')

    def build(self) -> None:
        self.add_line('top', (15, 2), (33, 2))
        self.add_arc('tr', (33, 2), (37, 6), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('right', (37, 6), (37, 42))
        self.add_arc('br', (37, 42), (33, 46), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('bottom', (33, 46), (15, 46))
        self.add_arc('bl', (15, 46), (11, 42), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('left', (11, 42), (11, 6))
        self.add_arc('tl', (11, 6), (15, 2), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('body', 'top', 'tr', 'right', 'br', 'bottom', 'bl', 'left', 'tl', closed=True)
        self.add_line('cap', (11, 13), (37, 13))
        self.relate('connect', 'cap', 'body')
        self.add_line('base', (11, 38), (37, 38))
        self.relate('connect', 'base', 'body')
        self.add_polyline('label', (20, 21), (28, 21), (28, 30), (20, 30), closed=True)
