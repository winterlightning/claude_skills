"""Hammock on Palm Tree. A leaning palm supports a sagging hammock to the right; open frond strokes replace filled leaf outlines, retaining natural asymmetry.
Keyshape SQUARE, visible extremes (4, 4, 44, 44); centerline envelope inset by 2.
Construction: Lucide no useful local palm match; tangent arcs and shared frond junctions. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd9ac80f1-656c-4cf2-beab-ed537dcb386b'
SOURCE_PATH = 'pictographic-primitives/recreation/outdoor beach_d9ac80f1-656c-4cf2-beab-ed537dcb386b.svg'
AUTHOR = 'gpt-6'


class HammockOnPalmTree(Solo48):
    icon_id = 'hammock-on-palm-tree'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "recreation"
    aliases = ()
    keywords = ('hammock', 'on', 'palm', 'tree')

    def build(self) -> None:
        self.add_arc('trunk-lower', (12, 42), (14, 30), radius_x=45, radius_y=45, sweep=True)
        self.add_arc('trunk-upper', (14, 30), (18, 19), radius_x=45, radius_y=45, sweep=True)
        self.add_contour('trunk', 'trunk-lower', 'trunk-upper', closed=False)
        self.add_arc('frond-left', (18, 19), (6, 17), radius_x=12, radius_y=8, sweep=False)
        self.add_arc('frond-top', (18, 19), (10, 6), radius_x=14, radius_y=14, sweep=False)
        self.add_arc('frond-right', (18, 19), (34, 12), radius_x=16, radius_y=12, sweep=True)
        self.add_arc('frond-low', (18, 19), (29, 21), radius_x=12, radius_y=10, sweep=True)
        self.relate("connect", 'trunk', 'frond-left')
        self.relate("connect", 'trunk', 'frond-top')
        self.relate("connect", 'trunk', 'frond-right')
        self.relate("connect", 'trunk', 'frond-low')
        self.relate("connect", 'frond-left', 'frond-top')
        self.relate("connect", 'frond-left', 'frond-right')
        self.relate("connect", 'frond-left', 'frond-low')
        self.relate("connect", 'frond-top', 'frond-right')
        self.relate("connect", 'frond-top', 'frond-low')
        self.relate("connect", 'frond-right', 'frond-low')
        self.add_arc('hammock-bag', (14, 30), (42, 30), radius_x=14, radius_y=12, sweep=False)
        self.add_line('hammock-rim', (42, 30), (14, 30))
        self.add_contour('hammock', 'hammock-bag', 'hammock-rim', closed=True)
        self.relate("connect", 'trunk', 'hammock')
