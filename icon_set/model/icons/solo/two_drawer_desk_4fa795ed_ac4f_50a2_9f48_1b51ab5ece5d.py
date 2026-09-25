"""A desk has a single leg and a two-drawer pedestal."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='4fa795ed-ac4f-50a2-9f48-1b51ab5ece5d'
SOURCE_PATH='pictographic-primitives/office/office desk_4fa795ed-ac4f-50a2-9f48-1b51ab5ece5d.svg'
AUTHOR='gpt-6'

class TwoDrawerDesk(Solo48):
    icon_id='two-drawer-desk'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "office"
    aliases=()
    keywords=('desk', 'drawers', 'furniture', 'office', 'table', 'workplace')

    def build(self):
        # Plan: A desk has a single leg and a two-drawer pedestal. Centerline extremes (4,8)-(44,40).
        # Reduction: Retain both drawers and pulls; omit desktop thickness.
        # Reference: Lucide monitor: split structural rails and rectangular spaces.
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
        path('top',(4,8),(24,8),(44,8))
        line('left-leg',(4,8),(4,40))
        path('pedestal',(24,8),(24,24),(24,40),(44,40),(44,24),(44,8))
        line('drawer-divider',(24,24),(44,24))
        for i,y in enumerate([16,32]):line(f'pull-{i}',(32,y),(36,y))
        join_contacts()
