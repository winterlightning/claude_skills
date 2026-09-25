"""A water cooler stands beside a round potted plant."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='1838ba45-d0da-4e78-b2ef-7c142885a298'
SOURCE_PATH='pictographic-primitives/office/outdoors_1838ba45-d0da-4e78-b2ef-7c142885a298.svg'
AUTHOR='gpt-6'

class WaterCoolerWithPottedPlant(Solo48):
    icon_id='water-cooler-with-potted-plant'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "office"
    aliases=()
    keywords=('water cooler', 'plant', 'pot', 'dispenser', 'workplace', 'office')

    def build(self):
        # Plan: A water cooler stands beside a round potted plant. Centerline extremes (4,8)-(44,40).
        # Reduction: Reduce bottle bands to one division and tap to a dot.
        # Reference: Lucide milk: inverted bottle silhouette; source sets the plant companion.
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
        path('cooler',(4,40),(4,20),(4,12))
        arc('bottle-tl',(4,12),(8,8),4)
        line('bottle-top',(8,8),(16,8))
        arc('bottle-tr',(16,8),(20,12),4)
        path('cooler-right',(20,12),(20,20),(20,40),(4,40))
        line('bottle-base',(4,20),(20,20))
        self.add_dot('tap',(12,28))
        circle('canopy',36,18,6)
        line('trunk',(36,24),(36,32))
        path('pot',(28,32),(36,32),(44,32),(42,40),(30,40),closed=True)
        join_contacts()
