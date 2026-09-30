"""Wireless arcs omitted; boxes read as wired devices. Restore a radio arc above each diagonal router.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: router: antenna and wireless arc
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='5a93e8de-6f91-4fe6-b134-63af89e10c77'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__two-linked-wifi-routers/20260929T131521Z-thuan-mac/reference/mesh wifi_5a93e8de-6f91-4fe6-b134-63af89e10c77.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='two-linked-wifi-routers'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('two', 'linked', 'wifi', 'routers')
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

        box('router-a',6,18,18,26,2)
        box('router-b',30,34,42,42,2)
        line('antenna-a',(12,14),(12,18));join('antenna-a','router-a')
        line('antenna-b',(36,30),(36,34));join('antenna-b','router-b')
        path('wifi-a',(6,9),[('A',(18,9),6,3,True)])
        path('wifi-b',(30,25),[('A',(42,25),6,3,True)])
        line('link',(12,35),(20,40))
