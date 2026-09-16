"""A small rounded square connects downward to a horizontal branching line. Three matching rounded square nodes hang beneath the branch, each joined by a short vertical connector.
Symbol plan: One square parent and three equal square children at 16-unit pitch. A shared trunk and orthogonal branch link exact midpoint nodes; rounded stroke joins replace extra corner arcs.
Keyshape: HRECT_L; centerline extremes (4,8)-(44,40).
Construction reference: network; local original and atomic geometry inspected for Lucide.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '76675686-fe91-5003-8627-497d2cd08d61'
SOURCE_PATH = 'pictographic-primitives/business/hierarchy 5 organize_76675686-fe91-5003-8627-497d2cd08d61.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'organization-chart-with-three-children'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    aliases = ()
    keywords = ('organization', 'chart', 'with', 'three', 'children')

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

        self.add_polyline('parent',(20,8),(28,8),(28,16),(24,16),(20,16),closed=True)
        for j,x in enumerate((8,24,40)):
         self.add_polyline(f'child-{j}',(x-4,32),(x,32),(x+4,32),(x+4,40),(x-4,40),closed=True)
        self.add_polyline('trunk',(24,16),(24,24),(24,32))
        self.add_polyline('branches',(8,32),(8,24),(24,24),(40,24),(40,32))
        self.relate('connect','trunk','parent');self.relate('connect','trunk','child-1');self.relate('connect','trunk','branches')
        for n in ('child-0','child-2'):self.relate('connect','branches',n)
