"""Two matching computer workstations on a shared desk."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1079e644-2347-4a3c-a0ea-30da82079073'
SOURCE_PATH = 'pictographic-primitives/office/co working space monitors_1079e644-2347-4a3c-a0ea-30da82079073.svg'
AUTHOR = 'gpt-6'


class SharedComputerWorkstations(Solo48):
    icon_id = 'shared-computer-workstations'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "office"
    aliases = ()
    keywords = ('computer', 'monitor', 'desk', 'coworking', 'workstation', 'office')

    # Construction reference: Lucide monitor: blank screen, centered stand, repeated definition; use square corners to maximize screen space.
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
        # Plan: repeated blank monitor definition, two stems, one desk with outer legs.
        # Centerline extremes (4,8)-(44,40). Drop redundant third station and rear table.
        for col in range(2):
            x=4+col*24
            path(f'monitor-{col}',(x+8,24),(x,24),(x,8),(x+16,8),(x+16,24),(x+8,24),closed=True)
            line(f'stand-{col}',(x+8,24),(x+8,32))
        path('desk',(4,40),(4,32),(12,32),(36,32),(44,32),(44,40))
        join_contacts()
