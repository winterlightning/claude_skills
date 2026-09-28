"""A tape roll sits in a low dispenser with a raised cutter."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='21247aa3-cf95-5bbc-8785-366de4dab5a7'
SOURCE_PATH='pictographic-primitives/office/office tape_21247aa3-cf95-5bbc-8785-366de4dab5a7.svg'
AUTHOR='gpt-6'

class DesktopTapeDispenser(Solo48):
    icon_id='desktop-tape-dispenser'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "office"
    categories = ("office", "primitives")
    aliases=()
    keywords=('tape', 'dispenser', 'roll', 'adhesive', 'stationery', 'office')

    def build(self):
        # Plan: A tape roll sits in a low dispenser with a raised cutter. Centerline extremes (4,8)-(44,40).
        # Reduction: Omit inner tape path; retain central opening and raised cutter.
        # Reference: No useful Lucide tape match; concentric circle and connected base.
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
        circle('roll',16,20,12)
        circle('hub',16,20,3)
        path('dispenser',(4,20),(4,40),(44,40),(44,20),(28,20))
        join_contacts()
