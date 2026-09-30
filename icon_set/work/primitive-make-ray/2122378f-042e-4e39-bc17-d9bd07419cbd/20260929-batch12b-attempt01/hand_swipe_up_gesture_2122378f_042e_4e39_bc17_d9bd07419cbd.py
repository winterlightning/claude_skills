"""Rejected index finger ends in an arrow-like point and the thumb is square. Restore a round fingertip and a softly hooked thumb below the finger.
Plan: HRECT_L; coherent source-specific contours with shared physical joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='2122378f-042e-4e39-bc17-d9bd07419cbd'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__hand-swipe-up-gesture/20260929T132937Z-thuan-mac/reference/gesture swipe vertical up 2_2122378f-042e-4e39-bc17-d9bd07419cbd.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='hand-swipe-up-gesture'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('gesture', 'swipe', 'vertical', 'up', '2')
    def build(self):

        def path(name,start,steps,closed=False):
            here=start; members=[]
            for i,step in enumerate(steps):
                kind,end,*args=step; ident=f"{name}-{i}"
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                here=end; members.append(ident)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def join(a,b): self.relate('connect',a,b)

        def box(name,l,t,r,b,rad=0):
            if not rad:self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),closed=True)
            else:path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

        path('hand',(4,38),[('L',(4,28)),('L',(18,22)),('L',(40,22)),('A',(40,30),4,4,True),('L',(26,30)),('L',(26,34)),('C',(22,40),(32,34),(30,40)),('L',(4,38))],True)
        self.add_polyline('arrowhead',(20,12),(24,8),(28,12));self.add_line('shaft',(24,8),(24,14));join('arrowhead','shaft')
