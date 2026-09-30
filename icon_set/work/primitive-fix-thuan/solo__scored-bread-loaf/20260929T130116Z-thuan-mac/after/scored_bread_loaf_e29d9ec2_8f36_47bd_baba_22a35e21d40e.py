"""Rejected loaf looks like a tall square bread slice. Restore a broad rounded loaf and curved oblique score marks; retain two scores for clearance.
Plan: HRECT_M envelope; preserve source arrangement with coherent connected contours.
References: original and rejected SVGs visually compared before drawing.
Lucide apple/leaf for fruit and leaves, luggage for rounded case and straps,
scissors for crossing blades and loops, hand for rounded fingertips.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='e29d9ec2-8f36-47bd-baba-22a35e21d40e'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__scored-bread-loaf/20260929T130116Z-thuan-mac/reference/loaf_e29d9ec2-8f36-47bd-baba-22a35e21d40e.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='scored-bread-loaf'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('loaf',)
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
            if rad==0:
                self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),closed=True)
            else:
                path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

        path('loaf',(4,24),[('C',(16,11),(4,17),(8,12)),('C',(28,10),(20,10),(24,10)),('C',(44,24),(39,10),(44,17)),('C',(24,38),(44,36),(35,38)),('C',(4,24),(13,38),(4,36))],True)
        path('score-left',(16,11),[('C',(22,23),(20,14),(21,19))]);join('score-left','loaf')
        path('score-right',(28,10),[('C',(34,22),(32,14),(33,18))]);join('score-right','loaf')
