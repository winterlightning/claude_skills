"""Two mirrored cupped hands support a round sphere. Preserve the ball, upright fingers and inward thumbs; omit finger subdivisions."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '66991385-e96d-49e5-a043-770baf2d1ecf'
SOURCE_PATH = 'pictographic-primitives/religion/sphere hand_66991385-e96d-49e5-a043-770baf2d1ecf.svg'
AUTHOR = 'gpt-6'

class HandsCuppingSphere(Solo48):
    icon_id = 'hands-cupping-sphere'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "religion"
    categories = ("primitives", "religion")
    aliases = ()
    keywords = ('hand', 'sphere', 'holding', 'cupped', 'palm', 'orb')

    def oval(self,name,cx,cy,rx,ry=None):
        ry=rx if ry is None else ry
        self.add_arc(name+'-top',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def build(self) -> None:
        # Centerline box (8,4)-(40,44), mirrored about x=24.
        self.oval('sphere',24,13,9)
        for side in (-1,1):
         def point(x,y):return (24+side*x,y)
         name='hand-'+str(side)
         self.add_polyline(name,point(16,24),point(16,28),point(16,33),point(12,44))
         self.add_polyline(name+'-thumb',point(16,28),point(4,36),point(4,44))
         self.relate('connect',name,name+'-thumb')
