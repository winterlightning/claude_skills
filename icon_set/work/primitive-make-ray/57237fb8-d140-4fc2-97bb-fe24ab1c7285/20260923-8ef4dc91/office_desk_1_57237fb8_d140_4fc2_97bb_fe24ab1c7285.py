from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '57237fb8-d140-4fc2-97bb-fe24ab1c7285'
SOURCE_PATH = 'icon_set/work/todo-references/office desk 1_57237fb8-d140-4fc2-97bb-fe24ab1c7285.svg'
AUTHOR = 'gpt-6'
# Construction plan: Office workstation: monitor left, clock right, desk across bottom and two legs.
# Keyshape visible extremes are supplied by Keyshape.SQUARE.bounds_for(SOLO48).
# Lucide construction reference: laptop.
class Drawing(Solo48):
    icon_id = 'office-desk-1'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('office', 'desk', '1')
    def build(self):
        self.box('monitor',6,8,26,24,2)
        self.add_line('stand',(16,24),(16,32));self.relate('connect','monitor','stand')
        self.oval('clock',36,12,6)
        self.add_polyline('hands',(36,8),(36,12),(39,12))
        self.add_polyline('desk',(6,32),(42,32),(40,36),(8,36),closed=True)
        self.relate('connect','stand','desk')
        for i,(x,end) in enumerate(((10,6),(38,42))):
            self.add_line(f'leg-{i}',(x,36),(end,42));self.relate('connect','desk',f'leg-{i}')
        self.add_line('cup',(36,24),(36,32));self.relate('connect','cup','desk')

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
# Visual review: Monitor, clock and desk are recognizable, but the desk thickness collapses and the clock crowds the monitor and hands; requires revision.
