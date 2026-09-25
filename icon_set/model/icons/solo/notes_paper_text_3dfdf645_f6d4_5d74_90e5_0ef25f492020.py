from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3dfdf645-f6d4-5d74-90e5-0ef25f492020'
SOURCE_PATH = 'icon_set/work/todo-references/notes paper text_3dfdf645-f6d4-5d74-90e5-0ef25f492020.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    """A written page with its upper right corner folded.

    Plan: Fold shares two boundary nodes; evenly spaced writing rules below the fold.
    Construction reference: sticky-note: attached corner fold and uninterrupted page outline.
    """
    icon_id = 'notes-paper-text'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "content"
    aliases = ()
    keywords = ('notes', 'paper', 'text')

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

        self.add_polyline('page',(28,4),(8,4),(8,44),(40,44),(40,16),(28,4))
        self.add_polyline('fold',(28,4),(28,16),(40,16)); self.relate('connect','fold','page')
        for i,y in enumerate((25,34)): self.add_line(f'text-{i}',(17,y),(31 if i==0 else 27,y))
