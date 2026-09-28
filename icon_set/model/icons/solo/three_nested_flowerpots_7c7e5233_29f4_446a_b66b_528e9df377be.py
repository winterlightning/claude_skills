"""Stacked Flower Pots.
Plan: Three equal broad rim tiers above tapered nesting walls and flat base. Extrema (8,4)-(40,44).
Reference: Supplied original; no useful exact local Lucide match. Sparse outline and shared attachment principles.
Reduction: Each thick rim reduced to one stroke, keeping three distinct horizontal tiers.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7c7e5233-29f4-446a-b66b-528e9df377be'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/farming/pots_7c7e5233-29f4-446a-b66b-528e9df377be.svg'
AUTHOR = 'gpt-6'

class Batch29Icon(Solo48):
    icon_id = 'three-nested-flowerpots'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "farming"
    categories = ("farming", "primitives")
    aliases = ()
    keywords = ('stacked', 'flower', 'pots')

    def build(self):

        for i,y in enumerate((4,16,28)):
            self.add_polyline(f'rim-{i}',(8,y),(12+2*i,y),(36-2*i,y),(40,y))
        for i,y in enumerate((4,16)):
            for side,x in (('left',12+2*i),('right',36-2*i)):
                endx=x+2 if side=='left' else x-2
                self.add_line(f'wall-{i}-{side}',(x,y),(endx,y+12))
                self.relate('connect',f'wall-{i}-{side}',f'rim-{i}')
                self.relate('connect',f'wall-{i}-{side}',f'rim-{i+1}')
        self.add_polyline('base',(16,28),(18,44),(30,44),(32,28));self.relate('connect','base','rim-2')
