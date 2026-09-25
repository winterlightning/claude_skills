"""Electric Induction Cooktop."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c85e08f1-89e8-42cc-8a1b-46e164dae146'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/stove induction_c85e08f1-89e8-42cc-8a1b-46e164dae146.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'single-ring-induction-cooktop'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('induction', 'cooktop', 'burner', 'stove', 'appliance', 'kitchen', 'cooking')

    def build(self):
        # Plan: Perspective induction cooktop with elliptical burner and thick front lip. No exact Lucide match. Square envelope makes room for burner clearance; small control panel omitted. Bounds (6,6)-(42,42).
        self.add_polyline('top',(6,32),(12,6),(36,6),(42,32),(6,32))
        self.add_polyline('front',(6,32),(6,42),(42,42),(42,32));self.relate('connect','front','top')
        self.add_arc('ring-top',(18,19),(30,19),radius_x=6,radius_y=4)
        self.add_arc('ring-bottom',(30,19),(18,19),radius_x=6,radius_y=4)
        self.add_contour('burner','ring-top','ring-bottom',closed=True)
