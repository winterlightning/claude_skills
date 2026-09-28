"""box-truck: reconstructed on SOLO48 from the supplied transportation reference."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '4ee62ba5-0a42-458b-9505-29245dd4d0a6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__box-truck/20260926T073831Z-thuan-mac/reference/truck 2_4ee62ba5-0a42-458b-9505-29245dd4d0a6.svg'
AUTHOR = "claude-opus-5-5"


class BoxTruck(Solo48):
    icon_id = 'box-truck'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    categories = ("transportation", "primitives")
    aliases = ()
    keywords = ('truck', 'box truck', 'delivery', 'lorry', 'cargo', 'shipping', 'logistics', 'vehicle')

    def build(self):
        # Redraw (no reviewer text; matched to the reference): a box truck facing right in one
        # outline - cargo box x 4..28 from the roof y 8 (r4 corners) down to the chassis y 35,
        # a lower cab x 28..44 from y 16 with a slanted windscreen (36, 16)-(44, 24), and two r5
        # wheels centred on the chassis line at (13, 35) and (33, 35), set into the body as in the
        # reference: the outline runs into each wheel's side points, and the cab's back wall
        # drops to the rear wheel.
        self.add_line('box-left', (4, 31), (4, 12))
        self.add_arc('box-corner-nw', (4, 12), (8, 8), radius_x=4)
        self.add_line('box-top', (8, 8), (24, 8))
        self.add_arc('box-corner-ne', (24, 8), (28, 12), radius_x=4)
        self.add_line('box-back-upper', (28, 12), (28, 16))
        self.add_line('cab-top', (28, 16), (36, 16))
        self.add_line('windscreen', (36, 16), (44, 24))
        self.add_line('cab-front', (44, 24), (44, 31))
        self.add_arc('cab-corner', (44, 31), (40, 35), radius_x=4)
        self.add_line('chassis-front', (40, 35), (38, 35))
        self.add_contour('body', 'box-left', 'box-corner-nw', 'box-top', 'box-corner-ne', 'box-back-upper', 'cab-top',
                         'windscreen', 'cab-front', 'cab-corner', 'chassis-front')
        self.add_arc('box-corner-sw', (4, 31), (8, 35), radius_x=4, sweep=False)
        self.relate('connect', 'body', 'box-corner-sw')
        self.add_line('chassis-mid', (18, 35), (28, 35))
        self.add_line('cab-back', (28, 16), (28, 35))
        self.relate('connect', 'body', 'cab-back')
        self.relate('connect', 'cab-back', 'chassis-mid')
        for name, cx in (('wheel-rear', 13), ('wheel-front', 33)):
            r, cy = 5, 35
            pts = [(cx - r, cy), (cx, cy - r), (cx + r, cy), (cx, cy + r)]
            names = tuple(f'{name}-{q}' for q in ('nw', 'ne', 'se', 'sw'))
            for i, n in enumerate(names):
                self.add_arc(n, pts[i], pts[(i + 1) % 4], radius_x=r)
            self.add_contour(name, *names, closed=True)
            self.relate('connect', name, 'chassis-mid')
        self.relate('connect', 'wheel-rear', 'box-corner-sw')
        self.relate('connect', 'wheel-front', 'body')
        self.relate('connect', 'wheel-front', 'cab-back')
