"""Two overlapping triangles form a six-point star surrounding an eye.

Plan: Two triangles reflected about y24; eye uses paired smooth arcs and circular pupil. VRECT_L extremes (8,4)-(40,44). All components retained. Crossing lines left honestly unresolved for validation. No useful Lucide match for full nested symbol.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '240b3739-6bb7-5bfa-832d-48a5bdaa33e8'
SOURCE_PATH = 'icon_set/work/todo-references/astrology_240b3739-6bb7-5bfa-832d-48a5bdaa33e8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'astrology'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('astrology',)
    def build(self):
        axis=24
        self.add_polyline('triangle-up',(axis,4),(40,34),(8,34),closed=True)
        self.add_polyline('triangle-down',(axis,44),(8,14),(40,14),closed=True)
        self.add_arc('eye-top',(16,24),(32,24),radius_x=10,radius_y=8)
        self.add_arc('eye-bottom',(32,24),(16,24),radius_x=10,radius_y=8)
        self.add_contour('eye','eye-top','eye-bottom',closed=True)
        self.circle('pupil',24,24,2)

    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def roundrect(self,name,x0,y0,x1,y1,r):
        nodes=[(x0+r,y0),(x1-r,y0),(x1,y0+r),(x1,y1-r),(x1-r,y1),(x0+r,y1),(x0,y1-r),(x0,y0+r)]
        for i,a in enumerate(nodes):
            b=nodes[(i+1)%8]
            if i%2:self.add_arc(f'{name}-{i}',a,b,radius_x=r)
            else:self.add_line(f'{name}-{i}',a,b)
        self.add_contour(name,*(f'{name}-{i}' for i in range(8)),closed=True)
