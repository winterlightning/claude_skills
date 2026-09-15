"""A rounded handle narrows at its neck before widening into a broad comb head. Five long straight teeth descend from a horizontal shoulder line, leaving evenly spaced open gaps.
Symbol plan: Vertical rounded handle broadens into comb shoulder. Five teeth at constant 8-unit pitch; shared shoulder attachments.
Keyshape: VRECT_L, centerline extremes (8,4)-(40,44).
Construction reference: paint-roller; original and atomic geometry inspected when Lucide.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cb84f932-5046-413c-af40-b7d48cc9230d'
SOURCE_PATH = 'pictographic-primitives/beauty/hair dress comb 1_cb84f932-5046-413c-af40-b7d48cc9230d.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'wide-toothed-hair-pick'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'beauty'
    aliases = ()
    keywords = ('wide', 'toothed', 'hair', 'pick')

    def build(self):

        def segments(name, *points):
            for j,(a,b) in enumerate(zip(points,points[1:]),1):
                self.add_line(f'{name}-{j}',a,b)

        def circle(name, cx, cy, r):
            self.add_arc(name+'-top', (cx-r,cy), (cx+r,cy), radius_x=r)
            self.add_arc(name+'-bottom', (cx+r,cy), (cx-r,cy), radius_x=r)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)

        def rect(name, l,t,r,b, radius=0):
            if not radius:
                self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),closed=True)
                return
            q=radius
            points=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q),(l+q,t)]
            ids=[]
            for j,(a,z) in enumerate(zip(points,points[1:])):
                if a==z: continue
                part=f'{name}-{j}'
                if j%2: self.add_arc(part,a,z,radius_x=q)
                else: self.add_line(part,a,z)
                ids.append(part)
            self.add_contour(name,*ids,closed=True)

        def axes():
            self.add_line('axis-y',(6,6),(6,38))
            self.add_arc('axis-corner',(6,38),(10,42),radius_x=4,sweep=False)
            self.add_line('axis-x',(10,42),(42,42))
            self.add_contour('axes','axis-y','axis-corner','axis-x')

        self.add_arc('handle-top',(18,10),(30,10),radius_x=6)
        self.add_line('handle-right',(30,10),(30,18))
        self.add_arc('shoulder-right',(30,18),(40,28),radius_x=10,sweep=False)
        segments('comb-top',(40,28),(32,28),(24,28),(16,28),(8,28))
        self.add_arc('shoulder-left',(8,28),(18,18),radius_x=10,sweep=False)
        self.add_line('handle-left',(18,18),(18,10))
        self.add_contour('head','handle-top','handle-right','shoulder-right','comb-top-1','comb-top-2','comb-top-3','comb-top-4','shoulder-left','handle-left',closed=True)
        for j in range(5):
         x=8+8*j
         self.add_line(f'tooth-{j}',(x,28),(x,44))
         self.relate('connect',f'tooth-{j}','head')
