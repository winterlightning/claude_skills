"""A smooth line rises through two rounded peaks and intervening dips inside left and bottom axes. It begins near the lower-left and finishes high on the right with an upward turn.
Symbol plan: Rising smooth data stroke: two crests and two dips constructed as tangent quarter ellipses, isolated from rounded L axes.
Keyshape: SQUARE, centerline extremes (6,6)-(42,42).
Construction reference: chart-spline; original and atomic geometry inspected when Lucide.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '82b336ab-b6e2-5e37-a1d9-2432b628d6d6'
SOURCE_PATH = 'pictographic-primitives/business/graph lines_82b336ab-b6e2-5e37-a1d9-2432b628d6d6.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'rising-line-chart-with-two-dips'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    aliases = ()
    keywords = ('rising', 'line', 'chart', 'with', 'two', 'dips')

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
        self.add_arc('rise1',(15,32),(19,20),radius_x=4,radius_y=12)
        self.add_arc('dip1a',(19,20),(23,24),radius_x=4,radius_y=4)
        self.add_arc('dip1b',(23,24),(27,28),radius_x=4,radius_y=4,sweep=False)
        self.add_arc('rise2a',(27,28),(31,19),radius_x=4,radius_y=9,sweep=False)
        self.add_arc('rise2b',(31,19),(35,10),radius_x=4,radius_y=9)
        self.add_arc('dip2a',(35,10),(38,12),radius_x=3,radius_y=2)
        self.add_arc('dip2b',(38,12),(40,14),radius_x=2,radius_y=2,sweep=False)
        self.add_arc('end',(40,14),(42,12),radius_x=2,radius_y=2,sweep=False)
        self.add_contour('data','rise1','dip1a','dip1b','rise2a','rise2b','dip2a','dip2b','end')
