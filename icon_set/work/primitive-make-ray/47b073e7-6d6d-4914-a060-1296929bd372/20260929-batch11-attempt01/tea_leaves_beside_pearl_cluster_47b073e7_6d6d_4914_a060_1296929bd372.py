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

        path('leaf-left',(12,25),[('C',(10,6),(4,19),(6,11)),('C',(12,25),(17,15),(17,19))],True)
        path('leaf-right',(12,25),[('C',(33,8),(17,15),(29,16)),('C',(12,25),(33,24),(24,27))],True);join('leaf-left','leaf-right')
        self.add_line('stem',(12,25),(6,37));join('stem','leaf-left');join('stem','leaf-right')
        circle('pearl-upper',36,29,6)
        circle('pearl-left',22,36,6)
        circle('pearl-right',38,40,2)
