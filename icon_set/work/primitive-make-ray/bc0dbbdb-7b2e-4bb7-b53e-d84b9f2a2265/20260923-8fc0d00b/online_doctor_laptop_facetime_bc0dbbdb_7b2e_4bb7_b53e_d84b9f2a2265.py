from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'bc0dbbdb-7b2e-4bb7-b53e-d84b9f2a2265'
SOURCE_PATH = 'icon_set/work/todo-references/online doctor laptop facetime_bc0dbbdb-7b2e-4bb7-b53e-d84b9f2a2265.svg'
AUTHOR = 'gpt-6'
# Construction plan: Remote doctor bust above a laptop at lower left, with medical cross at right. Detached head/body gap is 8 centerline units, 4 visible units.
# Keyshape visible extremes are supplied by Keyshape.SQUARE.bounds_for(SOLO48).
# Lucide construction reference: laptop.
class Drawing(Solo48):
    icon_id = 'online-doctor-laptop-facetime'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('online', 'doctor', 'laptop', 'facetime')
    def build(self):
        self.oval('head',30,12,6)
        self.add_arc('shoulders',(18,38),(30,26),radius_x=12)
        self.add_arc('shoulders-right',(30,26),(42,38),radius_x=12)
        self.add_contour('body','shoulders','shoulders-right')
        self.add_polyline('laptop',(6,42),(8,34),(8,26),(16,26))
        self.add_line('base',(6,42),(28,42));self.relate('connect','laptop','base')
        self.cross('medical',34,34,4)

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
# Visual review: Doctor head and shoulders read, but the medical cross merges into the shoulder and laptop crowds the body. Head bottom y=18 and shoulder top y=26 establish exactly 8 centerline / 4 ink units. Shared human_ref/user.svg informed proportions; other MIC failures remain.
