"""A hand squeezes a phone between inward arrows.
Plan: Phone owns its frame; a repeated three-finger grip and paired arrows flank it.
Keyshape: SQUARE; extrema follow the profile contract.
References: supplied reference SVG; lucide/original/square-x.svg and atomic-debug/square-x.svg: equal corner radii and centered marks
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8d871e7d-03c3-4f02-90aa-ec0ac69a56b5'
SOURCE_PATH = 'icon_set/work/todo-references/squeeze sides_8d871e7d-03c3-4f02-90aa-ec0ac69a56b5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'squeeze-sides'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('squeeze', 'sides')

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

        self.rect('phone',14,6,20,36,4)
        for i in range(3):
            self.rect(f'finger-{i}',6,18+i*8,16,8,4)
        self.add_polyline('left-arrow',(6,8),(10,12),(6,16))
        self.add_polyline('right-arrow',(42,8),(38,12),(42,16))
        self.add_polyline('thumb',(34,20),(40,20),(40,30),(42,32))
        self.add_line('wrist',(34,38),(42,42))
