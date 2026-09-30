"""The rejected infinity closes both source breaks and forms a central junction. Restore a single flowing open S-shaped loop with two free ends.
Plan: HRECT_M exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: No additional match needed; inspected source owns the open topology.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='1739e39c-1f28-5f58-b32d-18e847e5acf6'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__open-infinity-loop-batch-015-02/20260929T135617Z-thuan-mac/reference/loop_1739e39c-1f28-5f58-b32d-18e847e5acf6.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='open-infinity-loop-batch-015-02'
    keyshape=Keyshape.HRECT_M
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('open', 'infinity', 'loop', 'batch', '015', '02')
    def build(self):

        def path(n,start,steps,closed=False):
            members=[];here=start
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{j}'
                if kind=='L':self.add_line(m,here,end)
                elif kind=='A':self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C':self.add_bezier(m,here,(args[0],args[1],end))
                members.append(m);here=end
            self.add_contour(n,*members,closed=closed)
        def oval(n,x,y,rx,ry):path(n,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(n,l,t,r,b,rad=0):
            if not rad:self.add_polyline(n,(l,t),(r,t),(r,b),(l,b),closed=True);return
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('loop',(18,14),[('C',(14,10),(17,12),(16,10)),('A',(4,24),10,14,False),('A',(14,38),10,14,False),('C',(34,10),(22,38),(26,10)),('A',(44,24),10,14,True),('A',(34,38),10,14,True),('C',(30,34),(32,38),(31,36))])
