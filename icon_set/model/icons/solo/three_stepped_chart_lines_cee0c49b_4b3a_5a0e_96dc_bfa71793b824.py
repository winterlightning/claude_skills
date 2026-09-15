"""Three separate horizontal step lines run across a chart framed by left and bottom axes. Each changes level through square rises and drops, with the upper line finishing highest.
Symbol plan: Three step series, consistent 12-unit vertical spacing. Preserve independent series and orthogonal steps; simplify each to one level change.
Keyshape: SQUARE, centerline extremes (6,6)-(42,42).
Construction reference: chart-gantt; original and atomic geometry inspected when Lucide.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cee0c49b-4b3a-5a0e-96dc-bfa71793b824'
SOURCE_PATH = 'pictographic-primitives/business/graph stepped area chart_cee0c49b-4b3a-5a0e-96dc-bfa71793b824.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'three-stepped-chart-lines'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    aliases = ()
    keywords = ('three', 'stepped', 'chart', 'lines')

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

        axes()
        for j,y in enumerate((9,21,33)):
         self.add_polyline(f'series-{j}',(16,y),(28,y),(28,y-3),(42,y-3))
