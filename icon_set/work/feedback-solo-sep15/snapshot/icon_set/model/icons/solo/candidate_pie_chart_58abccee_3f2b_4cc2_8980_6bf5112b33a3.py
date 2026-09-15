"""Lucide user-round: two repeated candidate busts beside a three-sector pie; directional results layout retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '58abccee-3f2b-4cc2-8980-6bf5112b33a3'
SOURCE_PATH = 'pictographic-primitives/school-learning/election result 1_58abccee-3f2b-4cc2-8980-6bf5112b33a3.svg'
AUTHOR = 'gpt-6'


class CandidatePieChart(Solo48):
    icon_id = 'candidate-pie-chart'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "society/elections"
    aliases = ()
    keywords = ('candidate', 'pie', 'chart', 'result', 'election', 'people')

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

        self.circle('pie',17,28,11)
        self.add_polyline('sector',(17,17),(17,28),(28,28))
        self.add_line('third-sector',(17,28),(9,36))
        self.relate('connect','pie','sector')
        self.relate('connect','sector','third-sector')
        self.relate('connect','pie','third-sector')
        self.bust('candidate-top',38,8,r=2,width=4)
        self.bust('candidate-bottom',38,35,r=2,width=4)
