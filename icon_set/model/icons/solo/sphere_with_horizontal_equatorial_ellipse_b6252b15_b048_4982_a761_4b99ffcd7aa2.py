"""Three Dimensional Sphere.

Symbol plan: One spherical circle and equatorial ellipse sharing cardinal endpoints. Lucide globe supplies clean half-arc construction; equator stays horizontal as in source.
Keyshape: CIRCLE; exact visible bounds (2, 2, 46, 46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b6252b15-b048-4982-a761-4b99ffcd7aa2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/sphere shape_b6252b15-b048-4982-a761-4b99ffcd7aa2.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'sphere-with-horizontal-equatorial-ellipse'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "design"
    categories = ("design", "primitives")
    aliases = ()
    keywords = ('three', 'dimensional', 'sphere')

    def build(self):
        x,y,r=24,24,20
        for name,ry in [('outline',r),('equator',7)]:
            self.add_arc(name+'-top',(x-r,y),(x+r,y),radius_x=r,radius_y=ry)
            self.add_arc(name+'-bottom',(x+r,y),(x-r,y),radius_x=r,radius_y=ry)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)
        self.relate('connect','outline','equator')
