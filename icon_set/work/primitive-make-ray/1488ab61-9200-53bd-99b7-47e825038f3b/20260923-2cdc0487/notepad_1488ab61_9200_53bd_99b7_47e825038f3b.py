from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1488ab61-9200-53bd-99b7-47e825038f3b'
SOURCE_PATH = 'icon_set/work/todo-references/notepad_1488ab61-9200-53bd-99b7-47e825038f3b.svg'
AUTHOR = 'gpt-6'
# Construction plan: Square note block with three equally spaced top binding strokes.
# Keyshape visible extremes are supplied by Keyshape.SQUARE.bounds_for(SOLO48).
# Lucide construction reference: notebook-pen.
class Drawing(Solo48):
    icon_id = 'notepad'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('notepad',)
    def build(self):
        self.add_polyline('page',(6,18),(6,42),(42,42),(42,18),(42,14),(6,14),(6,18))
        for i,x in enumerate((14,24,34)):
            self.add_line(f'ring-{i}',(x,6),(x,22))
            self.relate('connect','page',f'ring-{i}')

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
# Visual review: Three binding stems are evenly spaced; blank note area remains open in both themes.
