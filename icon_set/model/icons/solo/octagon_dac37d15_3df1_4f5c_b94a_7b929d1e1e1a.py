from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dac37d15-3df1-4f5c-b94a-7b929d1e1e1a'
SOURCE_PATH = 'icon_set/work/todo-references/octagon_dac37d15-3df1-4f5c-b94a-7b929d1e1e1a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    """An eight-sided polygon.

    Plan: Four mirrored corner cuts with equal horizontal and vertical spans.
    Construction reference: octagon: symmetric corner cuts and one closed contour.
    """
    icon_id = 'octagon-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "container"
    categories = ("container",)
    aliases = ()
    keywords = ('octagon',)

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

        low,high,cut=6,42,11
        self.add_polyline('octagon',(low+cut,low),(high-cut,low),(high,low+cut),(high,high-cut),(high-cut,high),(low+cut,high),(low,high-cut),(low,low+cut),closed=True)
