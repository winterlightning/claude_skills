from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '7d27b436-d05f-41d3-b72f-2e31759f48e2'
SOURCE_PATH = 'icon_set/work/todo-references/onam 1_7d27b436-d05f-41d3-b72f-2e31759f48e2.svg'
AUTHOR = 'gpt-6'
# Construction plan: Circular Onam flower with six radial petals around a small center; mirrored diagonal petals share definitions.
# Keyshape visible extremes are supplied by Keyshape.CIRCLE.bounds_for(SOLO48).
# Lucide construction reference: flower.
class Drawing(Solo48):
    icon_id = 'onam-1'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('onam', '1')
    def build(self):
        self.oval('rim',24,24,20)
        self.oval('center',24,24,4)
        self.add_bezier('petal-top',(24,20),((16,17),(20,10),(24,7)),((28,10),(32,17),(24,20)))
        self.add_bezier('petal-bottom',(24,28),((16,31),(20,38),(24,41)),((28,38),(32,31),(24,28)))
        for side in (-1,1):
            for vertical in (-1,1):
                def p(x,y):return (24+side*x,24+vertical*y)
                self.add_bezier(f'petal-{side}-{vertical}',p(4,2),(p(7,10),p(14,11),p(17,8)),(p(16,2),p(10,0),p(4,2)))

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


# Visible keyshape extremes: (2, 2, 46, 46).
# Visual review: Six petals and outer circle are retained, but their clearances close into a heavy flower at native size. Requires revision; not a pass.
