"""Two matching pans hang from a level balance beam."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='147e1cba-168d-4203-a9f8-c59cde7b9f36'
SOURCE_PATH='pictographic-primitives/office/legal scale_147e1cba-168d-4203-a9f8-c59cde7b9f36.svg'
AUTHOR='gpt-6'

class BalanceScales(Solo48):
    icon_id='balance-scales'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "office"
    aliases=()
    keywords=('scales', 'balance', 'justice', 'legal', 'weighing', 'office')

    def build(self):
        # Plan: Two matching pans hang from a level balance beam. Centerline extremes (4,8)-(44,40).
        # Reduction: Reduce stepped base to a bar and finial to a stem.
        # Reference: Lucide scale: shared axis and repeated suspended pans.
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
        axis=24
        path('stem',(axis,8),(axis,16),(axis,40))
        path('beam',(4,16),(10,16),(24,16),(38,16),(44,16))
        path('foot',(16,40),(24,40),(32,40))
        for i,cx in enumerate([10,38]):
            line(f'hanger-{i}',(cx,16),(cx,24))
            path(f'rim-{i}',(cx-6,24),(cx,24),(cx+6,24))
            arc(f'pan-{i}',(cx+6,24),(cx-6,24),6,8)
        join_contacts()
