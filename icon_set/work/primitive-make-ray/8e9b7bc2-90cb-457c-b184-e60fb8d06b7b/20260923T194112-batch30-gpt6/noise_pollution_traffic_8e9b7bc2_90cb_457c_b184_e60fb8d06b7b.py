from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8e9b7bc2-90cb-457c-b184-e60fb8d06b7b'
SOURCE_PATH = 'icon_set/work/todo-references/noise pollution traffic_8e9b7bc2-90cb-457c-b184-e60fb8d06b7b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    """Two cars beneath a lightning bolt and noise marks.

    Plan: A repeated pair of compact car silhouettes; an asymmetric lightning zigzag centered above.
    Construction reference: car-front: repeated car body and paired wheel placement.
    """
    icon_id = 'noise-pollution-traffic'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('noise', 'pollution', 'traffic')

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

        for i,x in enumerate((4,28)):
            self.add_polyline(f'car-{i}',(x,36),(x,32),(x+4,28),(x+12,28),(x+16,32),(x+16,36),(x+13,36),(x+13,40),(x+10,40),(x+10,36),(x+6,36),(x+6,40),(x+3,40),(x+3,36),closed=True)
        self.add_polyline('lightning',(26,8),(18,18),(25,18),(22,24),(32,14),(25,14),closed=True)
        self.add_polyline('noise-left',(4,17),(8,21),(12,17))
        self.add_polyline('noise-right',(40,10),(36,14),(40,18))
