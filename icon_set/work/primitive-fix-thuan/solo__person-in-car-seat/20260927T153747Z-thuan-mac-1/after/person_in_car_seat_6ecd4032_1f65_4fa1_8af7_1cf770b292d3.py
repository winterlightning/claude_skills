"""Person in Car Seat.
Plan: Seated figure with circular head, bent knees and supporting seat back; exact detached head gap.
References: supplied source; no useful exact Lucide match.
Native SOLO48 construction, no cross-family scaling.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6ecd4032-1f65-4fa1-8af7-1cf770b292d3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-in-car-seat/20260927T153747Z-thuan-mac-1/reference/person with seat_6ecd4032-1f65-4fa1-8af7-1cf770b292d3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'person-in-car-seat'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('sub icon', 'person', 'in', 'car', 'seat')
    def build(self):
        # The seat cradles a seated figure whose forearm extends forward.
        self.add_arc('head-top', (19, 11), (29, 11), radius_x=5)
        self.add_arc('head-bottom', (29, 11), (19, 11), radius_x=5)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('torso', (24, 24), (24, 32))
        self.add_polyline('legs', (24, 32), (34, 32), (42, 40))
        self.add_line('arm', (24, 24), (40, 24))
        self.add_line('seat-back', (6, 23), (6, 34))
        self.add_arc('seat-turn', (6, 34), (14, 42), radius_x=8, sweep=False)
        self.add_line('seat-base', (14, 42), (32, 42))
        self.relate('connect', 'seat-back', 'seat-turn')
        self.relate('connect', 'seat-turn', 'seat-base')
        self.relate('connect', 'torso', 'legs')
        self.relate('connect', 'torso', 'arm')
        self.mark_human_figure('person', head='head', torso='torso', torso_junction='start')
