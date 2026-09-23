from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8e2b5875-0c52-5e83-a90d-b42371b3df31'
SOURCE_PATH = 'icon_set/work/todo-references/notes checklist flip_8e2b5875-0c52-5e83-a90d-b42371b3df31.svg'
AUTHOR = 'gpt-6'
# Construction plan: Flip checklist: page frame, top separator, check and short writing runs.
# Keyshape visible extremes are supplied by Keyshape.VRECT_L.bounds_for(SOLO48).
# Lucide construction reference: file-text.
class Drawing(Solo48):
    icon_id = 'notes-checklist-flip'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('notes', 'checklist', 'flip')
    def build(self):
        self.box('page',8,4,40,44,4)
        self.add_line('flip-rule',(8,14),(40,14))
        self.relate('connect','page','flip-rule')
        self.add_polyline('check',(17,24),(20,27),(23,22))
        self.add_dot('entry',(31,25))
        for i,(a,b) in enumerate(((17,23),(31,31))):self.add_line(f'row-{i}',(a,35),(b,35))

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


# Visible keyshape extremes: (6, 2, 42, 46).
# Visual review: Flip header and check remain clear; short entries reduce to dots at native size. Accepted as simplified checklist.
