from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1488ab61-9200-53bd-99b7-47e825038f3b'
SOURCE_PATH = 'icon_set/work/todo-references/notepad_1488ab61-9200-53bd-99b7-47e825038f3b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    """A blank top-bound notepad.

    Plan: Three identical binding strokes at an 8-unit pitch; top frame split at attachment nodes.
    Construction reference: notepad-text: repeated binding rhythm and a single page silhouette.
    """
    icon_id = 'notepad'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases = ()
    keywords = ('notepad',)

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

        self.add_polyline('page',(16,14),(6,14),(6,42),(42,42),(42,14),(32,14),(24,14),(16,14))
        for x in (16,24,32):
            self.add_line(f'binding-{x}',(x,6),(x,14))
            self.relate('connect',f'binding-{x}','page')
