"""Rejected leaf pair is symmetric and pearls are solid dots below it. Restore asymmetric leaves on a diagonal stem and three large outlined pearls beside them.
Plan: SQUARE envelope; preserve source arrangement with coherent connected contours.
References: original and rejected SVGs visually compared before drawing.
Lucide apple/leaf for fruit and leaves, luggage for rounded case and straps,
scissors for crossing blades and loops, hand for rounded fingertips.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='47b073e7-6d6d-4914-a060-1296929bd372'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__tea-leaves-beside-pearl-cluster/20260929T130116Z-thuan-mac/reference/bubble tea leaf_47b073e7-6d6d-4914-a060-1296929bd372.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='tea-leaves-beside-pearl-cluster'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('bubble', 'tea', 'leaf')
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

        path('leaf-left',(14,18),[('C',(6,6),(6,18),(6,12)),('C',(14,18),(14,7),(15,12))],True)
        path('leaf-right',(14,18),[('C',(32,6),(19,11),(27,13)),('C',(14,18),(30,18),(23,21))],True);join('leaf-left','leaf-right')
        self.add_line('stem',(14,18),(6,22));join('stem','leaf-left');join('stem','leaf-right')
        for x in (12,24,36):circle(f'pearl-{x}',x,36,6)
        join('pearl-12','pearl-24');join('pearl-24','pearl-36')
