"""rectangle single man focus: standalone batch 17 repair.
Retained the portrait and full rectangular panel. Merged the four focus indicators into diagonal corner ticks on the panel to avoid a second nested frame. Human head center (24,16), radius 3; shoulder apex (24,27), exact four-unit visible detached gap.
"""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID = '748d6e5f-8942-4061-a602-5b499075202e'
SOURCE_PATH = 'pictographic-primitives/other/rectangle single man focus_748d6e5f-8942-4061-a602-5b499075202e.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'scan-face'
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'

class Drawing(Solo48):
    icon_id='rectangle-single-man-focus'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases=()
    keywords=('rectangle', 'single', 'man', 'focus')

    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)





    def build(self):
        self.add_polyline('panel',(8,4),(40,4),(40,44),(8,44),closed=True)
        self.circle('head',24,16,3)
        self.add_arc('shoulders-left',(19,31),(24,27),radius_x=5,radius_y=4)
        self.add_arc('shoulders-right',(24,27),(29,31),radius_x=5,radius_y=4)
        self.add_contour('shoulders','shoulders-left','shoulders-right')
        for n,a,b in [('tl',(8,4),(14,10)),('tr',(40,4),(34,10)),('bl',(8,44),(14,38)),('br',(40,44),(34,38))]:
            self.add_line('focus-'+n,a,b)
            self.relate('connect','panel','focus-'+n)

