"""A router broadcasts from a central round-tipped antenna between side waves."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='692ad9ca-edb7-4539-b99a-547069c275e7'
SOURCE_PATH='pictographic-primitives/networks/router signal_692ad9ca-edb7-4539-b99a-547069c275e7.svg'
AUTHOR='gpt-6'

class BroadcastRouter(Solo48):
    icon_id='broadcast-router'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'networks'
    aliases=()
    keywords=('broadcast', 'router', 'network')

    def build(self):
        # Plan: A router broadcasts from a central round-tipped antenna between side waves. Centerline extremes (6,6)-(42,42).
        # Reduction: Use one wave per side to keep the round antenna tip and broadcast arrangement clear.
        # Reference: Lucide radio and router: round antenna tip between mirrored circular waves.
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

        # Mirror side waves around x=24; center tip and antenna share endpoints.
        path('body',(6,32),(24,32),(42,32),(42,40),(34,40),(14,40),(6,40),closed=True)
        circle('tip',24,14,3)
        line('antenna',(24,17),(24,32))
        arc('wave-left',(12,6),(12,22),10,sweep=False)
        arc('wave-right',(36,22),(36,6),10,sweep=False)
        for n,x in enumerate([14,34]):line(f'foot-{n}',(x,40),(x+(-2 if x<24 else 2),42))
        join_contacts()
