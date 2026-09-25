"""Farming Field Scarecrow.
Plan: Mirrored shirt on crossbar and central stake beneath hatted head. Extrema (8,4)-(40,44).
Reference: Supplied source; no useful exact Lucide match. Coherent curves and shared attachment points.
Reduction: Sleeve corners and central hanging shirt retained above a visible six-unit support stake.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fa071659-1920-5f9e-8952-73d8159b6335'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/farming/farming scarecrow_fa071659-1920-5f9e-8952-73d8159b6335.svg'
AUTHOR = 'gpt-6'

class Batch28Icon(Solo48):
    icon_id = 'scarecrow-shirt-crossbar'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "farming"
    aliases = ()
    keywords = ('farming', 'field', 'scarecrow')

    def build(self):

        x,y,r=24,15,3
        self.add_arc('head-a',(x,y-r),(x,y+r),radius_x=r)
        self.add_arc('head-b',(x,y+r),(x,y-r),radius_x=r)
        self.add_contour('head','head-a','head-b',closed=True)

        self.add_polyline('brim',(x-10,y-r),(x-6,y-r),(x,y-r),(x+6,y-r),(x+10,y-r))
        self.add_polyline('crown',(x-6,y-r),(x-4,y-r-8),(x+4,y-r-8),(x+6,y-r))
        self.relate('connect','head','brim');self.relate('connect','brim','crown')

        self.add_polyline('shirt',(8,26),(16,26),(24,26),(32,26),(40,26),(40,34),(32,34),(32,38),(24,38),(16,38),(16,34),(8,34),(8,26))
        self.add_line('pole',(24,38),(24,44));self.relate('connect','shirt','pole')
