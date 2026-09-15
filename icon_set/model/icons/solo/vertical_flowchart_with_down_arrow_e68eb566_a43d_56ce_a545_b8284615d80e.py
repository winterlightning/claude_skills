"""A rounded start node connects vertically to a wide rectangular process node. The same central connector continues below the rectangle and ends in an open downward arrowhead.
Symbol plan: Centred capsule start, rectangular process and downward connector; intrinsic process arrow. Shared x=24 attachment nodes.
Keyshape: VRECT_L, centerline extremes (8,4)-(40,44).
Construction reference: workflow; original and atomic geometry inspected when Lucide.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e68eb566-a43d-56ce-a545-b8284615d80e'
SOURCE_PATH = 'pictographic-primitives/business/flow chart hierachy_e68eb566-a43d-56ce-a545-b8284615d80e.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'vertical-flowchart-with-down-arrow'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    aliases = ()
    keywords = ('vertical', 'flowchart', 'with', 'down', 'arrow')

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

        segments('start-top',(18,4),(30,4))
        self.add_arc('start-r',(30,4),(30,12),radius_x=4)
        segments('start-base',(30,12),(24,12),(18,12))
        self.add_arc('start-l',(18,12),(18,4),radius_x=4)
        self.add_contour('start','start-top-1','start-r','start-base-1','start-base-2','start-l',closed=True)
        self.add_line('link',(24,12),(24,22))
        self.add_polyline('process',(8,22),(24,22),(40,22),(40,30),(24,30),(8,30),closed=True)
        self.relate('connect','link','start')
        self.relate('connect','link','process')
        self.add_line('output',(24,30),(24,44))
        self.add_polyline('arrow',(16,36),(24,44),(32,36))
        self.relate('connect','output','arrow')
        self.relate('connect','output','process')
