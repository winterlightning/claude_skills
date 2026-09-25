from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8e2b5875-0c52-5e83-a90d-b42371b3df31'
SOURCE_PATH = 'icon_set/work/todo-references/notes checklist flip_8e2b5875-0c52-5e83-a90d-b42371b3df31.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    """A flip notepad with a checklist.

    Plan: Top header strip, a check and two rows of writing.
    Construction reference: notepad-text: aligned writing rows and top binding.
    """
    icon_id = 'notes-checklist-flip'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "content"
    aliases = ()
    keywords = ('notes', 'checklist', 'flip')

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

        self.add_polyline('page',(8,12),(8,4),(40,4),(40,12),(40,44),(8,44),(8,12))
        self.add_line('header',(8,12),(40,12)); self.relate('connect','header','page')
        self.add_polyline('check',(16,24),(20,28),(24,22))
        self.add_line('row-right',(32,24),(32,24))
        self.add_line('row-bottom',(16,36),(32,36))
