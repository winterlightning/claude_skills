"""Lucide user-round: repeated heads and shoulder arcs. Three people and notched banner retained; folded second layer omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9c276e80-fe1b-4163-a5a7-8cb3946d5876'
SOURCE_PATH = 'pictographic-primitives/school-learning/election campaign 2_9c276e80-fe1b-4163-a5a7-8cb3946d5876.svg'
AUTHOR = 'gpt-6'


class CampaignRally(Solo48):
    icon_id = 'campaign-rally'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "society/elections"
    aliases = ()
    keywords = ('rally', 'campaign', 'people', 'banner', 'election', 'crowd')

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

        self.add_polyline('banner',(6,20),(6,6),(42,6),(37,12),(42,18),(6,18))
        for i,x in enumerate((12,24,36)):
            self.bust('person-'+str(i),x,35,r=2,width=6)
        self.relate('connect','person-0-shoulders','person-1-shoulders')
        self.relate('connect','person-1-shoulders','person-2-shoulders')

