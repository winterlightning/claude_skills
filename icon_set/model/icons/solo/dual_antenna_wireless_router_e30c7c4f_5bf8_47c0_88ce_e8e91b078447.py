"""A wireless router carries two antennas with matching signal arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='e30c7c4f-5bf8-47c0-88ce-e8e91b078447'
SOURCE_PATH='pictographic-primitives/networks/router signal double_e30c7c4f-5bf8-47c0-88ce-e8e91b078447.svg'
AUTHOR='gpt-6'

class DualAntennaWirelessRouter(Solo48):
    icon_id='dual-antenna-wireless-router'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'networks'
    categories = ('primitives', 'networks')
    aliases=()
    keywords=('dual', 'antenna', 'wireless', 'router', 'network')

    def build(self):
        # Plan: A wireless router carries two antennas with matching signal arcs. Centerline extremes (6,6)-(42,42).
        # Reduction: Reduce each signal to one clear arc; retain both antennas and short feet.
        # Reference: Lucide router and wifi: attached antennas and circular signal arcs.
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

        # Body and feet share the same two attachment axes; paired signals repeat.
        path('body',(6,32),(14,32),(34,32),(42,32),(42,40),(34,40),(14,40),(6,40),closed=True)
        for n,x in enumerate([14,34]):
            line(f'antenna-{n}',(x,22),(x,32))
            arc(f'signal-{n}',(x-5,11),(x+5,11),5)
            line(f'foot-{n}',(x,40),(x,42))
        join_contacts()
