"""A gateway block branches into three rectangular network endpoints."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='767db7df-b6eb-5c67-9c96-01e7aad4770b'
SOURCE_PATH='pictographic-primitives/networks/gateway api_767db7df-b6eb-5c67-9c96-01e7aad4770b.svg'
AUTHOR='gpt-6'

class GatewayNetworkTree(Solo48):
    icon_id='gateway-network-tree'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'networks'
    aliases=()
    keywords=('gateway', 'network', 'tree', 'network')

    def build(self):
        # Plan: A gateway block branches into three rectangular network endpoints. Centerline extremes (4,8)-(44,40).
        # Reduction: Retain all three endpoints and a broad top gateway; omit perspective tilt.
        # Reference: Lucide network: rectangular nodes and orthogonal shared branch connections.
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

        # Gateway centered at 24; endpoints repeated at pitch 16 with 8-unit openings.
        path('gateway',(16,8),(32,8),(32,16),(24,16),(16,16),closed=True)
        line('trunk',(24,16),(24,24))
        path('bus-left',(8,32),(8,24),(24,24))
        path('bus-right',(24,24),(40,24),(40,32))
        line('middle-lead',(24,24),(24,32))
        for n,x in enumerate([8,24,40]):path(f'endpoint-{n}',(x,32),(x+4,32),(x+4,40),(x-4,40),(x-4,32),closed=True)
        join_contacts()
