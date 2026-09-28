"""A padded salon chair is shown from the side with a tall curved back, rounded seat and raised armrest. A central pedestal supports it above a broad foot, with a front footrest extending right.
Symbol plan: Side-view chair with a tangent rounded back-to-seat, armrest, pedestal and forward footrest. Drop duplicate cushion outline.
Keyshape: HRECT_L, centerline extremes (4,8)-(44,40).
Construction reference: armchair; original and atomic geometry inspected when Lucide.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd057f678-f39c-50d4-9554-598acaf09010'
SOURCE_PATH = 'pictographic-primitives/beauty/hair dress chair_d057f678-f39c-50d4-9554-598acaf09010.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'salon-chair-with-footrest'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'beauty'
    categories = ('primitives', 'beauty')
    aliases = ()
    keywords = ('salon', 'chair', 'with', 'footrest')

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

        self.add_line('back',(4,8),(4,24))
        self.add_arc('elbow',(4,24),(12,32),radius_x=8,sweep=False)
        segments('seat',(12,32),(24,32),(34,32))
        self.add_contour('chair','back','elbow','seat-1','seat-2')
        self.add_polyline('arm',(14,16),(24,16),(24,23))
        self.add_line('pedestal',(24,32),(24,40))
        self.add_polyline('base',(12,40),(24,40),(32,40))
        self.relate('connect','pedestal','base');self.relate('connect','pedestal','chair')
        self.add_polyline('footrest',(34,32),(38,40),(44,40))
        self.relate('connect','chair','footrest')
