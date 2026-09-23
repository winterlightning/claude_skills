from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cfa8128f-ae7e-5ff0-a3c1-3f2f6f104b53'
SOURCE_PATH = 'icon_set/work/todo-references/notes paper_cfa8128f-ae7e-5ff0-a3c1-3f2f6f104b53.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    """A written note with its lower right corner turned up.

    Plan: Lower fold and page share endpoints; writing aligned above it.
    Construction reference: sticky-note: fold construction, deliberately moved to the input’s lower-right corner.
    """
    icon_id = 'notes-paper'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('notes', 'paper')

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

        self.add_polyline('page',(28,44),(8,44),(8,4),(40,4),(40,32),(28,44))
        self.add_polyline('fold',(28,44),(28,32),(40,32)); self.relate('connect','fold','page')
        for i,y in enumerate((14,23)): self.add_line(f'text-{i}',(17,y),(31 if i==0 else 27,y))
