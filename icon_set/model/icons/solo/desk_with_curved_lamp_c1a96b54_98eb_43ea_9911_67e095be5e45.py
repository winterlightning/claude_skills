"""A trestle desk with a curved lamp attached at its right edge."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c1a96b54-98eb-43ea-9911-67e095be5e45'
SOURCE_PATH = 'pictographic-primitives/office/desk lamp_c1a96b54-98eb-43ea-9911-67e095be5e45.svg'
AUTHOR = 'gpt-6'


class DeskWithCurvedLamp(Solo48):
    icon_id = 'desk-with-curved-lamp'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "office"
    categories = ("office", "primitives")
    aliases = ()
    keywords = ('desk', 'lamp', 'table', 'trestle', 'furniture', 'office')

    # Construction reference: Lucide lamp-desk: arm and hood separation by structural purpose; source sets the curved arm. The arm is intentionally on the right.
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
        # Plan: trapezoid desk; paired splayed trestles; tangent quarter-circle lamp arm.
        # Centerline extremes (4,8)-(44,40). Lamp intentionally on right.
        path('desktop',(8,24),(40,24),(44,32),(34,32),(14,32),(4,32),closed=True)
        line('lamp-hood',(16,8),(28,8))
        arc('lamp-curve',(28,8),(40,20),12)
        line('lamp-neck',(40,20),(40,24))
        for side,cx in [('left',14),('right',34)]:
            path(f'trestle-{side}',(cx-4,40),(cx,32),(cx+4,40))
        join_contacts()
