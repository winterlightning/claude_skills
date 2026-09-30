"""The rejected stress marks are three right-facing chevrons and its head is undersized. Restore irregular lightning-like stress marks above a larger circular head and shoulders.
Plan: VRECT_L exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: human_ref/user.svg: round head and smooth shoulders; exact detached head gap 4 ink.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='e097b5d9-237a-5a21-8e1e-3426dec249b1'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__stressed-person/20260929T145934Z-thuan-mac/reference/user man stress_e097b5d9-237a-5a21-8e1e-3426dec249b1.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='stressed-person'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('stressed', 'person')
    def build(self):

        def path(n,start,steps,closed=False):
            members=[];here=start
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{j}'
                if kind=='L':self.add_line(m,here,end)
                elif kind=='A':self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C':self.add_bezier(m,here,(args[0],args[1],end))
                members.append(m);here=end
            self.add_contour(n,*members,closed=closed)
        def oval(n,x,y,rx,ry):path(n,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(n,l,t,r,b,rad=0):
            if not rad:self.add_polyline(n,(l,t),(r,t),(r,b),(l,b),closed=True);return
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        oval('head',24,24,7,7)
        path('shoulders',(8,44),[('A',(24,39),16,5,True),('A',(40,44),16,5,True)])
        poly('stress-left',(8,4),(12,8),(8,10),(12,14));poly('stress-right',(40,4),(36,8),(40,10),(36,14))
