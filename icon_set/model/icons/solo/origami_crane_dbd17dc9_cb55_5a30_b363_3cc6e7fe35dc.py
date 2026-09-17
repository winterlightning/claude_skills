"""Origami Crane.

Plan: Angular folded crane with a raised wing, left neck and beak, broad body and pointed tail. Lucide origami informs deliberate fold corners. Bounds (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dbd17dc9-cb55-5a30-b363-3cc6e7fe35dc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/crafts origami_dbd17dc9-cb55-5a30-b363-3cc6e7fe35dc.svg'
AUTHOR = 'gpt-6'

class OrigamiCrane(Solo48):
    icon_id = 'origami-crane'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/hobbies"
    aliases = ()
    keywords = ('origami', 'crane')

    def build(self):
        self.add_polyline('bird',(6,20),(14,12),(24,12),(24,24),(34,6),(34,30),(42,42),(18,34),(10,20),closed=True)
