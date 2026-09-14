"""Incognito Hat and Glasses. Authored from the supplied visual brief."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '290cc284-c41b-4672-b20d-4ddd4d36a403'
SOURCE_PATH = 'pictographic-primitives/websites/incognito_290cc284-c41b-4672-b20d-4ddd4d36a403.svg'
AUTHOR = 'gpt-6'

class IncognitoHatAndGlasses(Solo48):
    icon_id = 'incognito-hat-and-glasses'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/technology"
    aliases = ()
    keywords = ('incognito', 'hat', 'glasses', 'disguise', 'private', 'spectacles', 'anonymous')

    def build(self):
        axis=24
        self.add_polyline('crown',(9,17),(13,8),(2*axis-13,8),(2*axis-9,17))
        self.add_polyline('brim',(6,17),(9,17),(39,17),(42,17))
        self.relate('connect','crown','brim')
        for side,cx in [('left',13),('right',2*axis-13)]:
            self.ring(side,cx,33,7)
        self.add_line('bridge',(20,33),(28,33))
        self.relate('connect','bridge','left')
        self.relate('connect','bridge','right')

    def ring(self,name,cx,cy,r):
        points=[(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
        for i,p in enumerate(points):
            self.add_arc(f'{name}-{i}',p,points[(i+1)%4],radius_x=r)
        self.add_contour(name,*(f'{name}-{i}' for i in range(4)),closed=True)
