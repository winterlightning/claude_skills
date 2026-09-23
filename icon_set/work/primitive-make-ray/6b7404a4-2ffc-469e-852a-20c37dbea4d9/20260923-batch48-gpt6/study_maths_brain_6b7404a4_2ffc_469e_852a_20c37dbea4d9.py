"""A head in profile contains plus, minus and multiplication signs.
Plan: Smooth cranial silhouette, stepped facial profile, three mathematical operators.
Keyshape: SQUARE; extrema follow the profile contract.
References: supplied reference SVG; No useful local Lucide subject match used; shared geometric construction principles applied.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6b7404a4-2ffc-469e-852a-20c37dbea4d9'
SOURCE_PATH = 'icon_set/work/todo-references/study maths brain_6b7404a4-2ffc-469e-852a-20c37dbea4d9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'study-maths-brain'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('study', 'maths', 'brain')

    def circle(self, name, x, y, r):
        self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
        self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def rect(self, name, x, y, w, h, r=4):
        # One owning rectangle; four equal tangent corner arcs.
        points = [(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),
                  (x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        members=[]
        for i,p in enumerate(points):
            q=points[(i+1)%8]; n=f'{name}-{i}'
            if i%2: self.add_arc(n,p,q,radius_x=r)
            else: self.add_line(n,p,q)
            members.append(n)
        self.add_contour(name,*members,closed=True)

    def cross(self, name, x, y, r, diagonal=False):
        # Four rays share the true intersection node.
        offsets=[(-r,-r),(r,r),(-r,r),(r,-r)] if diagonal else [(-r,0),(r,0),(0,-r),(0,r)]
        ids=[]
        for i,(dx,dy) in enumerate(offsets):
            n=f'{name}-{i}';self.add_line(n,(x,y),(x+dx,y+dy));ids.append(n)
        for i,a in enumerate(ids):
            for b in ids[i+1:]: self.relate('connect',a,b)

    def build(self):

        self.add_bezier('cranium',(10,20),((10,10),(19,6),(27,6)),((36,6),(42,13),(42,22)),((42,28),(36,30),(36,36)))
        self.add_polyline('neck',(36,36),(36,42))
        self.add_polyline('face',(10,20),(6,29),(10,30),(10,34),(18,34),(18,42))
        self.add_contour('profile','face-6','face-5') if False else None
        self.relate('connect','cranium','face');self.relate('connect','cranium','neck')
        self.cross('plus',23,16,3)
        self.add_line('minus',(18,27),(23,27))
        self.cross('times',32,27,3,True)
