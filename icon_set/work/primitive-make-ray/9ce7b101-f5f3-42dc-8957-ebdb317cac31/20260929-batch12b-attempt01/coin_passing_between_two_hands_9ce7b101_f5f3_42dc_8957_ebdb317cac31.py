"""Rejected coin is a solid dot far left and both hands are stiff. Restore an outlined coin between smooth opposing open hands.
Plan: VRECT_L; coherent source-specific contours with shared physical joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='9ce7b101-f5f3-42dc-8957-ebdb317cac31'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__coin-passing-between-two-hands/20260929T132613Z-thuan-mac/reference/begging hands give coin_9ce7b101-f5f3-42dc-8957-ebdb317cac31.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='coin-passing-between-two-hands'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('begging', 'hands', 'give', 'coin')
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

        path('upper',(40,4),[('L',(30,4)),('L',(22,8)),('A',(24,16),5,5,False),('L',(32,12)),('L',(40,12))])
        circle('coin',16,25,3)
        path('lower',(8,36),[('L',(18,36)),('L',(28,32)),('L',(34,32)),('A',(34,40),4,4,True),('L',(20,44)),('L',(8,44))])
