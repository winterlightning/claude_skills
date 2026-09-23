"""A folded map accompanies a connected four-node learning diagram.
Plan: Map folds remain at upper left; one large node connects to a triangular group.
Keyshape: HRECT_L; extrema follow the profile contract.
References: supplied reference SVG; No useful local Lucide subject match used; shared geometric construction principles applied.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ef84068a-8813-43c3-b7d5-546375fbf309'
SOURCE_PATH = 'icon_set/work/todo-references/start your machine learning journey_ef84068a-8813-43c3-b7d5-546375fbf309.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'start-your-machine-learning-journey'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('start', 'your', 'machine', 'learning', 'journey')

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

        self.add_polyline('map',(4,26),(4,8),(13,12),(22,8),(22,20))
        self.add_line('map-fold',(13,12),(13,23));self.relate('connect','map','map-fold')
        self.circle('root',23,29,6)
        nodes=[('top',37,16,4),('right',41,28,3),('bottom',37,37,3)]
        for name,x,y,r in nodes: self.circle(name,x,y,r)
        self.add_line('upper-link',(27,25),(34,19))
        self.add_line('middle-link',(29,29),(38,28))
        self.add_line('lower-link',(27,33),(34,36))
        self.add_polyline('node-chain',(39,20),(42,25),(40,31),(38,34))
