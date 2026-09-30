"""Broad shallow pin resembles a fan; restore rounded teardrop marker and a slightly tapered map.
Plan: VRECT_L exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: map-pin: rounded crown tapering to a point
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='77035164-f010-491d-b43f-e3c91b10d2d0'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__map-with-location-pin/20260929T135357Z-thuan-mac/reference/maps pin_77035164-f010-491d-b43f-e3c91b10d2d0.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='map-with-location-pin'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('map', 'with', 'location', 'pin')
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

        path('pin',(14,14),[('A',(34,14),10,10,True),('C',(24,28),(34,19),(28,24)),('C',(14,14),(20,24),(14,19))],True)
        self.add_dot('center',(24,14))
        poly('map',(10,26),(8,44),(40,44),(38,26))
        line('map-row',(9,36),(39,36));join('map-row','map')
        for x in (18,30):line(f'fold{x}',(x,36),(x,44));join(f'fold{x}','map');join(f'fold{x}','map-row')
