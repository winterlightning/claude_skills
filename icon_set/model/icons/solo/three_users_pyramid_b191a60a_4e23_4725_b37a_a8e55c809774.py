"""Three matching round heads and arched shoulder lines form a triangle. Lucide users-round informs each repeated user; small neck stems are omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b191a60a-4e23-4725-b37a-a8e55c809774'
SOURCE_PATH = 'pictographic-primitives/users/multiple users_b191a60a-4e23-4725-b37a-a8e55c809774.svg'
AUTHOR = 'gpt-6'


class ThreeUsersPyramid(Solo48):
    icon_id = 'three-users-pyramid'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "users"
    categories = ("users", "primitives")
    aliases = ()
    keywords = ('users', 'group', 'three', 'team', 'people', 'network', 'hierarchy', 'community')

    def circle(self, name, cx, cy, radius):
        top, bottom = (cx, cy-radius), (cx, cy+radius)
        self.add_arc(name+'-a',top,bottom,radius_x=radius)
        self.add_arc(name+'-b',bottom,top,radius_x=radius)
        self.add_contour(name,name+'-a',name+'-b',closed=True)


    def build(self) -> None:
        # Square centerline extremes (6,6)-(42,42); repeated compact user glyphs.
        for name,cx,head_y,shoulder_y in [('top',24,9,23),('left',9,28,42),('right',39,28,42)]:
            self.circle('head-'+name,cx,head_y,3)
            self.add_arc('shoulders-'+name,(cx-3,shoulder_y),(cx+3,shoulder_y),radius_x=3,radius_y=2)
