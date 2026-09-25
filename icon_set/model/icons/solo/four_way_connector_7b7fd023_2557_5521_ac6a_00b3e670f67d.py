"""A cross-shaped connector joins four outward leads."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='7b7fd023-2557-5521-ac6a-00b3e670f67d'
SOURCE_PATH='pictographic-primitives/networks/connector_7b7fd023-2557-5521-ac6a-00b3e670f67d.svg'
AUTHOR='gpt-6'

class FourWayConnector(Solo48):
    icon_id='four-way-connector'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'networks'
    aliases=()
    keywords=('four', 'way', 'connector', 'network')

    def build(self):
        # Plan: A cross-shaped connector joins four outward leads. Centerline extremes (6,6)-(42,42).
        # Reduction: Use a single rounded-join cross outline and four physical leads.
        # Reference: Lucide unplug: compact connector shell and attached leads.
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

        # Shared center 24 and quarter-turn symmetry define one connector.
        pts=[(18,14),(24,14),(30,14),(30,18),(34,18),(34,24),(34,30),(30,30),(30,34),(24,34),(18,34),(18,30),(14,30),(14,24),(14,18),(18,18)]
        path('shell',*pts,closed=True)
        for n,a,b in [('top',(24,6),(24,14)),('right',(34,24),(42,24)),('bottom',(24,34),(24,42)),('left',(6,24),(14,24))]:line(n,a,b)
        join_contacts()
