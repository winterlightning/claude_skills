"""Rejected fruit is a squat bowl beneath a tall stalk. Restore a full pear-like citrus body and a short stalk with a single pointed leaf.
Plan: VRECT_L envelope; preserve source arrangement with coherent connected contours.
References: original and rejected SVGs visually compared before drawing.
Lucide apple/leaf for fruit and leaves, luggage for rounded case and straps,
scissors for crossing blades and loops, hand for rounded fingertips.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='f3960946-7472-4368-97d7-b7f1d979eed7'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__pomelo-with-single-leaf/20260929T130116Z-thuan-mac/reference/pomelo_f3960946-7472-4368-97d7-b7f1d979eed7.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='pomelo-with-single-leaf'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('pomelo',)
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

        path('fruit',(20,22),[('C',(40,32),(27,22),(40,24)),('C',(24,44),(40,39),(31,44)),('C',(8,32),(15,44),(8,39)),('C',(20,22),(8,27),(14,25))],True)
        self.add_line('stem',(20,22),(26,14));join('stem','fruit')
        path('leaf',(26,14),[('C',(40,4),(26,4),(34,4)),('C',(26,14),(40,14),(32,14))],True);join('stem','leaf')
