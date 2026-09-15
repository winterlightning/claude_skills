"""Five separate horizontal data segments sit at different heights inside an L-shaped pair of chart axes. One touches the left axis, while the remaining segments float across the plotting area.
Symbol plan: Five horizontal segments on a shared 8-unit row step, plus L axes. Preserve staggered placement and one left-axis attachment.
Keyshape: SQUARE, centerline extremes (6,6)-(42,42).
Construction reference: chart-gantt; original and atomic geometry inspected when Lucide.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3fd40e5d-b34b-57f0-a5b0-1ab82c6f94d1'
SOURCE_PATH = 'pictographic-primitives/business/graph lines jumped_3fd40e5d-b34b-57f0-a5b0-1ab82c6f94d1.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'chart-with-floating-horizontal-segments'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    aliases = ()
    keywords = ('chart', 'with', 'floating', 'horizontal', 'segments')

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

        self.add_polyline('axes',(6,6),(6,30),(6,42),(42,42))
        for j,(x,y,z) in enumerate([(30,6,42),(14,14,24),(22,22,32),(6,30,16),(32,34,42)]):
         self.add_line(f'data-{j}',(x,y),(z,y))
        self.relate('connect','axes','data-3')
