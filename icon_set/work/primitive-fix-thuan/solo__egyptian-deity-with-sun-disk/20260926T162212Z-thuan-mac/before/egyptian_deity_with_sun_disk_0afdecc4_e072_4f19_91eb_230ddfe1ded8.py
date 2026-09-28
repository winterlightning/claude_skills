"""A falcon-headed Egyptian deity wearing a sun disk. Keep sun, projecting beak and curved throat; omit the tiny serpent and facial details."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0afdecc4-e072-4f19-91eb-230ddfe1ded8'
SOURCE_PATH = 'pictographic-primitives/religion/epgyptian mythology_0afdecc4-e072-4f19-91eb-230ddfe1ded8.svg'
AUTHOR = 'gpt-6'


class EgyptianDeityWithSunDisk(Solo48):
    icon_id = 'egyptian-deity-with-sun-disk'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "religion"
    categories = ("primitives", "religion")
    aliases = ()
    keywords = ('egyptian', 'deity', 'sun', 'disk', 'head', 'mythology', 'serpent')

    def oval(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-top', (cx-rx,cy), (cx+rx,cy), radius_x=rx, radius_y=ry)
        self.add_arc(name+'-bottom', (cx+rx,cy), (cx-rx,cy), radius_x=rx, radius_y=ry)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def build(self) -> None:
        # Live VRECT centerline box (8,4)-(40,44).
        self.oval('sun',23,13,9)
        self.add_polyline('back',(8,44),(14,33),(23,31),(29,31))
        self.add_arc('beak-forehead',(29,31),(40,38),radius_x=13)
        self.add_polyline('beak',(40,38),(31,38),(34,44))
        self.add_arc('throat',(23,31),(23,44),radius_x=14,sweep=False)
        self.relate('connect','back','throat')
        self.relate('connect','back','beak-forehead');self.relate('connect','beak-forehead','beak')
