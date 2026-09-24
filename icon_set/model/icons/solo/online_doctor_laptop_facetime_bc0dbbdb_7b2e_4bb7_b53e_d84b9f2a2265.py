from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc0dbbdb-7b2e-4bb7-b53e-d84b9f2a2265'
SOURCE_PATH = 'icon_set/work/todo-references/online doctor laptop facetime_bc0dbbdb-7b2e-4bb7-b53e-d84b9f2a2265.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    """A doctor behind an open laptop.

    Plan: Circular head above smooth shoulders, cross on right chest, laptop in left foreground.
    Construction reference: laptop: tapered base; human_ref/user.svg: round head and broad arched shoulders.
    """
    icon_id = 'online-doctor-laptop-facetime'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('online', 'doctor', 'laptop', 'facetime')
    # human_ref/user.svg inspected. Head bottom y=22, shoulder top y=30: 8 centerline units / 4 ink units. Head radius 7, shoulder radius_x 14. Medical cross clearance is independently validated.

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

        self.circle('head',30,15,7)
        self.add_arc('shoulder',(16,37),(44,37),radius_x=14,radius_y=7)
        self.add_line('body-right',(44,37),(44,40)); self.add_contour('body','shoulder','body-right')
        self.add_polyline('laptop',(4,40),(7,32),(23,32),(28,40),(4,40))
        self.add_polyline('screen',(7,32),(7,23),(12,23)); self.relate('connect','screen','laptop')
        self.cross('medical',35,36,4)
