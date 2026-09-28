"""A horizontal battery has a rounded rectangular case and a short projecting terminal on the right. One hollow rectangular charge block occupies the left portion, leaving most of the case interior open."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b63f7e34-fcd6-4615-82e7-c5f15c2f13a5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__medium-battery-gauge/20260927T133815Z-thuan-mac-1/reference/charging battery medium_b63f7e34-fcd6-4615-82e7-c5f15c2f13a5.svg'
AUTHOR = "gpt-6"

class MobileIcon(Solo48):
    icon_id = 'medium-battery-gauge'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "mobile"
    categories = ("mobile", "primitives")
    aliases = ()
    keywords = ('battery', 'medium', 'charge', 'power', 'energy', 'level', 'indicator')

    def build(self):
        # Horizontal battery case and its attached terminal share one outline.
        parts = []
        def line(name, a, b):
            self.add_line(name, a, b)
            parts.append(name)
        def arc(name, a, b, radius):
            self.add_arc(name, a, b, radius_x=radius, sweep=True)
            parts.append(name)
        line('top', (8, 8), (36, 8))
        arc('top-right', (36, 8), (40, 12), 4)
        line('right-upper', (40, 12), (40, 20))
        line('terminal-top', (40, 20), (42, 20))
        arc('terminal-top-round', (42, 20), (44, 22), 2)
        line('terminal-end', (44, 22), (44, 26))
        arc('terminal-bottom-round', (44, 26), (42, 28), 2)
        line('terminal-bottom', (42, 28), (40, 28))
        line('right-lower', (40, 28), (40, 36))
        arc('bottom-right', (40, 36), (36, 40), 4)
        line('bottom', (36, 40), (8, 40))
        arc('bottom-left', (8, 40), (4, 36), 4)
        line('left', (4, 36), (4, 12))
        arc('top-left', (4, 12), (8, 8), 4)
        self.add_contour('battery-case', *parts, closed=True)
        self.add_polyline('level-gauge', (13, 17), (25, 17), (25, 31), (13, 31), closed=True)
