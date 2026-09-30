"""Vertical dumbbell links replace the horizontal interlocked chain. Restore two offset horizontal open capsules.
Plan: HRECT_L exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: No useful exact match; source capsule links and shared rounded construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='28673231-6d46-5446-ab57-4cfa5240085c'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__personal-hotspot-connection/20260929T135610Z-thuan-mac/reference/personal hotspot connection_28673231-6d46-5446-ab57-4cfa5240085c.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='personal-hotspot-connection'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('personal', 'hotspot', 'connection')
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

        path('upper-link',(4,18),[('A',(14,8),10,10,True),('L',(30,8)),('A',(30,28),10,10,True),('L',(26,28))])
        path('lower-link',(24,20),[('L',(22,20)),('A',(22,40),10,10,False),('L',(34,40)),('A',(44,30),10,10,False)])
