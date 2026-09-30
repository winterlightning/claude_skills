"""Rejected pointing hand and swipe path are angular polygons. Restore rounded fingertip, thumb and a continuous smooth downward arrow curve.
Plan: HRECT_L; coherent source-specific contours with shared physical joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='03865b1d-fc66-475a-9459-24a0071714cf'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__hand-gesture-vertical-swipe-down/20260929T132937Z-thuan-mac/reference/gesture swipe vertical down 2_03865b1d-fc66-475a-9459-24a0071714cf.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='hand-gesture-vertical-swipe-down'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('gesture', 'swipe', 'vertical', 'down', '2')
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

        path('hand',(4,30),[('L',(4,22)),('L',(12,14)),('C',(20,14),(16,10),(24,10)),('L',(20,18)),('L',(26,18)),('A',(26,26),4,4,True),('L',(20,26)),('L',(18,34)),('L',(4,32)),('L',(4,30))],True)
        path('swipe',(40,8),[('C',(44,22),(44,14),(44,17)),('C',(32,40),(44,30),(40,35))])
        self.add_polyline('arrowhead',(34,32),(32,40),(40,38));join('arrowhead','swipe')
