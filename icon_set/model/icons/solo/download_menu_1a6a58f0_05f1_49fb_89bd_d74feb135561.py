"""A downward download arrow above three horizontal menu rules.
Construction reference: arrow-down: shaft joins a mirrored chevron at its tip.
Reduction: No omissions.
Keyshape: VRECT_M; geometry authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1a6a58f0-05f1-49fb-89bd-d74feb135561'
SOURCE_PATH = 'icon_set/work/todo-references/download menu_1a6a58f0-05f1-49fb-89bd-d74feb135561.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'download-menu'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/media"
    aliases = ()
    keywords = ('download', 'menu')

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
        # Plan: mirrored arrow at x=24 and three evenly spaced menu rules.
        self.add_line('shaft',(24,4),(24,20))
        self.add_polyline('arrowhead',(14,10),(24,20),(34,10))
        self.relate('connect','shaft','arrowhead')
        for i,y in enumerate((28,36,44)):
            self.add_line(f'rule-{i}',(10,y),(38,y))
