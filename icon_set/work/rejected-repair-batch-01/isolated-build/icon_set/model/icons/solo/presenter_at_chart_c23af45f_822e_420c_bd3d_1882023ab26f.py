"""A presenter raises one arm toward a wall-mounted chart."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='c23af45f-822e-420c-bd3d-1882023ab26f'
SOURCE_PATH='pictographic-primitives/office/workflow coaching chart_c23af45f-822e-420c-bd3d-1882023ab26f.svg'
AUTHOR='gpt-6'

class PresenterAtChart(Solo48):
    icon_id='presenter-at-chart'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/office"
    aliases=()
    keywords=('presenter', 'chart', 'screen', 'coaching', 'person', 'office')

    def build(self):
        # Centerline extremes (4,8)-(44,40).
        # Reduction: Reduce zigzag to one rising segment; omit frame thickness and small arm detail.
        # Reference: human_ref/user.svg and full_body_ref.png: head and torso; Lucide chart-line and presentation: screen and trend.
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
        # Plan: circular head, shoulder quarter-arc, raised arm and partially open screen.
        # Head r4 at (10,16): bottom20. Shoulder apex28: exact detached ink gap4.
        circle('head',10,16,4)
        line('body-left',(4,40),(4,34))
        arc('shoulder',(4,34),(10,28),6)
        line('shoulder-top',(10,28),(16,28))
        line('body-right',(16,28),(16,40))
        line('raised-arm',(16,28),(24,20))
        path('screen',(24,20),(24,8),(44,8),(44,32),(24,32))
        line('trend',(32,22),(36,18))
        join_contacts()
