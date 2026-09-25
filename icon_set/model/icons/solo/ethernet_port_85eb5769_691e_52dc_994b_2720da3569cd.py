"""An Ethernet socket has a stepped latch notch and four contact pins."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='85eb5769-691e-52dc-994b-2720da3569cd'
SOURCE_PATH='pictographic-primitives/networks/ethernet port_85eb5769-691e-52dc-994b-2720da3569cd.svg'
AUTHOR='gpt-6'

class EthernetPort(Solo48):
    icon_id='ethernet-port'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'networks'
    aliases=()
    keywords=('ethernet', 'port', 'network')

    def build(self):
        # Plan: An Ethernet socket has a stepped latch notch and four contact pins. Centerline extremes (4,8)-(44,40).
        # Reduction: Remove redundant outer faceplate to preserve the socket notch and all four pins at valid spacing.
        # Reference: Lucide ethernet-port: one stepped socket silhouette and evenly spaced contacts.
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

        # Shared notch axis x=24; four contacts at constant pitch 8.
        path('socket',(4,40),(4,16),(16,16),(16,8),(32,8),(32,16),(44,16),(44,40),closed=True)
        for n,x in enumerate(range(12,37,8)):line(f'pin-{n}',(x,25),(x,32))
        join_contacts()
