"""Abstract ballot trapezoid above a rounded box. Lucide vote informs the ballot/box hierarchy; the supplied detached insertion layout is retained.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='5ca61ae4-1cec-4ea5-8502-86356d125601'
SOURCE_PATH='pictographic-primitives/symbol/vote_5ca61ae4-1cec-4ea5-8502-86356d125601.svg'
AUTHOR='gpt-6'

class BallotBoxVote(Solo48):
    icon_id='ballot-box-vote'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "symbol"
    categories = ("symbol", "state")
    aliases=()
    keywords=('vote', 'ballot', 'election', 'box', 'poll', 'democracy', 'choice', 'civic')

    def oval(self,n,cx,cy,rx,ry=None):
        ry=rx if ry is None else ry
        self.add_arc(n+'-top',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(n+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)

    def raw(self,n,points):
        for j,(a,b) in enumerate(zip(points,points[1:]),1):self.add_line(n+'-'+str(j),a,b)

    def path(self,n,points,closed=False):
        self.add_polyline(n,*points,closed=closed)

    def build(self):

        self.path('ballot',[(14,6),(34,6),(28,16),(20,16)],True)
        self.add_line('top',(12,26),(36,26));self.add_arc('tr',(36,26),(42,32),radius_x=6)
        self.add_line('right',(42,32),(42,36));self.add_arc('br',(42,36),(36,42),radius_x=6)
        self.add_line('base',(36,42),(12,42));self.add_arc('bl',(12,42),(6,36),radius_x=6)
        self.add_line('left',(6,36),(6,32));self.add_arc('tl',(6,32),(12,26),radius_x=6)
        self.add_contour('box','top','tr','right','br','base','bl','left','tl',closed=True)
