"""Single Burning Fire Flame."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd11d120b-44dc-4986-8c2a-a773c8830e0c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/fire/flame_d11d120b-44dc-4986-8c2a-a773c8830e0c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'flame-with-inner-drop'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'fire'
    aliases = ()
    keywords = ('fire', 'flame', 'drop', 'burning', 'heat', 'blaze', 'symbol')

    def build(self):
        # Plan: Outer flame and returning inner teardrop make one open-base silhouette. Lucide rounded bowl. Pointed upper tip and right spur retain asymmetry. Bounds (8,4)-(40,44).
        self.add_bezier('outline',(18,44),((11,40),(8,35),(8,29)),((8,19),(26,16),(21,4)),((31,9),(32,17),(30,23)),((35,23),(39,20),(40,16)),((40,21),(40,25),(40,29)),((40,36),(35,41),(30,44)))
        self.add_bezier('inner',(18,44),((13,35),(18,29),(24,25)),((24,32),(35,33),(30,44)))
        self.relate('connect','outline','inner')
