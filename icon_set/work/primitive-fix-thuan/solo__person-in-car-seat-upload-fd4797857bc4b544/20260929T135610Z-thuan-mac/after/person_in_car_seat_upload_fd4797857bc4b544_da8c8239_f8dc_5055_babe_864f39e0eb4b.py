"""Current reference has a bulky enclosed seat and a disjoint angular body. Redraw seat as a smooth open profile with a recognizable seated torso and legs.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: human_ref/full_body_ref.png: circular head, coherent torso and limbs
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='da8c8239-f8dc-5055-babe-864f39e0eb4b'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__person-in-car-seat-upload-fd4797857bc4b544/20260929T135610Z-thuan-mac/reference/person-in-car-seat-upload-fd4797857bc4b544_da8c8239-f8dc-5055-babe-864f39e0eb4b.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='person-in-car-seat-upload-fd4797857bc4b544'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('person', 'in', 'car', 'seat', 'upload', 'fd4797857bc4b544')
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

        oval('head',18,10,4,4)
        poly('torso',(18,22),(18,30),(32,30),(42,36))
        poly('arm',(18,22),(30,22),(36,18));join('arm','torso')
        path('seat',(6,22),[('C',(14,38),(8,28),(8,34)),('C',(30,42),(18,42),(24,42)),('L',(34,42))])
        self.mark_human_figure('person',head='head',torso='torso-1',torso_junction='start')
