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
    category = "symbol"
    categories = ("symbol",)
    aliases = ()
    keywords = ('gas', 'fuel', 'pump', 'petrol', 'station', 'car', 'diesel', 'refuel')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_line('top',(12, 4),(24, 4))
        self.add_bezier('top-right',(24, 4),*(((25.6162858, 4), (27.19868669, 4.72578466), (28, 6)),))
        self.add_line('right-upper',(28, 6),(28, 36))
        self.add_line('right-lower',(28, 36),(28, 42))
        self.add_bezier('bottom-right',(28, 42),*(((27.19868669, 43.27421534), (25.6162858, 44), (24, 44)),))
        self.add_line('bottom',(24, 44),(12, 44))
        self.add_bezier('bottom-left',(12, 44),*(((10.3837142, 44), (8.80131331, 43.27421534), (8, 42)),))
        self.add_line('left',(8, 42),(8, 6))
        self.add_bezier('top-left',(8, 6),*(((8.80131331, 4.72578466), (10.3837142, 4), (12, 4)),))
        self.add_line('display',(17, 14),(19, 14))
        self.add_line('hose-start',(28, 36),(34, 36))
        self.add_bezier('hose-turn',(34, 36),*(((37.3137085, 36.5), (40, 33.3137085), (40, 30)),))
        self.add_line('hose-rise',(40, 30),(40, 16))
        self.add_bezier('nozzle',(40, 16),*(((40, 13.73857625), (38.209139, 11.5), (36, 12)),))
        self.add_contour('pump',*('top', 'top-right', 'right-upper', 'right-lower', 'bottom-right', 'bottom', 'bottom-left', 'left', 'top-left'),closed=True)
        self.add_contour('hose',*('hose-start', 'hose-turn', 'hose-rise', 'nozzle'),closed=False)
        self.relate('connect',*('pump', 'hose'))
