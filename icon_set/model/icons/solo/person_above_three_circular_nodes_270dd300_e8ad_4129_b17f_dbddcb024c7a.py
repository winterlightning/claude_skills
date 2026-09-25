"""A separate circular head sits above a domed bust connected to a branching line. Three circular nodes hang below it, evenly spaced along the lower horizontal connector.
Symbol plan: Person above a three-node hierarchy. Head radius 4 at (24,8), neck (24,20), exact 4 ink gap. Broad quarter-ellipse shoulders frame the vertical torso. Three compact circular nodes share radius 2 and 14-unit pitch; omit the bust baseline.
Keyshape: VRECT_L; centerline extremes (8,4)-(40,44).
Construction reference: network; human_ref/user.svg; human_ref/full_body_ref.png. Lucide original and atomic-debug renders inspected where named.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '270dd300-e8ad-4129-b17f-dbddcb024c7a'
SOURCE_PATH = 'pictographic-primitives/companies/human resources hierarchy_270dd300-e8ad-4129-b17f-dbddcb024c7a.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'person-above-three-circular-nodes'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'companies'
    categories = ('primitives', 'companies')
    aliases = ()
    keywords = ('person', 'above', 'three', 'circular', 'nodes')

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

        circle('head',24,8,4)
        self.add_line('torso',(24,20),(24,32))
        self.add_arc('shoulder-left',(16,24),(24,20),radius_x=8,radius_y=4)
        self.add_arc('shoulder-right',(24,20),(32,24),radius_x=8,radius_y=4)
        self.add_contour('shoulders','shoulder-left','shoulder-right');self.relate('connect','torso','shoulders')
        self.add_polyline('branches',(10,40),(10,32),(24,32),(38,32),(38,40));self.relate('connect','torso','branches')
        self.add_line('middle-link',(24,32),(24,40));self.relate('connect','middle-link','branches');self.relate('connect','middle-link','torso')
        for j,x in enumerate((10,24,38)):
         self.add_arc(f'node-{j}-right',(x,40),(x,44),radius_x=2)
         self.add_arc(f'node-{j}-left',(x,44),(x,40),radius_x=2)
         self.add_contour(f'node-{j}',f'node-{j}-right',f'node-{j}-left',closed=True)
         self.relate('connect',f'node-{j}','middle-link' if j==1 else 'branches')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
