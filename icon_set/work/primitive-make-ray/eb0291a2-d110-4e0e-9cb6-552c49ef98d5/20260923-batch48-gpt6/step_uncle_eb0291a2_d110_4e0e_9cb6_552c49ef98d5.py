"""A plain-headed man with a circular relationship badge.
Plan: Circular head, smooth shoulders and lower-right badge.
Keyshape: SQUARE; extrema follow the profile contract.
References: supplied reference SVG; human_ref/user.svg and human_ref/full_body_ref.png: circular heads and smooth shoulders or limbs
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'eb0291a2-d110-4e0e-9cb6-552c49ef98d5'
SOURCE_PATH = 'icon_set/work/todo-references/step uncle_eb0291a2-d110-4e0e-9cb6-552c49ef98d5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'step-uncle'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('step', 'uncle')
    human_construction = 'bust'

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

        # human_ref/user.svg: circular head and broad smooth shoulders.
        # Head lower centerline y=26, shoulder apex y=30: touching ink.
        self.circle('head',22,16,10)
        self.add_arc('shoulder-left',(6,42),(22,30),radius_x=16,radius_y=12)
        self.add_bezier('shoulder-right',(22,30),((27,30),(30,31),(32,34)))
        self.add_line('base',(6,42),(26,42))
        self.add_contour('body','shoulder-left','shoulder-right')
        self.relate('connect','head','body')
        self.relate('connect','base','body')
        self.circle('badge',36,36,6)
