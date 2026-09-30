"""The rejected straps replace both buckles with divider bars. Restore two protruding outlined buckles and matched rounded strap ends.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: No useful direct match.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='403d3b09-28f3-4968-b55e-9f29cb36fbe9'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__paired-adjustable-suspender-straps/20260929T135632Z-thuan-mac/reference/suspenders_403d3b09-28f3-4968-b55e-9f29cb36fbe9.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='paired-adjustable-suspender-straps'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('paired', 'adjustable', 'suspender', 'straps')
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

        for j,l in enumerate((6,28)):
         n='strap'+str(j)
         path(n+'top',(l+2,26),[('L',(l+2,10)),('A',(l+6,6),4,4,True),('L',(l+8,6)),('A',(l+12,10),4,4,True),('L',(l+12,26))])
         box(n+'buckle',l,26,l+14,34,2)
         path(n+'bottom',(l+2,34),[('L',(l+2,38)),('A',(l+6,42),4,4,False),('L',(l+8,42)),('A',(l+12,38),4,4,False),('L',(l+12,34))])
         join(n+'top',n+'buckle');join(n+'bottom',n+'buckle')
