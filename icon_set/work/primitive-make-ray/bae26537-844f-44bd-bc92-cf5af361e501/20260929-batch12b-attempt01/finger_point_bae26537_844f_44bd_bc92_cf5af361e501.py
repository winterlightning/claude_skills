"""Rejected long central finger can read as a middle-finger gesture. Move the raised index to the left of the folded finger group and restore a broader thumb and palm.
Plan: VRECT_L; coherent source-specific contours with shared physical joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='bae26537-844f-44bd-bc92-cf5af361e501'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__finger-point/20260929T132613Z-thuan-mac/reference/finger point_bae26537-844f-44bd-bc92-cf5af361e501.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='finger-point'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('finger', 'point')
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

        path('hand',(8,32),[('C',(16,22),(8,25),(11,22)),('L',(16,8)),('A',(24,8),4,4,True),('L',(24,20)),('A',(32,20),4,4,True),('L',(32,24)),('A',(40,24),4,4,True),('L',(40,32)),('A',(24,44),16,12,True),('A',(8,32),16,12,True)],True)
        self.add_line('thumb-fold',(16,22),(16,30));join('thumb-fold','hand')
        self.add_line('finger-fold',(24,20),(24,26));join('finger-fold','hand')
        self.add_line('little-fold',(32,24),(32,28));join('little-fold','hand')
