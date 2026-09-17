"""Farmer with Pitchfork.
Plan: Farmer stands beside three-tined fork; head (16,15), r3; neck (16,26). Extrema (8,4)-(40,44).
Reference: human_ref/full_body_ref.png: circular detached heads, coherent torso and simple limbs; Lucide person-standing supports shared joints.
Reduction: Bib pocket and overalls outline omitted; hat, figure and three fork tines retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '82d178e5-3f74-432a-987e-abc1c9057ae8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/farming/farmer_82d178e5-3f74-432a-987e-abc1c9057ae8.svg'
AUTHOR = 'gpt-6'

class Batch28Icon(Solo48):
    icon_id = 'farmer-standing-beside-pitchfork'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/agriculture"
    aliases = ()
    keywords = ('farmer', 'with', 'pitchfork')

    def build(self):

        x,y,r=16,15,3
        self.add_arc('head-a',(x,y-r),(x,y+r),radius_x=r)
        self.add_arc('head-b',(x,y+r),(x,y-r),radius_x=r)
        self.add_contour('head','head-a','head-b',closed=True)

        self.add_polyline('brim',(x-8,y-r),(x-6,y-r),(x,y-r),(x+6,y-r),(x+8,y-r))
        self.add_polyline('crown',(x-6,y-r),(x-4,y-r-8),(x+4,y-r-8),(x+6,y-r))
        self.relate('connect','head','brim');self.relate('connect','brim','crown')

        self.add_line('torso',(16,26),(16,34))
        self.add_polyline('legs',(8,44),(16,34),(20,44));self.relate('connect','torso','legs')
        self.add_polyline('arm',(16,26),(8,28),(8,34));self.relate('connect','arm','torso')
        self.add_polyline('fork',(24,24),(24,30),(32,30),(40,30),(40,24))
        self.add_polyline('shaft',(32,24),(32,30),(32,44));self.relate('connect','fork','shaft')
        self.mark_human_figure('farmer',head='head',torso='torso',torso_junction='start')
