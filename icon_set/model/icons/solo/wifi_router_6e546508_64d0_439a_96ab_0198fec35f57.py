"""A router has a centered antenna beneath nested Wi-Fi waves."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='6e546508-64d0-439a-96ab-0198fec35f57'
SOURCE_PATH='pictographic-primitives/networks/router signal_6e546508-64d0-439a-96ab-0198fec35f57.svg'
AUTHOR='gpt-6'

class WifiRouter(Solo48):
    icon_id='wifi-router'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'networks'
    aliases=()
    keywords=('wifi', 'router', 'network')

    def build(self):
        # Plan: A router has a centered antenna beneath nested Wi-Fi waves. Centerline extremes (6,6)-(42,42).
        # Reduction: Reduce three signal arcs to two for clear spacing; retain central antenna and splayed feet.
        # Reference: Lucide wifi and router: concentric arcs with a shared center above the antenna.
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

        # Two concentric signal arcs centered at (24,20), radii 14 and 5.
        path('body',(6,32),(24,32),(42,32),(42,40),(34,40),(14,40),(6,40),closed=True)
        for n,r in enumerate([14,5]):arc(f'signal-{n}',(24-r,20),(24+r,20),r)
        line('antenna',(24,28),(24,32))
        for n,x in enumerate([14,34]):line(f'foot-{n}',(x,40),(x+(-2 if x<24 else 2),42))
        join_contacts()
