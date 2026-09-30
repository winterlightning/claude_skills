"""Rejected pendant is squat and its tiny loop floats separately. Enlarge the loop and join it to a taller pointed pendant.
Plan: VRECT_M envelope; preserve source arrangement with coherent connected contours.
References: original and rejected SVGs visually compared before drawing.
Lucide apple/leaf for fruit and leaves, luggage for rounded case and straps,
scissors for crossing blades and loops, hand for rounded fingertips.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='6cdf2e13-8630-47a9-a6a3-a003f4cecfdb'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__teardrop-pendant-round-loop/20260929T130116Z-thuan-mac/reference/pendant_6cdf2e13-8630-47a9-a6a3-a003f4cecfdb.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='teardrop-pendant-round-loop'
    keyshape=Keyshape.VRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('pendant',)
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

        circle('loop',24,9,5)
        path('pendant',(24,14),[('C',(38,32),(29,18),(38,26)),('A',(24,44),14,12,True),('A',(10,32),14,12,True),('C',(24,14),(10,26),(19,18))],True);join('loop','pendant')
