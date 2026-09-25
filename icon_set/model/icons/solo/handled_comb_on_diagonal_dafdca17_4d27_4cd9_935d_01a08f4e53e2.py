"""A long comb angles from lower-left to upper-right, with a rounded handle and curved outer spine. A row of widely spaced straight teeth projects diagonally from its inner edge.
Symbol plan: Open diagonal comb spine with radius-5 circular handle and crown, exact 3:4 tangents. Three teeth share normal (6,8) and pitch (8,-6). Preserve the asymmetric tooth side and open spine.
Keyshape: CIRCLE, centerline extremes radius 20 about (24,24).
Construction reference: brush; original and atomic geometry inspected when Lucide.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'dafdca17-4d27-4cd9-935d-01a08f4e53e2'
SOURCE_PATH = 'pictographic-primitives/beauty/hair dress comb_dafdca17-4d27-4cd9-935d-01a08f4e53e2.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'handled-comb-on-diagonal'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'beauty'
    categories = ('primitives', 'beauty')
    aliases = ()
    keywords = ('handled', 'comb', 'on', 'diagonal')

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

        segments('inner',(41,30),(35,22),(27,28),(19,34),(15,37))
        self.add_arc('handle',(15,37),(9,29),radius_x=5)
        self.add_line('outer',(9,29),(33,11))
        self.add_arc('crown',(33,11),(40,12),radius_x=5)
        self.add_contour('comb','inner-1','inner-2','inner-3','inner-4','handle','outer','crown')
        for j in range(2):
         x,y=19+8*j,34-6*j
         self.add_line(f'tooth-{j}',(x,y),(x+6,y+8))
         self.relate('connect',f'tooth-{j}','comb')
