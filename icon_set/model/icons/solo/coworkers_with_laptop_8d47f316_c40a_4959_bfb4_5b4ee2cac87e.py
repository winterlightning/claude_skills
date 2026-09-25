"""Two coworkers sit together behind a laptop at a shared table."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8d47f316-c40a-4959-bfb4-5b4ee2cac87e'
SOURCE_PATH = 'pictographic-primitives/office/co working space team laptop_8d47f316-c40a-4959-bfb4-5b4ee2cac87e.svg'
AUTHOR = 'gpt-6'


class CoworkersWithLaptop(Solo48):
    icon_id = 'coworkers-with-laptop'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "office"
    aliases = ()
    keywords = ('coworkers', 'laptop', 'team', 'desk', 'people', 'office')

    # Construction reference: human_ref/user.svg and full_body_ref.png: outlined circular heads and smooth shoulders. Lucide monitor: screen construction.
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
        # Plan: two identical circular heads and shoulder arcs; laptop covers right torso.
        # Human refs: icon_set/references/human_ref/user.svg and full_body_ref.png.
        # Head radius 4, cy=8; shoulder top=20 => exact 4-unit visible gap (20-12-4).
        # Centerline extremes (8,4)-(40,44). Laptop makes lower scene asymmetric.
        for col in range(2):
            cx=16+col*16
            arc(f'head-{col}-upper',(cx-4,8),(cx+4,8),4)
            arc(f'head-{col}-lower',(cx+4,8),(cx-4,8),4)
            self.add_contour(f'head-{col}',f'head-{col}-upper',f'head-{col}-lower',closed=True)
            arc(f'shoulders-{col}',(cx-8,28),(cx+8,28),8)
        line('left-body',(8,28),(8,44))
        path('laptop',(24,44),(24,28),(40,28),(40,44))
        path('table',(8,44),(24,44),(40,44))
        self.add_dot('laptop-mark',(32,36))
        join_contacts()
