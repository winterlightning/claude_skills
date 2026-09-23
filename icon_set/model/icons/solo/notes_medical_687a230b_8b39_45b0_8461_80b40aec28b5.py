from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '687a230b-8b39-45b0-8461-80b40aec28b5'
SOURCE_PATH = 'icon_set/work/todo-references/notes medical_687a230b-8b39-45b0-8461-80b40aec28b5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    """A medical cross inside a rounded square.

    Plan: Symmetric outlined cross, owned by one shared center and arm thickness.
    Construction reference: notebook: consistent rounded enclosure; outlined medical cross from supplied reference.
    """
    icon_id = 'notes-medical'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('notes', 'medical')

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

        self.rounded('frame',6,6,42,42)
        c=24; lo=c-9; hi=c+9; a=c-4; b=c+4
        self.add_polyline('medical-cross',(a,lo),(b,lo),(b,a),(hi,a),(hi,b),(b,b),(b,hi),(a,hi),(a,b),(lo,b),(lo,a),(a,a),closed=True)
