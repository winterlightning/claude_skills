"""A tall cabinet has one inset drawer and two short feet."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='98811014-730c-4372-b33b-b7f55029429e'
SOURCE_PATH='pictographic-primitives/office/shelf corner_98811014-730c-4372-b33b-b7f55029429e.svg'
AUTHOR='gpt-6'

class SingleDrawerCabinet(Solo48):
    icon_id='single-drawer-cabinet'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/office"
    aliases=()
    keywords=('cabinet', 'drawer', 'storage', 'furniture', 'handle', 'office')

    def build(self):
        # Centerline extremes (8,4)-(40,44).
        # Reduction: Reduce drawer pull to a centered knob; retain drawer inset and feet.
        # Reference: Lucide book: simple inset rectangular structure.
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
        # Plan: cabinet outline; centered drawer rectangle; pair of aligned feet.
        axis=24;left=8;right=2*axis-left
        path('cabinet',(left,4),(right,4),(right,40),(left,40),closed=True)
        path('drawer',(16,16),(2*axis-16,16),(2*axis-16,32),(16,32),closed=True)
        self.add_dot('pull',(axis,24))
        for i,x in enumerate([left,right]):line(f'foot-{i}',(x,40),(x,44))
        join_contacts()
