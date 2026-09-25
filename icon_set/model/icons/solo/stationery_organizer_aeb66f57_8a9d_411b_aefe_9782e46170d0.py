"""A low stationery holder contains a pencil and scissors."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='aeb66f57-8a9d-411b-aefe-9782e46170d0'
SOURCE_PATH='pictographic-primitives/office/stationery_aeb66f57-8a9d-411b-aefe-9782e46170d0.svg'
AUTHOR='gpt-6'

class StationeryOrganizer(Solo48):
    icon_id='stationery-organizer'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "office"
    aliases=()
    keywords=('stationery', 'organizer', 'pen', 'pencil', 'scissors', 'office')

    def build(self):
        # Centerline extremes (4,8)-(44,40).
        # Reduction: Omit the redundant pen and pocket clip; retain pointed pencil and two scissor loops.
        # Reference: Lucide scissors: paired circular handles and converging blades; pencil: pointed outline.
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
        # Plan: low holder, pointed pencil, repeated circular scissor handles and shared pivot and closed tips.
        path('holder',(4,32),(8,32),(16,32),(34,32),(44,32),(44,40),(4,40),closed=True)
        path('pencil',(8,32),(8,16),(12,8),(16,16),(16,32))
        for i,cx in enumerate([27,41]):circle(f'handle-{i}',cx,12,3)
        pivot=(34,28)
        path('blade-left',(27,15),pivot,(34,32))
        line('blade-right',(41,15),pivot)
        join_contacts()
