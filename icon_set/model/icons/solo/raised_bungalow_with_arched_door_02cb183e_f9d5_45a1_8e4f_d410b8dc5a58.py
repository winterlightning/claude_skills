"""A small bungalow has a broad curved roof over two straight supporting walls. An arched doorway opens centrally, while a low horizontal platform line crosses the supports near the base.
Symbol plan: Mirror a half-ellipse roof and walls about x=24. Arched entrance, raised floor and post ends. Remove duplicate platform edges.
Keyshape: HRECT_L, centerline extremes (4,8)-(44,40).
Construction reference: house; original and atomic geometry inspected when Lucide.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '02cb183e-f9d5-45a1-8e4f-d410b8dc5a58'
SOURCE_PATH = 'pictographic-primitives/building/floating bungalow 1_02cb183e-f9d5-45a1-8e4f-d410b8dc5a58.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'raised-bungalow-with-arched-door'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'building'
    categories = ('building', 'primitives')
    aliases = ()
    keywords = ('raised', 'bungalow', 'with', 'arched', 'door')

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

        self.add_arc('roof-curve',(4,20),(44,20),radius_x=20,radius_y=12)
        segments('eaves',(44,20),(40,20),(8,20),(4,20))
        self.add_contour('roof','roof-curve','eaves-1','eaves-2','eaves-3',closed=True)
        for x in (8,40):
         self.add_polyline(f'post-{x}',(x,20),(x,36),(x,40))
         self.relate('connect','roof',f'post-{x}')
        self.add_line('floor-left',(8,36),(20,36))
        self.add_line('floor-right',(28,36),(40,36))
        self.relate('connect','floor-left','post-8')
        self.relate('connect','floor-right','post-40')
        self.add_line('door-left',(20,36),(20,32))
        self.add_arc('door-arch',(20,32),(28,32),radius_x=4)
        self.add_line('door-right',(28,32),(28,36))
        self.add_contour('door','door-left','door-arch','door-right')
        self.relate('connect','door','floor-left')
        self.relate('connect','door','floor-right')
