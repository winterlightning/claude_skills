"""Three tall triangular peaks share a horizontal baseline inside left and bottom chart axes. Their heights vary, with the rightmost peak tallest and the central peak shortest.
Symbol plan: Three triangular peaks with unequal heights and common baseline. Omit redundant left axis; keep all three data peaks.
Keyshape: HRECT_L, centerline extremes (4,8)-(44,40).
Construction reference: chart-area; original and atomic geometry inspected when Lucide.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '43f2faa5-08d7-4977-9c37-ff132822efe7'
SOURCE_PATH = 'pictographic-primitives/business/graph bars pyramid stacked_43f2faa5-08d7-4977-9c37-ff132822efe7.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'chart-with-three-triangular-peaks'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('chart', 'with', 'three', 'triangular', 'peaks')

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

        self.add_polyline('peaks',(4,40),(10,16),(18,40),(24,24),(30,40),(38,8),(44,40),(30,40),(18,40),closed=True)
