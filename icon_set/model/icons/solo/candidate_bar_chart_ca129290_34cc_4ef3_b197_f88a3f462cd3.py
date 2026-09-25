"""Lucide user-round: paired busts aligned with unequal outlined bars; shared vertical axis retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ca129290-34cc-4ef3-b197-f88a3f462cd3'
SOURCE_PATH = 'pictographic-primitives/school-learning/election result_ca129290-34cc-4ef3-b197-f88a3f462cd3.svg'
AUTHOR = 'gpt-6'


class CandidateBarChart(Solo48):
    icon_id = 'candidate-bar-chart'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "school-learning"
    aliases = ()
    keywords = ('candidate', 'bar', 'chart', 'result', 'election', 'comparison')

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

        self.bust('candidate-top',11,8,r=2,width=5)
        self.bust('candidate-bottom',11,35,r=2,width=5)
        self.add_polyline('axis',(25,6),(25,12),(25,20),(25,32),(25,40),(25,42))
        self.add_polyline('bar-top',(25,12),(42,12),(42,20),(25,20))
        self.add_polyline('bar-bottom',(25,32),(35,32),(35,40),(25,40))
        self.relate('connect','axis','bar-top')
        self.relate('connect','axis','bar-bottom')
