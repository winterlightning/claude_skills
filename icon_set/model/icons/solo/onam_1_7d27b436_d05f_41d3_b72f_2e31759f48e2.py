from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7d27b436-d05f-41d3-b72f-2e31759f48e2'
SOURCE_PATH = 'icon_set/work/todo-references/onam 1_7d27b436-d05f-41d3-b72f-2e31759f48e2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    """A six-petal Onam flower inside a circular rim.

    Plan: Six petals built as mirrored arc pairs around a central hexagon; circular frame.
    Construction reference: No useful Lucide match; mirrored arc-pair petal construction follows the supplied flower.
    """
    icon_id = 'onam-1'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('onam', '1')

    def circle(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-a', (cx-rx,cy), (cx+rx,cy), radius_x=rx, radius_y=ry)
        self.add_arc(name+'-b', (cx+rx,cy), (cx-rx,cy), radius_x=rx, radius_y=ry)
        self.add_contour(name, name+'-a', name+'-b', closed=True)

    def rounded(self, name, left, top, right, bottom, radius=4):
        r=radius
        pts=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),
             (right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
        names=[]
        for i,a in enumerate(pts):
            b=pts[(i+1)%8]; n=f'{name}-{i}'; names.append(n)
            if i%2: self.add_arc(n,a,b,radius_x=r)
            else: self.add_line(n,a,b)
        self.add_contour(name,*names,closed=True)

    def clipboard(self):
        # Clip and board share the two nodes (16,12), (32,12).
        self.add_polyline('board', (16,12),(8,12),(8,44),(40,44),(40,12),(32,12))
        self.rounded('clip',16,4,32,12,4)
        self.relate('connect','board','clip')

    def cross(self, name, cx, cy, radius):
        for suffix,end in [('l',(cx-radius,cy)),('r',(cx+radius,cy)),('t',(cx,cy-radius)),('b',(cx,cy+radius))]:
            self.add_line(name+'-'+suffix,(cx,cy),end)
        self.relate('connect',*(name+'-'+s for s in ['l','r','t','b']))

    def build(self):

        self.circle('rim',24,24,20)
        core=[(20,18),(28,18),(32,24),(28,30),(20,30),(16,24)]
        self.add_polyline('center',*core,closed=True)
        petals=[((20,18),(24,7),(28,18)),((28,18),(39,13),(32,24)),((32,24),(39,35),(28,30)),((28,30),(24,41),(20,30)),((20,30),(9,35),(16,24)),((16,24),(9,13),(20,18))]
        for i,(a,tip,b) in enumerate(petals):
            self.add_arc(f'petal-{i}-a',a,tip,radius_x=12)
            self.add_arc(f'petal-{i}-b',tip,b,radius_x=12)
            self.add_contour(f'petal-{i}',f'petal-{i}-a',f'petal-{i}-b')
            self.relate('connect',f'petal-{i}','center')
