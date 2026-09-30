"""Rejected sprayer has a single floating dash and squat reservoir. Restore a diverging spray pair, clearer feed tube and more natural gun grip.
Plan: SQUARE envelope; preserve source arrangement with coherent connected contours.
References: original and rejected SVGs visually compared before drawing.
Lucide apple/leaf for fruit and leaves, luggage for rounded case and straps,
scissors for crossing blades and loops, hand for rounded fingertips.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='c7b717ca-423a-41ee-ad70-88e50f6aa4d6'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__paint-spray-gun-bottle/20260929T130116Z-thuan-mac/reference/paint sprayer_c7b717ca-423a-41ee-ad70-88e50f6aa4d6.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='paint-spray-gun-bottle'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('paint', 'sprayer')
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

        box('housing',6,6,26,18,3)
        self.add_polyline('grip',(10,18),(6,34),(14,34),(18,18));join('grip','housing')
        self.add_polyline('feed',(26,18),(26,26),(34,26),(34,30));join('feed','housing')
        box('reservoir',26,30,42,42,4);join('feed','reservoir')
        self.add_line('spray-upper',(36,8),(42,6))
        self.add_line('spray-lower',(36,18),(42,20))
