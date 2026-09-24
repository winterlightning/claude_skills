"""A circular compass with a northeast needle and the letter E underneath.
Construction reference: compass: circular housing and angular directional needle.
Reduction: Retained four compass ticks and E. Deliberate northeast orientation follows the source.
Keyshape: VRECT_M; geometry authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ad12d3ce-dd3a-4c8e-9db3-83b54c4a1c0b'
SOURCE_PATH = 'icon_set/work/todo-references/east_ad12d3ce-dd3a-4c8e-9db3-83b54c4a1c0b.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'east'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/media"
    aliases = ()
    keywords = ('east',)

    def path(self, name, start, segments, closed=False):
        members = []
        for i, spec in enumerate(segments):
            part = f"{name}-{i+1}"
            if len(spec) == 2:
                end = spec
                self.add_line(part, start, end)
            else:
                end, rx, ry, sweep = spec
                self.add_arc(part, start, end, radius_x=rx, radius_y=ry, sweep=sweep)
            members.append(part)
            start = end
        self.add_contour(name, *members, closed=closed)

    def circle(self, name, x, y, r):
        self.path(name, (x-r,y), [((x+r,y),r,r,True),((x-r,y),r,r,True)], True)

    def rect(self, name, x, y, w, h, r=3):
        self.path(name, (x+r,y), [(x+w-r,y),((x+w,y+r),r,r,True),(x+w,y+h-r),((x+w-r,y+h),r,r,True),(x+r,y+h),((x,y+h-r),r,r,True),(x,y+r),((x+r,y),r,r,True)], True)

    def build(self):
        # Plan: four housing quadrants and radial ticks; concave needle and hand-drawn E.
        cx,cy,r=24,18,14
        self.path('rim',(24,4),[((38,18),r,r,True),((24,32),r,r,True),((10,18),r,r,True),((24,4),r,r,True)],True)
        for name,a,b in [('north',(24,4),(24,6)),('east',(38,18),(36,18)),('south',(24,32),(24,30)),('west',(10,18),(12,18))]:
            self.add_line(name,a,b)
            self.relate('connect',name,'rim')
        self.add_polyline('needle',(19,17),(30,12),(25,23),(23,19),closed=True)
        self.add_polyline('letter-e',(28,36),(20,36),(20,40),(20,44),(28,44))
        self.add_line('e-middle',(20,40),(26,40))
        self.relate('connect','letter-e','e-middle')
