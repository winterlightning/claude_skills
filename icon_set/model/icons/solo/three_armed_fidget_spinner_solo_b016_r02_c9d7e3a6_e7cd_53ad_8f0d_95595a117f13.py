"""Three-lobed spinner with central bearing circle and smooth waist transitions. Peripheral holes omitted to preserve clearance. Top and lower lobe radii9/8; centerline6,6–42,42.
Construction reference: No useful exact Lucide match; supplied reference.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='c9d7e3a6-e7cd-53ad-8f0d-95595a117f13'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/toys fidget spinner_c9d7e3a6-e7cd-53ad-8f0d-95595a117f13.svg'
SAVED_REFERENCE_PATH='/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/toys fidget spinner_c9d7e3a6-e7cd-53ad-8f0d-95595a117f13.svg'
EXPORTED_REFERENCE_PATH='work/brief-exports/20260918-all-todo-batches-15/batches/batch-016/references/toys fidget spinner_c9d7e3a6-e7cd-53ad-8f0d-95595a117f13.svg'
AUTHOR='gpt-6'
class BatchIcon(Solo48):
    icon_id='three-armed-fidget-spinner-solo-b016-r02'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "kids"
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

        path('spinner',(15,15),[('A',9,9,True,(33,15)),('B',(33,20),(37,25),(38,26)),('B',(41,28),(42,30),(42,34)),('A',8,8,True,(34,42)),('B',(29,42),(28,36),(24,36)),('B',(20,36),(19,42),(14,42)),('A',8,8,True,(6,34)),('B',(6,30),(7,28),(10,26)),('B',(11,25),(15,20),(15,15))],True)
        circle('bearing',24,25,2)
