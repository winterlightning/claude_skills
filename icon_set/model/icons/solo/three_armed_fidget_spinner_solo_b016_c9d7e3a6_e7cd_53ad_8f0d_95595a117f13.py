"""Three-lobed spinner with top and paired lower lobes. Central bearing retained; tiny peripheral bearings omitted to preserve clear lobes at48. Centerline6,6–42,42.
Lucide construction reference: No useful exact Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='c9d7e3a6-e7cd-53ad-8f0d-95595a117f13'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/toys fidget spinner_c9d7e3a6-e7cd-53ad-8f0d-95595a117f13.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/toys fidget spinner_c9d7e3a6-e7cd-53ad-8f0d-95595a117f13.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-016/references/toys fidget spinner_c9d7e3a6-e7cd-53ad-8f0d-95595a117f13.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='three-armed-fidget-spinner-solo-b016'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "kids"
    categories = ("primitives", "kids")
    aliases=()
    keywords=('three', 'armed', 'fidget', 'spinner')
    def build(self):

        def circle(n,x,y,r):
            pts=((x-r,y),(x,y-r),(x+r,y),(x,y+r));members=[]
            for i in range(4):
                m=n+str(i);self.add_arc(m,pts[i],pts[(i+1)%4],radius_x=r);members.append(m)
            self.add_contour(n,*members,closed=True)
        def path(n,start,commands,closed=False):
            p=start;members=[]
            for i,c in enumerate(commands):
                m=n+str(i);q=c[-1]
                if c[0]=='L':self.add_line(m,p,q)
                elif c[0]=='A':self.add_arc(m,p,q,radius_x=c[1],radius_y=c[2],sweep=c[3])
                elif c[0]=='B':self.add_bezier(m,p,(c[1],c[2],q))
                members.append(m);p=q
            self.add_contour(n,*members,closed=closed)

        path('spinner',(16,14),[('A',8,8,True,(32,14)),('B',(32,23),(34,24),(38,26)),('B',(41,28),(42,30),(42,34)),('A',8,8,True,(34,42)),('B',(29,42),(28,34),(24,34)),('B',(20,34),(19,42),(14,42)),('A',8,8,True,(6,34)),('B',(6,30),(7,28),(10,26)),('B',(14,24),(16,23),(16,14))],True)
        self.add_dot('bearing',(24,23))
