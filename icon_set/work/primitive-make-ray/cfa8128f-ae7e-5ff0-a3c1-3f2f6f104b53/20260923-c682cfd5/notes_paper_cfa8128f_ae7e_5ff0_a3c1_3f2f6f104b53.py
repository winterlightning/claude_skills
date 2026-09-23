from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'cfa8128f-ae7e-5ff0-a3c1-3f2f6f104b53'
SOURCE_PATH = 'icon_set/work/todo-references/notes paper_cfa8128f-ae7e-5ff0-a3c1-3f2f6f104b53.svg'
AUTHOR = 'gpt-6'
# Construction plan: Text page with lower-right dog-ear; two text lines above the fold.
# Keyshape visible extremes are supplied by Keyshape.VRECT_L.bounds_for(SOLO48).
# Lucide construction reference: file-text.
class Drawing(Solo48):
    icon_id = 'notes-paper'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('notes', 'paper')
    def build(self):
        self.add_polyline('page',(8,4),(40,4),(40,32),(28,44),(8,44),closed=True)
        self.add_polyline('fold',(28,44),(28,32),(40,32))
        self.relate('connect','page','fold')
        for i,(y,end) in enumerate(((14,31),(23,26))):self.add_line(f'text-{i}',(17,y),(end,y))

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
# Visual review: Lower folded corner remains clear with two writing rules. Intentional lower-right asymmetry.
