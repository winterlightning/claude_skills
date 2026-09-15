"""A chair tucked beneath a broad desk with a rounded front edge."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fa1a56a0-1c5c-4e6a-9fbf-7f8dc3520610'
SOURCE_PATH = 'pictographic-primitives/office/chair table_fa1a56a0-1c5c-4e6a-9fbf-7f8dc3520610.svg'
AUTHOR = 'gpt-6'


class DeskWithTuckedInChair(Solo48):
    icon_id = 'desk-with-tucked-in-chair'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/office"
    aliases = ()
    keywords = ('desk', 'chair', 'furniture', 'office', 'seat', 'workstation')

    # Construction reference: Lucide monitor: tangent quarter-circle corners on the desktop.
    def build(self):
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
        # Plan: broad desktop slab, visible upper arch, tucked seat and paired legs.
        # Centerline extremes (4,8)-(44,40), mirrored about x=24.
        axis=24
        arc('chair-arch',(16,16),(32,16),8)
        line('back-left',(16,16),(16,20))
        line('back-right',(32,16),(32,20))
        path('desktop-top',(8,20),(16,20),(32,20),(40,20))
        arc('front-right',(40,20),(44,24),4)
        line('edge-right',(44,24),(44,28))
        path('desktop-front',(44,28),(32,28),(16,28),(4,28))
        line('edge-left',(4,28),(4,24))
        arc('front-left',(4,24),(8,20),4)
        for side,x,foot in [('left',16,14),('right',32,34)]:
            path(f'chair-leg-{side}',(x,28),(x,36),(foot,40))
        line('seat',(16,36),(32,36))
        for side,x in [('left',4),('right',44)]:
            line(f'desk-leg-{side}',(x,28),(x,40))
        join_contacts()
