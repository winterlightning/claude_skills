"""The rejected arrows are tiny chevrons without shafts. Restore clear up/down arrows and a rounded horizontal finger between them.
Plan: VRECT_L exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: Lucide move-vertical: aligned shafts and open arrowheads.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='29be15de-fd49-4163-972a-6f0743088f4e'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__vertical-swipe-gesture/20260929T145934Z-thuan-mac/reference/gesture swipe vertical 1_29be15de-fd49-4163-972a-6f0743088f4e.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='vertical-swipe-gesture'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('vertical', 'swipe', 'gesture')
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

        path('finger',(8,20),[('L',(34,20)),('A',(34,28),4,4,True),('L',(8,28))])
        for n,tip,base in [('up',4,12),('down',44,36)]:
         line(n+'shaft',(32,base),(32,tip));poly(n+'head',(26,base),(32,tip),(38,base));join(n+'shaft',n+'head')
