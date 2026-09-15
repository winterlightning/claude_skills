"""A fuel dispenser has a short display and an external hose. VRECT_L extremes (8,6)-(40,42). Lucide fuel informs the rounded body and tangent hose turn. Preserve right-side hose asymmetry; shorten the display to keep generous clearance."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5e926d0b-c0ce-4cda-8027-a4553f9978ac'
SOURCE_PATH = 'pictographic-primitives/symbol/gas pump_5e926d0b-c0ce-4cda-8027-a4553f9978ac.svg'
AUTHOR = 'gpt-6'


class GasPump(Solo48):
    icon_id = 'gas-pump'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('gas', 'fuel', 'pump', 'petrol', 'station', 'car', 'diesel', 'refuel')

    def build(self) -> None:
        self.add_line('top',(12,6),(24,6))
        self.add_arc('top-right',(24,6),(28,8),radius_x=4)
        self.add_line('right-upper',(28,8),(28,36))
        self.add_line('right-lower',(28,36),(28,40))
        self.add_arc('bottom-right',(28,40),(24,42),radius_x=4)
        self.add_line('bottom',(24,42),(12,42))
        self.add_arc('bottom-left',(12,42),(8,40),radius_x=4)
        self.add_line('left',(8,40),(8,8))
        self.add_arc('top-left',(8,8),(12,6),radius_x=4)
        self.add_contour('pump','top','top-right','right-upper','right-lower','bottom-right','bottom','bottom-left','left','top-left',closed=True)
        self.add_line('display',(17,14),(19,14))
        self.add_line('hose-start',(28,36),(34,36))
        self.add_arc('hose-turn',(34,36),(40,30),radius_x=6,sweep=False)
        self.add_line('hose-rise',(40,30),(40,16))
        self.add_arc('nozzle',(40,16),(36,12),radius_x=4,sweep=False)
        self.add_contour('hose','hose-start','hose-turn','hose-rise','nozzle')
        self.relate('connect','pump','hose')
