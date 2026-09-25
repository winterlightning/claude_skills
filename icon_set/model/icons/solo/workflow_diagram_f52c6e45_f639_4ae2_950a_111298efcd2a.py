"""Four rounded rectangular nodes form two staggered columns. Right-angled connecting lines run from the two left nodes into a central vertical branch and outward toward the right-hand nodes.
Lucide workflow orthogonal branches and repeated rounded nodes. Four staggered boxes share dimensions and corner radii; connector spacing is regular. Text omitted.
SQUARE: centerline extremes (6,6)-(42,42); freshly authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f52c6e45-f639-4ae2-950a-111298efcd2a'
SOURCE_PATH = 'pictographic-primitives/work/workflow gantt chart_f52c6e45-f639-4ae2-950a-111298efcd2a.svg'
AUTHOR = 'gpt-6'


class WorkflowDiagram(Solo48):
    icon_id = 'workflow-diagram'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "work"
    aliases = ()
    keywords = ('workflow', 'diagram', 'flowchart', 'node', 'connection', 'process')

    def build(self) -> None:
        self.add_line('a-t', (7, 6), (13, 6))
        self.add_arc('a-ne', (13, 6), (14, 7), radius_x=1, radius_y=1, sweep=True, large_arc=False)
        self.add_line('a-r', (14, 7), (14, 13))
        self.add_arc('a-se', (14, 13), (13, 14), radius_x=1, radius_y=1, sweep=True, large_arc=False)
        self.add_line('a-b', (13, 14), (7, 14))
        self.add_arc('a-sw', (7, 14), (6, 13), radius_x=1, radius_y=1, sweep=True, large_arc=False)
        self.add_line('a-l', (6, 13), (6, 7))
        self.add_arc('a-nw', (6, 7), (7, 6), radius_x=1, radius_y=1, sweep=True, large_arc=False)
        self.add_contour('a', 'a-t', 'a-ne', 'a-r', 'a-se', 'a-b', 'a-sw', 'a-l', 'a-nw', closed=True)
        self.add_line('b-t', (7, 24), (13, 24))
        self.add_arc('b-ne', (13, 24), (14, 25), radius_x=1, radius_y=1, sweep=True, large_arc=False)
        self.add_line('b-r', (14, 25), (14, 31))
        self.add_arc('b-se', (14, 31), (13, 32), radius_x=1, radius_y=1, sweep=True, large_arc=False)
        self.add_line('b-b', (13, 32), (7, 32))
        self.add_arc('b-sw', (7, 32), (6, 31), radius_x=1, radius_y=1, sweep=True, large_arc=False)
        self.add_line('b-l', (6, 31), (6, 25))
        self.add_arc('b-nw', (6, 25), (7, 24), radius_x=1, radius_y=1, sweep=True, large_arc=False)
        self.add_contour('b', 'b-t', 'b-ne', 'b-r', 'b-se', 'b-b', 'b-sw', 'b-l', 'b-nw', closed=True)
        self.add_line('c-t', (35, 16), (41, 16))
        self.add_arc('c-ne', (41, 16), (42, 17), radius_x=1, radius_y=1, sweep=True, large_arc=False)
        self.add_line('c-r', (42, 17), (42, 23))
        self.add_arc('c-se', (42, 23), (41, 24), radius_x=1, radius_y=1, sweep=True, large_arc=False)
        self.add_line('c-b', (41, 24), (35, 24))
        self.add_arc('c-sw', (35, 24), (34, 23), radius_x=1, radius_y=1, sweep=True, large_arc=False)
        self.add_line('c-l', (34, 23), (34, 17))
        self.add_arc('c-nw', (34, 17), (35, 16), radius_x=1, radius_y=1, sweep=True, large_arc=False)
        self.add_contour('c', 'c-t', 'c-ne', 'c-r', 'c-se', 'c-b', 'c-sw', 'c-l', 'c-nw', closed=True)
        self.add_line('e-t', (35, 34), (41, 34))
        self.add_arc('e-ne', (41, 34), (42, 35), radius_x=1, radius_y=1, sweep=True, large_arc=False)
        self.add_line('e-r', (42, 35), (42, 41))
        self.add_arc('e-se', (42, 41), (41, 42), radius_x=1, radius_y=1, sweep=True, large_arc=False)
        self.add_line('e-b', (41, 42), (35, 42))
        self.add_arc('e-sw', (35, 42), (34, 41), radius_x=1, radius_y=1, sweep=True, large_arc=False)
        self.add_line('e-l', (34, 41), (34, 35))
        self.add_arc('e-nw', (34, 35), (35, 34), radius_x=1, radius_y=1, sweep=True, large_arc=False)
        self.add_contour('e', 'e-t', 'e-ne', 'e-r', 'e-se', 'e-b', 'e-sw', 'e-l', 'e-nw', closed=True)
        self.add_polyline('upper-link', (14, 10), (24, 10), (24, 20), (34, 20), closed=False)
        self.relate("connect", 'upper-link', 'a')
        self.relate("connect", 'upper-link', 'c')
        self.add_polyline('lower-link', (14, 28), (24, 28), (24, 38), (34, 38), closed=False)
        self.relate("connect", 'lower-link', 'b')
        self.relate("connect", 'lower-link', 'e')
        self.add_line('branch', (24, 20), (24, 28))
        self.relate("connect", 'branch', 'upper-link')
        self.relate("connect", 'branch', 'lower-link')
