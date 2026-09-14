"""Lucide user-round informs head and shoulders; broad podium and one sash stroke retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '49936d88-84dd-409f-9fb1-0754fd6ca144'
SOURCE_PATH = 'pictographic-primitives/school-learning/election politician podium neutral_49936d88-84dd-409f-9fb1-0754fd6ca144.svg'
AUTHOR = 'gpt-6'


class PoliticianAtPodium(Solo48):
    icon_id = 'politician-at-podium'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "society/elections"
    aliases = ()
    keywords = ('politician', 'podium', 'speech', 'sash', 'person', 'election')

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

        self.circle('head',24,10,4)
        self.add_arc('shoulder-left',(12,32),(20,24),radius_x=8)
        self.add_line('shoulder-top',(20,24),(28,24))
        self.add_arc('shoulder-right',(28,24),(36,32),radius_x=8)
        self.add_contour('shoulders','shoulder-left','shoulder-top','shoulder-right')
        self.add_polyline('ledge',(6,32),(12,32),(36,32),(42,32))
        self.add_line('sash',(28,24),(20,32))
        self.relate('connect','sash','shoulders')
        self.relate('connect','sash','ledge')
        self.relate('connect','shoulders','ledge')
        for side,x,d in (('left',12,1),('right',36,-1)):
            self.add_line('leg-'+side,(x,32),(x+d*2,42))
            self.relate('connect','leg-'+side,'ledge')
            self.relate('connect','leg-'+side,'shoulders')
