"""Gas Stove Burner with Flame."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3d9de121-d2f1-5234-9ff9-988fc6cea6e2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/stove gas_3d9de121-d2f1-5234-9ff9-988fc6cea6e2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'single-flame-gas-burner'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('gas', 'burner', 'flame', 'stove', 'heat', 'cooking', 'kitchen')

    def build(self):
        # Plan: Curling flame above broad gas burner. Lucide flame coherent outer silhouette. Narrow inner cleft and tiny supports omitted for clearance. Envelope (8,4)-(40,44).
        self.add_bezier('flame',(24,4),((24,12),(14,14),(14,20)),((14,25),(18,27),(24,27)),((30,27),(34,24),(34,20)),((34,14),(28,7),(24,4)))
        self.add_contour('fire','flame',closed=True)
        self.add_polyline('base',(8,36),(40,36),(40,44),(8,44),closed=True)
