"""An arched desktop hole punch stands on a broad base."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='4d33055e-78f5-4158-b719-697c41ecf87d'
SOURCE_PATH='pictographic-primitives/office/hole puncher_4d33055e-78f5-4158-b719-697c41ecf87d.svg'
AUTHOR='gpt-6'

class DesktopHolePunch(Solo48):
    icon_id='desktop-hole-punch'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "office"
    categories = ("office", "primitives")
    aliases=()
    keywords=('hole punch', 'puncher', 'paper', 'stationery', 'desktop', 'office')

    def build(self):
        # Plan: An arched desktop hole punch stands on a broad base. Centerline extremes (4,8)-(44,40).
        # Reduction: Keep raised arched handle and two posts; omit small seam details.
        # Reference: Lucide presentation: simple structural attachments.
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
        path('handle',(8,24),(8,16),(12,8),(36,8),(40,16),(40,24))
        arc('handle-opening',(16,24),(32,24),8)
        path('base-top',(8,24),(12,24),(16,24),(32,24),(36,24),(40,24))
        path('base',(8,24),(4,32),(4,40),(44,40),(44,32),(40,24))
        path('base-seam',(4,32),(16,32),(32,32),(44,32))
        for i,x in enumerate([16,32]):line(f'post-{i}',(x,24),(x,32))
        join_contacts()
