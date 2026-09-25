"""An office building has three windows around a lower-right arched doorway."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='8d540d04-67f3-4692-b0a9-c2e07729d239'
SOURCE_PATH='pictographic-primitives/office/small office tall building_8d540d04-67f3-4692-b0a9-c2e07729d239.svg'
AUTHOR='gpt-6'

class ThreeWindowOfficeBuilding(Solo48):
    icon_id='three-window-office-building'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "office"
    aliases=()
    keywords=('building', 'office', 'windows', 'door', 'architecture', 'workplace')

    def build(self):
        # Centerline extremes (6,6)-(42,42).
        # Reduction: Represent all three windows as dots; retain their arrangement and the roof band.
        # Reference: Lucide building: repeated window positions and arched doorway.
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
        # Plan: roof band, walls, three window positions and offset entrance.
        path('roof',(6,6),(42,6),(42,14),(40,14),(8,14),(6,14),closed=True)
        path('wall-left',(8,14),(8,42),(24,42))
        path('wall-right',(32,42),(40,42),(40,14))
        path('ground-left',(6,42),(8,42))
        path('ground-right',(40,42),(42,42))
        for i,(x,y) in enumerate([(16,22),(28,22),(16,34)]):self.add_dot(f'window-{i}',(x,y))
        line('door-left',(24,42),(24,34))
        arc('door-arch',(24,34),(32,34),4)
        line('door-right',(32,34),(32,42))
        line('threshold',(24,42),(32,42))
        join_contacts()
