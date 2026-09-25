"""Fire Flame Symbol."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '48a5f358-deb5-4917-8e95-796a7b826567'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/fire/shield with flame_48a5f358-deb5-4917-8e95-796a7b826567.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'single-flame-inner-tongue'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'fire'
    aliases = ()
    keywords = ('fire', 'flame', 'burning', 'heat', 'tongue', 'blaze', 'symbol')

    def build(self):
        # Plan: Tall outer teardrop encloses an open upward tongue. Lucide flame supplies a rounded lower bowl. Bounds (8,4)-(40,44); asymmetric apex.
        self.add_bezier('outer',(25,4),((28,17),(8,19),(8,30)),((8,39),(15,44),(24,44)),((33,44),(40,39),(40,30)),((40,18),(31,7),(25,4)))
        self.add_contour('outline','outer',closed=True)
        self.add_bezier('tongue',(22,34),((18,30),(22,26),(25,23)),((24,28),(30,30),(27,34)))
