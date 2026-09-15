"""Minimal Fuel Pump, re-authored from its reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7f85add7-29a9-41d6-b767-bcc1a2396a1b'
SOURCE_PATH = 'pictographic-primitives/transportation/low fuel_7f85add7-29a9-41d6-b767-bcc1a2396a1b.svg'
AUTHOR = 'gpt-6'

class MinimalFuelPump(Solo48):
    icon_id = 'minimal-fuel-pump'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/transportation"
    aliases = ()
    keywords = ('fuel pump', 'low fuel', 'petrol', 'gas station', 'refuel', 'fuel', 'dashboard', 'car')

    def build(self) -> None:
        # Current contract centerline extremes: (6,6)-(42,42).
        self.add_line('top',(10,6),(22,6))
        self.add_arc('tr',(22,6),(26,10),radius_x=4)
        self.add_line('right-upper',(26,10),(26,24))
        self.add_line('right-lower',(26,24),(26,38))
        self.add_arc('br',(26,38),(22,42),radius_x=4)
        self.add_line('bottom',(22,42),(10,42))
        self.add_arc('bl',(10,42),(6,38),radius_x=4)
        self.add_line('left-lower',(6,38),(6,24))
        self.add_line('left-upper',(6,24),(6,10))
        self.add_arc('tl',(6,10),(10,6),radius_x=4)
        self.add_contour('pump','top','tr','right-upper','right-lower','br','bottom','bl','left-lower','left-upper','tl',closed=True)
        self.add_line('divider',(6,24),(26,24))
        self.relate('connect','divider','pump')
        self.add_line('display',(15,15),(17,15))
        self.add_arc('nozzle',(34,6),(42,14),radius_x=8)
        self.add_line('hose-long',(42,14),(42,36))
        self.add_arc('hose-loop',(42,36),(34,36),radius_x=4)
        self.add_line('hose-short',(34,36),(34,24))
        self.add_line('hose-join',(34,24),(26,24))
        self.add_contour('hose','nozzle','hose-long','hose-loop','hose-short','hose-join')
        self.relate('connect','hose','pump')
