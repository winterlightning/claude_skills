from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'dac37d15-3df1-4f5c-b94a-7b929d1e1e1a'
SOURCE_PATH = 'icon_set/work/todo-references/octagon_dac37d15-3df1-4f5c-b94a-7b929d1e1e1a.svg'
AUTHOR = 'gpt-6'
# Construction plan: Regular-looking octagon with equal paired diagonal cuts about both axes.
# Keyshape visible extremes are supplied by Keyshape.SQUARE.bounds_for(SOLO48).
# Lucide construction reference: octagon.
class Drawing(Solo48):
    icon_id = 'octagon'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('octagon',)
    def build(self):
        x0,x1=6,42;cut=11
        self.add_polyline('octagon',(x0+cut,x0),(x1-cut,x0),(x1,x0+cut),(x1,x1-cut),(x1-cut,x1),(x0+cut,x1),(x0,x1-cut),(x0,x0+cut),closed=True)

    def oval(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-top', (cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def box(self, name, x, y, right, bottom, r=3):
        points=[(x+r,y),(right-r,y),(right,y+r),(right,bottom-r),(right-r,bottom),(x+r,bottom),(x,bottom-r),(x,y+r),(x+r,y)]
        members=[]
        for i,(a,b) in enumerate(zip(points,points[1:])):
            part=f'{name}-{i}'
            if i%2: self.add_arc(part,a,b,radius_x=r)
            else: self.add_line(part,a,b)
            members.append(part)
        self.add_contour(name,*members,closed=True)

    def cross(self,name,cx,cy,r):
        for suffix,p in [('left',(cx-r,cy)),('right',(cx+r,cy)),('top',(cx,cy-r)),('bottom',(cx,cy+r))]:
            self.add_line(name+'-'+suffix,p,(cx,cy))
        self.relate('connect',*[name+'-'+s for s in ('left','right','top','bottom')])

    def clipboard(self):
        self.box('clip',17,4,31,12,4)
        self.add_polyline('board',(17,8),(8,8),(8,44),(40,44),(40,8),(31,8))
        self.relate('connect','clip','board')


# Visible keyshape extremes: (4, 4, 44, 44).
# Visual review: Octagon has balanced paired sides and consistent corner cuts; clear at native size in both themes.
