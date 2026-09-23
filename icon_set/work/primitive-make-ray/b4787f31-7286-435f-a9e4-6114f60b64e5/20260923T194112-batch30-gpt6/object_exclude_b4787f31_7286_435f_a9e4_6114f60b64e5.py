from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b4787f31-7286-435f-a9e4-6114f60b64e5'
SOURCE_PATH = 'icon_set/work/todo-references/object exclude_b4787f31-7286-435f-a9e4-6114f60b64e5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    """A circle crossed by diagonal exclusion lines.

    Plan: Four circle arcs with shared diagonal endpoints; two diagonals split at their intersection.
    Construction reference: combine: simple Boolean geometry; circular exclusion topology from input.
    """
    icon_id = 'object-exclude'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('object', 'exclude')

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

        pts=[(12,8),(36,8),(36,40),(12,40)]
        for i in range(4): self.add_arc(f'rim-{i}',pts[i],pts[(i+1)%4],radius_x=20)
        self.add_contour('rim',*(f'rim-{i}' for i in range(4)),closed=True)
        for i,p in enumerate(pts):
            self.add_line(f'spoke-{i}',p,(24,24)); self.relate('connect',f'spoke-{i}','rim')
        self.relate('connect',*(f'spoke-{i}' for i in range(4)))
