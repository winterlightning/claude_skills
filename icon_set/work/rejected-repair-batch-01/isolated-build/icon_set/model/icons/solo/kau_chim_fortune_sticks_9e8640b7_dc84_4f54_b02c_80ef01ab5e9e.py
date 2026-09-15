"""Three fortune sticks in a cylindrical cup. Keep splayed sticks and rounded vessel; omit stick thickness and rear elliptical rim."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9e8640b7-dc84-4f54-b02c-80ef01ab5e9e'
SOURCE_PATH = 'pictographic-primitives/religion/chinese kau chim_9e8640b7-dc84-4f54-b02c-80ef01ab5e9e.svg'
AUTHOR = 'gpt-6'


class KauChimFortuneSticks(Solo48):
    icon_id = 'kau-chim-fortune-sticks'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "culture/religion"
    aliases = ()
    keywords = ('kau chim', 'fortune', 'stick', 'divination', 'holder', 'chinese')

    def oval(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-top', (cx-rx,cy), (cx+rx,cy), radius_x=rx, radius_y=ry)
        self.add_arc(name+'-bottom', (cx+rx,cy), (cx-rx,cy), radius_x=rx, radius_y=ry)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def build(self) -> None:
        # Live VRECT centerline box (8,4)-(40,44).
        self.add_polyline('rim',(8,24),(16,24),(24,24),(32,24),(40,24))
        self.add_line('side-right',(40,24),(40,38))
        self.add_arc('bottom-right',(40,38),(34,44),radius_x=6)
        self.add_line('bottom',(34,44),(14,44))
        self.add_arc('bottom-left',(14,44),(8,38),radius_x=6)
        self.add_line('side-left',(8,38),(8,24))
        self.add_contour('cup','side-right','bottom-right','bottom','bottom-left','side-left')
        self.relate('connect','rim','cup')
        for name,start,end in [('left',(10,4),(16,24)),('middle',(24,7),(24,24)),('right',(38,4),(32,24))]:
            self.add_line('stick-'+name,start,end)
            self.relate('connect','stick-'+name,'rim')
