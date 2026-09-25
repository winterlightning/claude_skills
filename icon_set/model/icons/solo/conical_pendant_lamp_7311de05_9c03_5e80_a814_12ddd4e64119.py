"""Conical Pendant Lamp. VRECT_L centerlines (8,6)-(40,42): vertical cord, broad tapered shade and exposed bulb. Merge the small collar into a flat shade crown.
Lucide lamp-ceiling / lamp-floor inform simple shades and explicit support joins.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7311de05-9c03-5e80-a814-12ddd4e64119'
SOURCE_PATH = 'pictographic-primitives/lamps/table lamp hanging_7311de05-9c03-5e80-a814-12ddd4e64119.svg'
AUTHOR = 'gpt-6'

class ConicalPendantLamp(Solo48):
    icon_id = 'conical-pendant-lamp'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'lamps'
    aliases = ()
    keywords = ('lamp', 'pendant', 'conical', 'shade', 'bulb', 'ceiling')

    def build(self) -> None:
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.
        self.add_line('cord', (24, 4), (24, 18))
        self.add_polyline('shade-top', (8, 34), (18, 18), (24, 18), (30, 18), (40, 34))
        self.add_polyline('rim', (40, 34), (34, 34), (14, 34), (8, 34))
        self.add_arc('bulb', (34, 34), (14, 34), radius_x=10, sweep=True)
        self.relate('connect', 'bulb', 'rim')
        self.relate('connect', 'shade-top', 'rim')
        self.relate('connect', 'shade-top', 'cord')
