"""Two cars with a lightning bolt and noise marks.
Repair plan: Open lightning zigzag; repeated car bodies and paired wheels preserve the traffic scene. Noise marks intentionally differ.
Omissions: Return side of the outlined lightning bolt.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8e9b7bc2-90cb-457c-b184-e60fb8d06b7b'
SOURCE_PATH = 'pictographic-primitives/ecology/noise pollution traffic_8e9b7bc2-90cb-457c-b184-e60fb8d06b7b.svg'
AUTHOR = 'gpt-6'
# Construction plan: Two repeated front-facing cars below a central lightning bolt; shared car dimensions preserve equality.
# Keyshape visible extremes are supplied by Keyshape.SQUARE.bounds_for(SOLO48).
# Lucide construction reference: car-front.
class Drawing(Solo48):
    icon_id = 'noise-pollution-traffic'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'ecology'
    aliases = ()
    keywords = ('noise', 'pollution', 'traffic')
    def build(self):
        for i,x in enumerate((6,30)):
            self.add_polyline(f'car-{i}',(x,38),(x,32),(x+3,26),(x+9,26),(x+12,32),(x+12,38),closed=True)
            for j,dx in enumerate((0,12)):
                self.add_line(f'wheel-{i}-{j}',(x+dx,38),(x+dx,42))
                self.relate('connect',f'car-{i}',f'wheel-{i}-{j}')
        self.add_polyline('lightning',(28,6),(18,14),(32,14),(22,22))
        self.add_polyline('noise-left',(6,14),(8,18),(10,14))
        self.add_polyline('noise-right',(40,8),(42,12),(40,16))

    def oval(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-top', (cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def box(self, name, x, y, right, bottom, r=3):
        points=[(x+r,y),(right-r,y),(right,y+r),(right,bottom-r),(right-r,bottom),(x+r,bottom),(x,bottom-r),(x,y+r),(x+r,y)]
        members=[]
        for i,(a,b) in enumerate(zip(points,points[1:])):
            part=f'{name}-{i}'
            if i%2: self.add_arc(part,a,b,radius_x=r)
            else: self.add_line(part,a,b)
            members.append(part)
        self.add_contour(name,*members,closed=True)

    def cross(self,name,cx,cy,r):
        for suffix,p in [('left',(cx-r,cy)),('right',(cx+r,cy)),('top',(cx,cy-r)),('bottom',(cx,cy+r))]:
            self.add_line(name+'-'+suffix,p,(cx,cy))
        self.relate('connect',*[name+'-'+s for s in ('left','right','top','bottom')])

    def clipboard(self):
        self.box('clip',17,4,31,12,4)
        self.add_polyline('board',(17,8),(8,8),(8,44),(40,44),(40,8),(31,8))
        self.relate('connect','clip','board')


# Visible keyshape extremes: (4, 4, 44, 44).
# Visual review: Open lightning and paired cars remain recognizable at native size.
