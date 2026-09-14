'A leaping marlin with a rounder left flank and curved dorsal edge. SQUARE extremes (6,6)-(42,42) preserve the bill and tall fin. No useful local Lucide marlin match; coherent elliptical arcs replace the pointed flank junction. Directional pose is intentional.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '62cae7c5-b221-5640-af8e-3e439786f697'
SOURCE_PATH = 'pictographic-primitives/animals/shark swordfish_62cae7c5-b221-5640-af8e-3e439786f697.svg'
AUTHOR = 'gpt-6'

class LeapingMarlin(Solo48):
    icon_id = 'leaping-marlin'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals/marine'
    aliases = ()
    keywords = ('marlin', 'swordfish', 'jump', 'bill', 'sea', 'fishing', 'sport', 'ocean')

    def build(self) -> None:
        self.add_arc('body-1', (8, 22), (20, 12), radius_x=32, radius_y=26, sweep=True)
        self.add_line('body-2', (20, 12), (32, 7))
        self.add_arc('body-3', (32, 7), (19, 29), radius_x=23, radius_y=23, sweep=True)
        self.add_arc('body-4', (19, 29), (22, 38), radius_x=10, radius_y=10, sweep=False)
        self.add_line('body-5', (22, 38), (30, 30))
        self.add_arc('body-6', (30, 30), (30, 42), radius_x=28, radius_y=28, sweep=False)
        self.add_line('body-7', (30, 42), (22, 40))
        self.add_arc('body-8', (22, 40), (6, 30), radius_x=20, radius_y=10, sweep=True)
        self.add_arc('body-9', (6, 30), (8, 22), radius_x=6, radius_y=8, sweep=True)
        self.add_contour('body', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', 'body-8', 'body-9', closed=True)
        self.add_line('bill-1', (32, 7), (42, 6))
        self.add_contour('bill', 'bill-1', closed=False)
        self.add_arc('dorsal-1', (8, 22), (7, 6), radius_x=24, radius_y=24, sweep=False)
        self.add_arc('dorsal-2', (7, 6), (20, 12), radius_x=30, radius_y=30, sweep=True)
        self.add_contour('dorsal', 'dorsal-1', 'dorsal-2', closed=False)
        self.relate('connect', 'body', 'dorsal')
        self.relate('connect', 'body', 'bill')
