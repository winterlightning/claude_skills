"""Dome Pendant Lamp. VRECT_L centerlines (8,6)-(40,42): vertical cord, semicircular dome and exposed bulb. Omit the small cap; retain the circular shade and bulb.
Lucide lamp-ceiling / lamp-floor inform simple shades and explicit support joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '590e3124-67e7-5ef1-9f35-c589ee85cdd4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__dome-pendant-lamp/20260926T173134Z-thuan-mac-1/reference/table lamp hanging_590e3124-67e7-5ef1-9f35-c589ee85cdd4.svg'
AUTHOR = "gpt-6"

class DomePendantLamp(Solo48):
    icon_id = 'dome-pendant-lamp'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'lamps'
    categories = ('lamps', 'primitives')
    aliases = ()
    keywords = ('lamp', 'pendant', 'dome', 'shade', 'bulb', 'ceiling')

    def build(self) -> None:
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.
        self.add_line('cord', (24, 4), (24, 18))
        self.add_arc('dome-left', (8, 34), (24, 18), radius_x=16, sweep=True)
        self.add_arc('dome-right', (24, 18), (40, 34), radius_x=16, sweep=True)
        self.add_polyline('rim', (40, 34), (34, 34), (14, 34), (8, 34))
        self.add_arc('bulb', (34, 34), (14, 34), radius_x=10, sweep=True)
        self.relate('connect', 'bulb', 'rim')
        self.add_contour('shade', 'dome-left', 'dome-right')
        self.relate('connect', 'shade', 'rim')
        self.relate('connect', 'shade', 'cord')
