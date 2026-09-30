"""Rejected hand is a stepped block with no rounded finger or thumb; restore a rounded raised finger and curved palm beneath three direction arrows.
Plan: HRECT_L exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: pointer and hand: rounded finger and thumb; arrow-up: shared shaft
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='52c32e39-3bac-4a0f-8904-0928470decff'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__hand-expansion-touch-gesture/20260929T135357Z-thuan-mac/reference/gesture expand 1_52c32e39-3bac-4a0f-8904-0928470decff.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='hand-expansion-touch-gesture'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('hand', 'expansion', 'touch', 'gesture')
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

        path('hand',(18,40),[('L',(14,34)),('C',(20,32),(11,29),(16,29)),('L',(22,34)),('L',(22,28)),('A',(30,28),4,4,True),('L',(30,34)),('L',(32,34)),('L',(32,40)),('L',(18,40))],True)
        poly('up',(20,12),(24,8),(28,12));line('up-shaft',(24,8),(24,16));join('up','up-shaft')
        poly('left',(8,18),(4,22),(8,26));poly('right',(40,18),(44,22),(40,26))
