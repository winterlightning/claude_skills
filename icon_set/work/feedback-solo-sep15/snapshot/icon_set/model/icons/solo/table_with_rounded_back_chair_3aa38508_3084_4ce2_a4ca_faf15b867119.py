"""A rounded-back chair with splayed legs in front of a straight-legged table."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3aa38508-3084-4ce2-a4ca-faf15b867119'
SOURCE_PATH = 'pictographic-primitives/office/chair table_3aa38508-3084-4ce2-a4ca-faf15b867119.svg'
AUTHOR = 'gpt-6'


class TableWithRoundedBackChair(Solo48):
    icon_id = 'table-with-rounded-back-chair'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/office"
    aliases = ()
    keywords = ('table', 'chair', 'furniture', 'office', 'seat', 'workstation')

    # Construction reference: Lucide monitor: clean structural rails; source sets mirrored chair arch.
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
        # Plan: mirrored chair arch and legs; tabletop and seat remain 8 apart.
        # Centerline extremes (4,8)-(44,40), axis x=24.
        axis=24
        arc('chair-arch',(16,16),(32,16),8)
        for side,x,foot in [('left',axis-8,axis-10),('right',axis+8,axis+10)]:
            path(f'chair-{side}',(x,16),(x,24),(x,32),(foot,40))
        line('seat',(16,32),(32,32))
        path('tabletop',(4,24),(16,24),(32,24),(44,24))
        for side,x in [('left',4),('right',44)]:
            line(f'table-{side}',(x,24),(x,40))
        join_contacts()
