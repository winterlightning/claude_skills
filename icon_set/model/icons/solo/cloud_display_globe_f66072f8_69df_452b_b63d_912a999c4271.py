"""Cloud inside a round display globe on a low pedestal. VRECT_XL (5,2)-(43,46). Lucide cloud informs a flat base and broad lobes. Pedestal corner detail simplified."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f66072f8-69df-452b-b63d-912a999c4271'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-04/sphere_f66072f8-69df-452b-b63d-912a999c4271.svg'
AUTHOR = 'gpt-6'


class CloudDisplayGlobe(Solo48):
    icon_id = 'cloud-display-globe'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/decoration"
    aliases = ()
    keywords = ('globe', 'cloud', 'sphere', 'pedestal', 'display', 'ornament', 'decor')

    def build(self) -> None:
        self.add_arc('globe-l', (12, 36), (5, 21), radius_x=7, radius_y=15, sweep=True, large_arc=False)
        self.add_arc('globe-t', (5, 21), (43, 21), radius_x=19, radius_y=19, sweep=True, large_arc=False)
        self.add_arc('globe-r', (43, 21), (36, 36), radius_x=7, radius_y=15, sweep=True, large_arc=False)
        self.add_contour('globe', 'globe-l', 'globe-t', 'globe-r', closed=False)
        self.add_line('base-t', (12, 36), (36, 36))
        self.add_arc('base-tr', (36, 36), (40, 40), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('base-r', (40, 40), (40, 42))
        self.add_arc('base-br', (40, 42), (36, 46), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('base-b', (36, 46), (12, 46))
        self.add_arc('base-bl', (12, 46), (8, 42), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('base-l', (8, 42), (8, 40))
        self.add_arc('base-tl', (8, 40), (12, 36), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('base', 'base-t', 'base-tr', 'base-r', 'base-br', 'base-b', 'base-bl', 'base-l', 'base-tl', closed=True)
        self.relate('connect', 'globe', 'base')
        self.add_arc('cloud-left', (18, 27), (18, 17), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_arc('cloud-top', (18, 17), (30, 17), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('cloud-right', (30, 17), (30, 27), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('cloud-bottom', (30, 27), (18, 27))
        self.add_contour('cloud', 'cloud-left', 'cloud-top', 'cloud-right', 'cloud-bottom', closed=True)
