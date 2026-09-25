"""Lucide bus: shared axle and circular wheels; attached flag retains campaign identity. Window dividers omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '637f75de-1cc0-403f-8da8-3087fab11c86'
SOURCE_PATH = 'pictographic-primitives/school-learning/election campaign 1_637f75de-1cc0-403f-8da8-3087fab11c86.svg'
AUTHOR = 'gpt-6'


class CampaignBus(Solo48):
    icon_id = 'campaign-bus'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "school-learning"
    aliases = ()
    keywords = ('bus', 'campaign', 'flag', 'election', 'vehicle', 'transport')

    def circle(self, name, x, y, r):
        pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
        ids=[]
        for j,(a,b) in enumerate(zip(pts,pts[1:])):
            eid=name+'-'+str(j)
            self.add_arc(eid,a,b,radius_x=r);ids.append(eid)
        self.add_contour(name,*ids,closed=True)

    def bust(self, name, x, y, r=2, width=5):
        self.circle(name+'-head',x,y,r)
        self.add_arc(name+'-sl',(x-width,y+7),(x,y+r),radius_x=width,radius_y=7-r)
        self.add_arc(name+'-sr',(x,y+r),(x+width,y+7),radius_x=width,radius_y=7-r)
        self.add_contour(name+'-shoulders',name+'-sl',name+'-sr')
        self.relate('connect',name+'-head',name+'-shoulders')

    def build(self) -> None:
        # Bounds are derived from the live SOLO48 contract, not the stale skill table.

        self.add_polyline('flag',(18,22),(18,6),(38,6),(34,10),(38,14),(18,14))
        self.add_polyline('body',(12,38),(6,38),(6,26),(10,22),(18,22),(38,22),(42,26),(42,38),(36,38))
        self.relate('connect','flag','body')
        self.add_line('window-rule',(6,30),(42,30))
        self.relate('connect','body','window-rule')
        self.circle('wheel-left',16,38,4)
        self.circle('wheel-right',32,38,4)
        self.add_line('axle',(20,38),(28,38))
        for w in ('wheel-left','wheel-right'):
            self.relate('connect','body',w)
            self.relate('connect','axle',w)
