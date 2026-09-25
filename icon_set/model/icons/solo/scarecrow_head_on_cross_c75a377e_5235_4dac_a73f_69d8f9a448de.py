"""Minimalist Farm Scarecrow.
Plan: Angular hat and circular head over an unclothed crossbar and stake. Extrema (8,4)-(40,44).
Reference: Supplied source; no useful exact Lucide match. Coherent curves and shared attachment points.
Reduction: No facial detail; bare crossbar distinguishes it from the shirted scarecrow.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c75a377e-5235-4dac-a73f-69d8f9a448de'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/farming/scarecrow_c75a377e-5235-4dac-a73f-69d8f9a448de.svg'
AUTHOR = 'gpt-6'

class Batch28Icon(Solo48):
    icon_id = 'scarecrow-head-on-cross'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "farming"
    categories = ("farming", "primitives")
    aliases = ()
    keywords = ('minimalist', 'farm', 'scarecrow')

    def build(self):

        x,y,r=24,15,3
        self.add_arc('head-a',(x,y-r),(x,y+r),radius_x=r)
        self.add_arc('head-b',(x,y+r),(x,y-r),radius_x=r)
        self.add_contour('head','head-a','head-b',closed=True)

        self.add_polyline('brim',(x-10,y-r),(x-6,y-r),(x,y-r),(x+6,y-r),(x+10,y-r))
        self.add_polyline('crown',(x-6,y-r),(x-4,y-r-8),(x+4,y-r-8),(x+6,y-r))
        self.relate('connect','head','brim');self.relate('connect','brim','crown')

        self.add_polyline('crossbar',(8,26),(24,26),(40,26))
        self.add_line('pole',(24,26),(24,44));self.relate('connect','crossbar','pole')
