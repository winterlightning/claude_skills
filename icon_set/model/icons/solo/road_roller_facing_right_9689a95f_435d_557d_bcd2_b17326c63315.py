"""A side-view road roller has a tall cab behind a low engine hood. A large front drum and smaller rear wheel are joined by a long rounded horizontal support arm.
Symbol plan: Two unequal circular wheels, cab and hood contour, shared wheel attachment points. Directional side view; omit window mullion and duplicate arm outline.
Keyshape: HRECT_L, centerline extremes (4,8)-(44,40).
Construction reference: tractor; original and atomic geometry inspected when Lucide.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9689a95f-435d-557d-bcd2-b17326c63315'
SOURCE_PATH = 'pictographic-primitives/construction/flattener_9689a95f-435d-557d-bcd2-b17326c63315.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'road-roller-facing-right'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'construction'
    categories = ('construction', 'primitives')
    aliases = ()
    keywords = ('road', 'roller', 'facing', 'right')

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

        circle('rear-wheel',10,34,6)
        circle('front-drum',35,31,9)
        self.add_polyline('cab-hood',(10,28),(10,8),(22,8),(22,14),(26,14),(35,22))
        self.relate('connect','cab-hood','rear-wheel')
        self.relate('connect','cab-hood','front-drum')
        self.add_line('chassis',(16,34),(26,31))
        self.relate('connect','chassis','rear-wheel')
        self.relate('connect','chassis','front-drum')
