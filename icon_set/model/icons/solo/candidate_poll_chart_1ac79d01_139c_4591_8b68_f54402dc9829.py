"""Lucide user-round: equal candidate busts. Three unequal bars are single strokes to preserve spacing."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1ac79d01-139c-4591-8b68-f54402dc9829'
SOURCE_PATH = 'pictographic-primitives/school-learning/election candidate poll_1ac79d01-139c-4591-8b68-f54402dc9829.svg'
AUTHOR = 'gpt-6'


class CandidatePollChart(Solo48):
    icon_id = 'candidate-poll-chart'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "society/elections"
    aliases = ()
    keywords = ('poll', 'chart', 'candidate', 'election', 'people', 'comparison')

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

        self.add_polyline('baseline',(6,24),(12,24),(24,24),(36,24),(42,24))
        for i,(x,y) in enumerate(((12,16),(24,6),(36,11))):
            self.add_line('bar-'+str(i),(x,y),(x,24))
            self.relate('connect','baseline','bar-'+str(i))
            self.bust('candidate-'+str(i),x,35,r=2,width=6)
        self.relate('connect','candidate-0-shoulders','candidate-1-shoulders')
        self.relate('connect','candidate-1-shoulders','candidate-2-shoulders')
