from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'd6e3d9b9-b561-4ac3-8008-110d0dfc61d6'
SOURCE_PATH = 'icon_set/work/todo-references/note dollar sign_d6e3d9b9-b561-4ac3-8008-110d0dfc61d6.svg'
AUTHOR = 'gpt-6'
# Construction plan: Upright clipboard with centered capsule clip and open board wall behind it.
# Keyshape visible extremes are supplied by Keyshape.VRECT_L.bounds_for(SOLO48).
# Lucide construction reference: clipboard.
class Drawing(Solo48):
    icon_id = 'note-dollar-sign'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('note', 'dollar', 'sign')
    def build(self):
        self.clipboard()
        self.add_bezier('dollar', (29,22), ((19,16),(17,27),(24,28)), ((33,29),(29,38),(19,34)))
        self.add_line('dollar-stem-top',(24,17),(24,20))
        self.add_line('dollar-stem-bottom',(24,36),(24,39))
        # Dollar stems remain detached; no contact waiver.

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
# Visual review: Dollar and board are recognizable, but the stem crowds the clip and lower edge; MIC blocks this candidate.
