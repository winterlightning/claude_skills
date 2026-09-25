"""A domed access hub feeds three circular nodes and downward arrows."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='9b159089-ab97-498a-9429-4100c9ea1ed7'
SOURCE_PATH='pictographic-primitives/networks/gpon access 3_9b159089-ab97-498a-9429-4100c9ea1ed7.svg'
AUTHOR='gpt-6'

class ThreeBranchAccessNetwork(Solo48):
    icon_id='three-branch-access-network'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'networks'
    aliases=()
    keywords=('three', 'branch', 'access', 'network', 'network')

    def build(self):
        # Plan: A domed access hub feeds three circular nodes and downward arrows. Centerline extremes (6,6)-(42,42).
        # Reduction: Flatten the hub dome; retain all three node-and-arrow branches.
        # Reference: Lucide network: repeated nodes and shared branch attachment points.
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

        # Dome with shared baseline, three branches at constant pitch 14.
        arc('dome-left',(6,16),(16,6),10)
        line('dome-top',(16,6),(32,6))
        arc('dome-right',(32,6),(42,16),10)
        path('base',(42,16),(38,16),(24,16),(10,16),(6,16))
        for n,x in enumerate([10,24,38]):
            circle(f'node-{n}',x,28,3)
            line(f'lead-{n}',(x,16),(x,25))
            line(f'shaft-{n}',(x,31),(x,42))
            path(f'head-{n}',(x-3,40),(x,42),(x+3,40))
        join_contacts()
