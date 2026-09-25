"""A lectern holds a blank sheet beside a tilted microphone."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='af728de7-23d6-4f1b-bb5b-222a29c317e7'
SOURCE_PATH='pictographic-primitives/office/presentation desk paper_af728de7-23d6-4f1b-bb5b-222a29c317e7.svg'
AUTHOR='gpt-6'

class LecternWithPaper(Solo48):
    icon_id='lectern-with-paper'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "office"
    categories = ("office", "primitives")
    aliases=()
    keywords=('lectern', 'paper', 'microphone', 'presentation', 'podium', 'office')

    def build(self):
        # Centerline extremes (4,8)-(44,40).
        # Reduction: Raise the blank sheet; omit surface thickness and microphone capsule.
        # Reference: Lucide mic: simple stem; presentation: board and support.
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
        # Plan: same physical lectern vocabulary, shorter blank paper and angled microphone.
        axis=24
        path('surface',(8,24),(axis,24),(40,24),(44,32),(axis,32),(4,32),closed=True)
        path('paper',(axis,24),(axis,12),(40,12),(40,24))
        line('microphone',(8,24),(16,8))
        line('pedestal',(axis,32),(axis,40))
        join_contacts()
