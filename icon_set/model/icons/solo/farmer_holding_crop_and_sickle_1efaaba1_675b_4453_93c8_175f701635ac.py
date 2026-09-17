"""Farmer Harvesting Crops.
Plan: Farmer holds fanned stalks left and curved sickle right. Head (24,17), r3; neck (24,28). Extrema (6,6)-(42,42).
Reference: human_ref/full_body_ref.png: circular detached heads, coherent torso and simple limbs; Lucide person-standing supports shared joints.
Reduction: Crop fan reduced to two stalks; sickle blade single-stroke; garment outline omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1efaaba1-675b-4453-93c8-175f701635ac'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/farming/farmer crops_1efaaba1-675b-4453-93c8-175f701635ac.svg'
AUTHOR = 'gpt-6'

class Batch28Icon(Solo48):
    icon_id = 'farmer-holding-crop-and-sickle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/agriculture"
    aliases = ()
    keywords = ('farmer', 'harvesting', 'crops')

    def build(self):

        x,y,r=24,17,3
        self.add_arc('head-a',(x,y-r),(x,y+r),radius_x=r)
        self.add_arc('head-b',(x,y+r),(x,y-r),radius_x=r)
        self.add_contour('head','head-a','head-b',closed=True)

        self.add_polyline('brim',(x-6,y-r),(x-4,y-r),(x,y-r),(x+4,y-r),(x+6,y-r))
        self.add_polyline('crown',(x-4,y-r),(x-4,y-r-8),(x+4,y-r-8),(x+4,y-r))
        self.relate('connect','head','brim');self.relate('connect','brim','crown')

        self.add_line('torso',(24,28),(24,34))
        self.add_polyline('legs',(16,42),(24,34),(32,42));self.relate('connect','torso','legs')
        self.add_polyline('arms',(10,30),(24,28),(38,28),(38,20))
        self.relate('connect','torso','arms')
        self.add_polyline('crop',(6,20),(10,30),(12,20));self.relate('connect','crop','arms')
        self.add_arc('sickle',(38,12),(38,20),radius_x=4);self.relate('connect','sickle','arms')
        self.mark_human_figure('farmer',head='head',torso='torso',torso_junction='start')
