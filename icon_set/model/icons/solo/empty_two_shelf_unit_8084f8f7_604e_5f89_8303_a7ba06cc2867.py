"""Two thick shelves span a pair of upright rails."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='8084f8f7-604e-5f89-8303-a7ba06cc2867'
SOURCE_PATH='pictographic-primitives/office/office shelf_8084f8f7-604e-5f89-8303-a7ba06cc2867.svg'
AUTHOR='gpt-6'

class EmptyTwoShelfUnit(Solo48):
    icon_id='empty-two-shelf-unit'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "office"
    aliases=()
    keywords=('shelf', 'shelving', 'storage', 'furniture', 'empty', 'office')

    def build(self):
        # Plan: Two thick shelves span a pair of upright rails. Centerline extremes (6,6)-(42,42).
        # Reduction: Retain both shelf slabs and projecting rails.
        # Reference: No close Lucide match; paired rails and repeated shelf definition.
        # All contacts below are physical joints sharing exact endpoints.
        endpoints = {}
        def line(name, a, b):
            self.add_line(name, a, b)
            endpoints[name] = (a, b)
        def path(name, *points, closed=False):
            self.add_polyline(name, *points, closed=closed)
            endpoints[name] = tuple(points)
        def arc(name, a, b, r, ry=None, sweep=True):
            self.add_arc(name, a, b, radius_x=r, radius_y=ry or r, sweep=sweep)
            endpoints[name] = (a, b)
        def join_contacts():
            names = list(endpoints)
            for i, a in enumerate(names):
                for b in names[i+1:]:
                    if set(endpoints[a]) & set(endpoints[b]):
                        self.relate("connect", a, b)
        def circle(name,cx,cy,r):
            arc(name+'-top',(cx-r,cy),(cx,cy-r),r)
            arc(name+'-right',(cx,cy-r),(cx+r,cy),r)
            arc(name+'-bottom',(cx+r,cy),(cx,cy+r),r)
            arc(name+'-left',(cx,cy+r),(cx-r,cy),r)
            self.add_contour(name,*(name+s for s in ['-top','-right','-bottom','-left']),closed=True)
        for i,x in enumerate([6,42]):path(f'rail-{i}',*((x,y) for y in [6,14,22,30,38,42]))
        for i,y in enumerate([14,30]):
            line(f'shelf-{i}-top',(6,y),(42,y))
            line(f'shelf-{i}-bottom',(6,y+8),(42,y+8))
        join_contacts()
