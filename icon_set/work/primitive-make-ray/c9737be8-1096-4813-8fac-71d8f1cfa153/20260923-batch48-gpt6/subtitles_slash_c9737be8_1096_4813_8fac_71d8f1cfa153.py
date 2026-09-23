"""A rounded speech bubble contains a rising slash.
Plan: Rounded rectangular speech body with a deliberate pointed lower-right tail.
Keyshape: SQUARE; extrema follow the profile contract.
References: supplied reference SVG; lucide/original/message-square.svg and atomic-debug/message-square.svg: rounded frame and integrated tail
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'c9737be8-1096-4813-8fac-71d8f1cfa153'
SOURCE_PATH = 'icon_set/work/todo-references/subtitles slash_c9737be8-1096-4813-8fac-71d8f1cfa153.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'subtitles-slash'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('subtitles', 'slash')

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

        self.add_line('top',(12,6),(36,6))
        self.add_arc('tr',(36,6),(42,12),radius_x=6)
        self.add_line('right',(42,12),(42,28))
        self.add_arc('br',(42,28),(36,34),radius_x=6)
        self.add_polyline('tail',(36,34),(36,42),(28,34),(12,34))
        self.add_arc('bl',(12,34),(6,28),radius_x=6)
        self.add_line('left',(6,28),(6,12))
        self.add_arc('tl',(6,12),(12,6),radius_x=6)
        self.add_contour('bubble','top','tr','right','br','tail-1','tail-2','tail-3','bl','left','tl',closed=True)
        self.add_line('slash',(17,25),(31,15))
