from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '57237fb8-d140-4fc2-97bb-fe24ab1c7285'
SOURCE_PATH = 'icon_set/work/todo-references/office desk 1_57237fb8-d140-4fc2-97bb-fe24ab1c7285.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    """An office desk with a monitor, clock, and cup.

    Plan: Desk spans the keyshape; monitor left and clock right deliberately balance different shapes.
    Construction reference: laptop: simple screen enclosure and supporting base.
    """
    icon_id = 'office-desk-1'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('office', 'desk', '1')

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

        self.add_polyline('desk',(4,32),(44,32),(42,40))
        self.add_line('leg-left',(6,32),(4,40)); self.relate('connect','leg-left','desk')
        self.rounded('monitor',4,8,26,24,3)
        self.add_line('stand',(15,24),(15,32)); self.relate('connect','stand','monitor'); self.relate('connect','stand','desk')
        self.circle('clock',38,14,6)
        self.add_polyline('hands',(38,10),(38,14),(41,14))
        self.add_polyline('cup',(34,32),(34,26),(40,26),(40,32)); self.relate('connect','cup','desk')
