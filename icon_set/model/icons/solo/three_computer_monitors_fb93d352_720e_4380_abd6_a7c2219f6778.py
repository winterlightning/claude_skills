"""Three monitors form a triangular group on central stands."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='fb93d352-720e-4380-abd6-a7c2219f6778'
SOURCE_PATH='pictographic-primitives/networks/monitor network_fb93d352-720e-4380-abd6-a7c2219f6778.svg'
AUTHOR='gpt-6'

class ThreeComputerMonitors(Solo48):
    icon_id='three-computer-monitors'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'networks'
    aliases=()
    keywords=('three', 'computer', 'monitors', 'network')

    def build(self):
        # Plan: Three monitors form a triangular group on central stands. Centerline extremes (8,4)-(40,44).
        # Reduction: Retain three screens and feet; use simple rounded-join rectangles without bezels.
        # Reference: Lucide monitor: blank screen, central support and horizontal foot.
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

        # Identical lower monitor symbols mirrored about x=24, upper centered.
        for n,x,y,w in [('top',24,4,16),('left',14,28,12),('right',34,28,12)]:
            path(n+'-screen',(x-w//2,y),(x+w//2,y),(x+w//2,y+8),(x,y+8),(x-w//2,y+8),closed=True)
            line(n+'-stand',(x,y+8),(x,y+16))
            path(n+'-foot',(x-4,y+16),(x,y+16),(x+4,y+16))
        join_contacts()
