"""Only the current drawing is available. Its arrow is a short bent mark and the finger arches are broad. Restore a long rightward shaft above two evenly sized fingers.
Plan: HRECT_L exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: Lucide move-vertical: shaft and open arrowhead; original supplies two fingers.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='7f5803c7-8dd5-55b8-bf1c-b02fdaa2a3bd'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__two-finger-swipe-right-upload-27a8bf31fe0cadb0/20260929T145934Z-thuan-mac/reference/two-finger-swipe-right-upload-27a8bf31fe0cadb0_7f5803c7-8dd5-55b8-bf1c-b02fdaa2a3bd.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='two-finger-swipe-right-upload-27a8bf31fe0cadb0'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('two', 'finger', 'swipe', 'right', 'upload', '27a8bf31fe0cadb0')
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

        for n,l,r in [('first',4,20),('second',28,44)]:
         path(n,(l,40),[('L',(l,34)),('A',(r,34),8,8,True),('L',(r,40))])
        line('shaft',(18,12),(38,12));poly('head',(32,8),(38,12),(32,16));join('shaft','head')
