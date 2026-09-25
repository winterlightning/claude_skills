"""square bubble user: standalone batch 17 repair.
Retained the speech bubble, lower-left tail and person. Changed to an upright keyshape and a shallow shoulder arch. Head center (24,16), radius 3; shoulder apex (24,27), exactly four units of visible detached clearance.
"""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID = '262dd529-82e6-4744-ac57-ec46c428f624'
SOURCE_PATH = 'pictographic-primitives/other/square bubble user_262dd529-82e6-4744-ac57-ec46c428f624.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'message-square'
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'

class Drawing(Solo48):
    icon_id = 'square-bubble-user'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ()
    keywords = ('square', 'bubble', 'user')

    def build(self):
        self.add_polyline('bubble',(8,4),(40,4),(40,38),(24,38),(16,44),(16,38),(8,38),closed=True)
        self.circle('head',24,16,3)
        self.add_arc('shoulders-left',(17,29),(24,27),radius_x=7,radius_y=2)
        self.add_arc('shoulders-right',(24,27),(31,29),radius_x=7,radius_y=2)
        self.add_contour('shoulders','shoulders-left','shoulders-right')

    def circle(self,name,x,y,r):
        self.add_arc(name+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

