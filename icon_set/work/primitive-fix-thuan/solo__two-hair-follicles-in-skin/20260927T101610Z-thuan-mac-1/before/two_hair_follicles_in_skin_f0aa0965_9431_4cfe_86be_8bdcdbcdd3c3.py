"""Two tall pointed hairs rise from rounded U-shaped follicles in a horizontal skin surface. Each hair has one curved side and one straighter side, tapering to an upright tip.
Symbol plan: Two matching pointed hairs with rounded roots above one continuous skin pocket. Repeat the hair definition at an 18-unit pitch; consolidate the tiny separate pockets into one broad skin curve.
Keyshape: HRECT_L; centerline extremes (4,8)-(44,40).
Construction reference: droplet; local original and atomic geometry inspected for Lucide.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f0aa0965-9431-4cfe-86be-8bdcdbcdd3c3'
SOURCE_PATH = 'pictographic-primitives/beauty/hair skin 1_f0aa0965-9431-4cfe-86be-8bdcdbcdd3c3.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'two-hair-follicles-in-skin'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'beauty'
    categories = ('primitives', 'beauty')
    aliases = ()
    keywords = ('two', 'hair', 'follicles', 'in', 'skin')

    def build(self):

        def segments(name,*points):
            for j,(a,b) in enumerate(zip(points,points[1:]),1):
                self.add_line(f'{name}-{j}',a,b)

        def circle(name,cx,cy,r):
            self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)

        def rect(name,l,t,r,b,q=0):
            if not q:
                self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),closed=True)
                return
            points=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q),(l+q,t)]
            ids=[]
            for j,(a,z) in enumerate(zip(points,points[1:])):
                if a==z:continue
                n=f'{name}-{j}'
                if j%2:self.add_arc(n,a,z,radius_x=q)
                else:self.add_line(n,a,z)
                ids.append(n)
            self.add_contour(name,*ids,closed=True)

        for j,x in enumerate((15,33)):
         self.add_arc(f'hair-{j}-side',(x+4,8),(x-4,24),radius_x=8,radius_y=16,sweep=False)
         self.add_arc(f'hair-{j}-root',(x-4,24),(x+4,24),radius_x=4,sweep=False)
         self.add_line(f'hair-{j}-straight',(x+4,24),(x+4,8))
         self.add_contour(f'hair-{j}',f'hair-{j}-side',f'hair-{j}-root',f'hair-{j}-straight',closed=True)
        self.add_arc('skin',(4,30),(44,30),radius_x=20,radius_y=10,sweep=False)
