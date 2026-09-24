from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

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
        # Rebalance screen/clock; remove the cup that cannot fit below the clock.
        self.add_polyline('desk',(4,36),(44,36),(42,40))
        self.add_line('leg-left',(6,36),(4,40))
        self.relate('connect','leg-left','desk')
        self.rounded('monitor',4,8,15,27,2)
        self.add_line('stand',(10,27),(10,36))
        self.relate('connect','stand','monitor')
        self.relate('connect','stand','desk')
        self.add_arc('clock-ne',(34,8),(44,18),radius_x=10)
        self.add_arc('clock-se',(44,18),(34,28),radius_x=10)
        self.add_arc('clock-sw',(34,28),(24,18),radius_x=10)
        self.add_arc('clock-nw',(24,18),(34,8),radius_x=10)
        self.add_contour('clock','clock-ne','clock-se','clock-sw','clock-nw',closed=True)
        self.add_polyline('hands',(34,8),(34,18),(44,18))
        self.relate('connect','hands','clock-ne')
        self.relate('connect','hands','clock-se')
        self.relate('connect','hands','clock-nw')
