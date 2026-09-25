"""Replace the uncertain left body curvature with an exact quarter-circle and a tangent vertical join; keep the bill and dorsal fin distinct. Applied to the original icon identity."""
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
    category = 'animals'
    aliases = ()
    keywords = ('marlin', 'swordfish', 'jump', 'bill', 'sea', 'fishing', 'sport', 'ocean')

    def build(self) -> None:
        """Symbol plan: Replace the uncertain left body curvature with an exact quarter-circle and a tangent vertical join; keep the bill and dorsal fin distinct. Reference: Lucide fish: coherent body curves with deliberate angular fins."""
        self.add_arc('body-1', (6, 26), (20, 12), radius_x=14, radius_y=14, sweep=True)
        self.add_line('body-2', (20, 12), (32, 7))
        self.add_bezier('body-3', (32, 7), ((32, 18), (18, 23), (18, 30)))
        self.add_line('body-4', (18, 30), (30, 30))
        self.add_line('body-5', (30, 30), (30, 42))
        self.add_line('body-6', (30, 42), (18, 38))
        self.add_bezier('body-8', (18, 38), ((12, 36), (6, 34), (6, 30)))
        self.add_line('body-9', (6, 30), (6, 26))
        self.add_contour('body', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-8', 'body-9', closed=True)
        self.add_line('bill-1', (32, 7), (42, 6))
        self.add_contour('bill', 'bill-1', closed=False)
        self.add_line('dorsal-1', (6, 26), (6, 6))
        self.add_line('dorsal-2', (6, 6), (20, 12))
        self.add_contour('dorsal', 'dorsal-1', 'dorsal-2', closed=False)
        self.relate('connect', 'body', 'dorsal')
        self.relate('connect', 'body', 'bill')
