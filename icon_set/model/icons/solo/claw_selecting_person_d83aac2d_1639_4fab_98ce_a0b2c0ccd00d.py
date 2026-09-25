"""A mechanical claw hangs above the central person in a group of three busts. Two angled pincers extend from a circular joint, framing the central head while partial figures flank it.
Lucide user construction; no exact claw selection match. Joint, paired pincers, central person and partial flanking busts retained. Symmetric scene.
SQUARE: centerline extremes (6,6)-(42,42); independently authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd83aac2d-1639-4fab-98ce-a0b2c0ccd00d'
SOURCE_PATH = 'pictographic-primitives/work/recruiting employee crane pick_d83aac2d-1639-4fab-98ce-a0b2c0ccd00d.svg'
AUTHOR = 'gpt-6'


class ClawSelectingPerson(Solo48):
    icon_id = 'claw-selecting-person'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "work"
    categories = ("work", "primitives")
    aliases = ()
    keywords = ('claw', 'person', 'recruiting', 'selection', 'team', 'employee')

    def build(self) -> None:
        self.add_arc('central-head-top', (21, 28), (27, 28), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('central-head-bottom', (27, 28), (21, 28), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_contour('central-head', 'central-head-top', 'central-head-bottom', closed=True)
        self.add_arc('central-left', (14, 42), (24, 40), radius_x=10, radius_y=2, sweep=True, large_arc=False)
        self.add_arc('central-right', (24, 40), (34, 42), radius_x=10, radius_y=2, sweep=True, large_arc=False)
        self.add_contour('central-bust', 'central-left', 'central-right', closed=False)
        self.add_arc('side-head-left-top', (8, 28), (12, 28), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_arc('side-head-left-bottom', (12, 28), (8, 28), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_contour('side-head-left', 'side-head-left-top', 'side-head-left-bottom', closed=True)
        self.add_arc('side-bust-left', (6, 42), (14, 42), radius_x=4, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('side-head-right-top', (36, 28), (40, 28), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_arc('side-head-right-bottom', (40, 28), (36, 28), radius_x=2, radius_y=2, sweep=True, large_arc=False)
        self.add_contour('side-head-right', 'side-head-right-top', 'side-head-right-bottom', closed=True)
        self.add_arc('side-bust-right', (34, 42), (42, 42), radius_x=4, radius_y=3, sweep=True, large_arc=False)
        self.relate("connect", 'central-bust', 'side-bust-left')
        self.relate("connect", 'central-bust', 'side-bust-right')
        self.add_line('cable', (24, 6), (24, 9))
        self.add_arc('joint-top', (21, 12), (27, 12), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('joint-bottom', (27, 12), (21, 12), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_contour('joint', 'joint-top', 'joint-bottom', closed=True)
        self.relate("connect", 'joint', 'cable')
        self.add_polyline('claw-left', (21, 12), (13, 16), (14, 18), closed=False)
        self.add_polyline('claw-right', (27, 12), (35, 16), (34, 18), closed=False)
        self.relate("connect", 'claw-left', 'joint')
        self.relate("connect", 'claw-right', 'joint')
