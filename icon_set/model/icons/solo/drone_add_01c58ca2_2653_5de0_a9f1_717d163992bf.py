"""A front-view drone with two rotors, landing supports and a plus badge.
Construction reference: drone: shared symmetry and repeated components; front-view silhouette follows the supplied reference.
Reduction: Reduced the undulating fuselage to a smooth capsule; retained badge enclosure.
Keyshape: SQUARE; geometry authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '01c58ca2-2653-5de0-a9f1-717d163992bf'
SOURCE_PATH = 'icon_set/work/todo-references/drone add_01c58ca2-2653-5de0-a9f1-717d163992bf.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'drone-add'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/media"
    aliases = ()
    keywords = ('drone', 'add')

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
        # Plan: mirrored rotor assemblies, body capsule, landing legs and plus badge.
        self.path('body',(10,14),[(38,14),((42,18),4,4,True),((38,22),4,4,True),(10,22),((6,18),4,4,True),((10,14),4,4,True)],True)
        for x in (11,37):
            self.add_polyline(f'rotor-{x}',(x-5,6),(x,6),(x+5,6))
            self.add_line(f'mast-{x}',(x,6),(x,14))
            self.relate('connect',f'rotor-{x}',f'mast-{x}')
            self.relate('connect',f'mast-{x}','body')
        self.add_polyline('leg-left',(15,22),(10,32),(14,32))
        self.add_polyline('leg-right',(33,22),(38,32),(34,32))
        for side in ('left','right'):
            self.relate('connect',f'leg-{side}','body')
        self.rect('badge',14,28,20,14,3)
        self.add_polyline('plus-horizontal',(20,35),(24,35),(28,35))
        self.add_polyline('plus-vertical',(24,31),(24,35),(24,39))
        self.relate('connect','plus-horizontal','plus-vertical')
