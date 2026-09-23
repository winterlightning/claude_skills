from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b4787f31-7286-435f-a9e4-6114f60b64e5'
SOURCE_PATH = 'icon_set/work/todo-references/object exclude_b4787f31-7286-435f-a9e4-6114f60b64e5.svg'
AUTHOR = 'gpt-6'
# Construction plan: Circular exclude symbol split at four diagonal attachment nodes, with crossing diagonals sharing the center.
# Keyshape visible extremes are supplied by Keyshape.CIRCLE.bounds_for(SOLO48).
# Lucide construction reference: No useful subject match; shared human reference for portraits.
class Drawing(Solo48):
    icon_id = 'object-exclude'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('object', 'exclude')
    def build(self):
        points=[(12,8),(40,12),(36,40),(8,36)]
        for i in range(4):
            self.add_arc(f'rim-{i}',points[i],points[(i+1)%4],radius_x=20)
            self.add_line(f'spoke-{i}',points[i],(24,24))
            self.relate('connect',f'rim-{i}',f'spoke-{i}')
            self.relate('connect',f'rim-{(i-1)%4}',f'spoke-{i}')
        self.add_contour('rim',*[f'rim-{i}' for i in range(4)],closed=True)
        self.relate('connect',*[f'spoke-{i}' for i in range(4)])

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
# Visual review: Circular outline and crossing strokes are clear in both themes. Diagonals use integer 12/16 radial offsets and are perpendicular; slight rotation retained for exact circular attachment.
