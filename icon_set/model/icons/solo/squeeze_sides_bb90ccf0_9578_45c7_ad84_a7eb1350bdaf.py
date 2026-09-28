"""Phone with inward-curving squeeze marks.
Plan: Wider phone accommodates the marks. Mirrored curves share radius and placement; phone has equal corner radii.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bb90ccf0-9578-45c7-ad84-a7eb1350bdaf'
SOURCE_PATH = 'pictographic-primitives/mobile/squeeze sides_bb90ccf0-9578-45c7-ad84-a7eb1350bdaf.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'squeeze-sides-bb90ccf0'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'mobile'
    categories = ('mobile', 'primitives')
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

        self.rect('phone',8,4,32,40,4)
        self.add_arc('left-squeeze',(17,14),(17,26),radius_x=10,sweep=True)
        self.add_arc('right-squeeze',(31,14),(31,26),radius_x=10,sweep=False)
        self.add_line('home-bar',(17,35),(31,35))

PLAN = 'Phone with inward-curving squeeze marks. Wider phone accommodates the marks.'
OMISSIONS = 'One curve per side; bottom separator reduced to a home bar.'
CONSTRUCTION_REFERENCES = ['icon_set/references/lucide/original/tablet.svg', 'icon_set/references/lucide/atomic-debug/tablet.svg']
PARENT_SOURCE = 'icon_set/model/icons/solo/squeeze_sides_bb90ccf0_9578_45c7_ad84_a7eb1350bdaf.py'
