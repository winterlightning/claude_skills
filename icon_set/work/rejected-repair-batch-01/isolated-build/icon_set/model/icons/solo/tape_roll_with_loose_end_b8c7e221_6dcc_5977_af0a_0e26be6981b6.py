"""A circular tape roll has a loose strip extending left."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='b8c7e221-6dcc-5977-af0a-0e26be6981b6'
SOURCE_PATH='pictographic-primitives/office/office tape_b8c7e221-6dcc-5977-af0a-0e26be6981b6.svg'
AUTHOR='gpt-6'

class TapeRollWithLooseEnd(Solo48):
    icon_id='tape-roll-with-loose-end'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/office"
    aliases=()
    keywords=('tape', 'roll', 'adhesive', 'strip', 'stationery', 'office')

    def build(self):
        # Plan: A circular tape roll has a loose strip extending left. Centerline extremes (4,8)-(44,40).
        # Reduction: Keep concentric roll and short loose end.
        # Reference: No useful Lucide tape match; concentric circular construction.
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
        circle('roll',28,24,16)
        circle('opening',28,24,7)
        line('loose-end',(4,40),(28,40))
        join_contacts()
