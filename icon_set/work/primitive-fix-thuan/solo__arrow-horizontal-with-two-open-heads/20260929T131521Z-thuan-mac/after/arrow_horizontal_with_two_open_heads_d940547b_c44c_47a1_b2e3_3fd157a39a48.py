"""Steep narrow arrowheads distort the 45-degree open heads in the source. Rebalance as matched 45-degree heads.
Plan: HRECT_M exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: move-horizontal: mirrored chevrons and shaft
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='d940547b-c44c-47a1-b2e3-3fd157a39a48'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__arrow-horizontal-with-two-open-heads/20260929T131521Z-thuan-mac/reference/look both ways 1_d940547b-c44c-47a1-b2e3-3fd157a39a48.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='arrow-horizontal-with-two-open-heads'
    keyshape=Keyshape.HRECT_M
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('arrow', 'horizontal', 'with', 'two', 'open', 'heads')
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

        line('shaft',(4,24),(44,24))
        for n,sgn in [('left',1),('right',-1)]:
         x=4 if sgn==1 else 44
         poly(n,(x+14*sgn,10),(x,24),(x+14*sgn,38));join(n,'shaft')
