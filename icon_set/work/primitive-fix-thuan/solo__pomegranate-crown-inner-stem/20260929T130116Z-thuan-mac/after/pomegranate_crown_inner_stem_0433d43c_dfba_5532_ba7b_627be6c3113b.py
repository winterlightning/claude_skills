"""Rejected oval fruit has three bare crown rays. Restore the pointed calyx as part of the fruit silhouette and an asymmetric branching inner stem.
Plan: VRECT_L envelope; preserve source arrangement with coherent connected contours.
References: original and rejected SVGs visually compared before drawing.
Lucide apple/leaf for fruit and leaves, luggage for rounded case and straps,
scissors for crossing blades and loops, hand for rounded fingertips.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='0433d43c-dfba-5532-ba7b-627be6c3113b'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__pomegranate-crown-inner-stem/20260929T130116Z-thuan-mac/reference/pomegranate_0433d43c-dfba-5532-ba7b-627be6c3113b.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='pomegranate-crown-inner-stem'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('pomegranate',)
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

        path('fruit',(16,18),[('C',(8,28),(10,21),(8,23)),('A',(24,44),16,16,False),('A',(40,28),16,16,False),('C',(32,18),(40,23),(38,21)),('L',(34,10)),('L',(28,12)),('L',(24,4)),('L',(20,12)),('L',(14,10)),('L',(16,18))],True)
        self.add_polyline('stem',(24,23),(24,29),(24,35))
        self.add_line('branch-left',(24,29),(18,26));join('stem','branch-left')
        self.add_line('branch-right',(24,29),(28,26));join('stem','branch-right');join('branch-left','branch-right')
