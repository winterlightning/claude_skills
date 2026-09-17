"""Needle Sewing Fabric.

Plan: Needle crosses fabric diagonally; thread makes a broad loop beyond the eye. Eye reduced to a round tip and fabric corners simplified. Bounds (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8180ae35-1c75-59d8-ad57-ff9729f28bc5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/sewing sewing scarf_8180ae35-1c75-59d8-ad57-ff9729f28bc5.svg'
AUTHOR = 'gpt-6'

class NeedleSewingFabric(Solo48):
    icon_id = 'needle-sewing-fabric'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/hobbies"
    aliases = ()
    keywords = ('needle', 'sewing', 'fabric')

    def build(self):
        self.add_polyline('fabric',(6,18),(24,18),(30,18),(30,42),(6,42),closed=True)
        self.add_line('needle',(6,42),(36,6))
        self.add_arc('thread',(36,6),(42,12),radius_x=6)
        self.relate('connect','fabric','needle');self.relate('connect','needle','thread')
