"""Rejected contact arc is a jagged polyline and finger is too thin. Round the contact arc and widen the horizontal fingertip while preserving the upward arrow.
Plan: SQUARE; coherent source-specific contours with shared physical joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='34ac1798-6cb8-43a2-9504-66d8147d1e43'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__hand-gesture-swipe-up/20260929T132937Z-thuan-mac/reference/gesture tap swipe up_34ac1798-6cb8-43a2-9504-66d8147d1e43.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='hand-gesture-swipe-up'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('gesture', 'tap', 'swipe', 'up')
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

        path('finger',(6,25),[('L',(26,25)),('A',(26,35),5,5,True),('L',(6,35))])
        path('contact',(34,18),[('C',(42,29),(40,18),(42,23)),('C',(32,42),(42,35),(38,40))])
        self.add_polyline('arrowhead',(20,10),(24,6),(28,10));self.add_line('shaft',(24,6),(24,14));join('arrowhead','shaft')
