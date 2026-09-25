"""Farmer Raking the Soil.
Plan: Farmer bends at hip and grips a diagonal hoe pointing down-left. Head (32,17), r3; neck (32,28). Extrema (6,6)-(42,42).
Reference: human_ref/full_body_ref.png: circular detached heads, coherent torso and simple limbs; Lucide person-standing supports shared joints.
Reduction: Soil patch and extra hand removed; bent hip, hat and diagonal hoe preserved.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cf3ffa48-69ee-55a9-b0f2-b59ed9778e0e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/farming/harvest farmer_cf3ffa48-69ee-55a9-b0f2-b59ed9778e0e.svg'
AUTHOR = 'gpt-6'

class Batch28Icon(Solo48):
    icon_id = 'farmer-working-long-handled-hoe'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "farming"
    aliases = ()
    keywords = ('farmer', 'raking', 'the', 'soil')

    def build(self):

        x,y,r=32,17,3
        self.add_arc('head-a',(x,y-r),(x,y+r),radius_x=r)
        self.add_arc('head-b',(x,y+r),(x,y-r),radius_x=r)
        self.add_contour('head','head-a','head-b',closed=True)

        self.add_polyline('brim',(x-10,y-r),(x-6,y-r),(x,y-r),(x+6,y-r),(x+10,y-r))
        self.add_polyline('crown',(x-6,y-r),(x-4,y-r-8),(x+4,y-r-8),(x+6,y-r))
        self.relate('connect','head','brim');self.relate('connect','brim','crown')

        self.add_polyline('torso',(32,28),(32,31),(36,34))
        self.add_polyline('legs',(28,42),(36,34),(42,42));self.relate('connect','torso','legs')
        self.add_line('arm',(32,28),(20,30));self.relate('connect','arm','torso')
        self.add_polyline('shaft',(10,42),(20,30),(24,25));self.relate('connect','shaft','arm')
        self.add_polyline('blade',(6,42),(10,42),(14,42));self.relate('connect','shaft','blade')
        self.mark_human_figure('farmer',head='head',torso='torso-1',torso_junction='start')
