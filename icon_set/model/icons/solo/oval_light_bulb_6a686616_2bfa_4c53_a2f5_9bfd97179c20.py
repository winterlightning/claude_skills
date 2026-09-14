"""An upright light bulb with an oval glass envelope tapering into a narrow neck. A rounded socket band and small terminal form the base beneath the otherwise empty glass.
Taller oval glass and rounded socket; Lucide lightbulb construction. Empty glass retained; tiny terminal omitted.
Keyshape VRECT_L; centerline extremes (8,6)-(40,42). Tall envelope fits the upright subject. Source inspected as a standalone physical or conceptual subject."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6a686616-2bfa-4c53-a2f5-9bfd97179c20'
SOURCE_PATH = 'pictographic-primitives/work/bulb_6a686616-2bfa-4c53-a2f5-9bfd97179c20.svg'
AUTHOR = 'gpt-6'


class OvalLightBulb(Solo48):
    icon_id = 'oval-light-bulb'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/work"
    aliases = ()
    keywords = ('bulb', 'light', 'lamp', 'idea', 'illumination', 'electricity')

    def build(self) -> None:
        self.add_arc('dome', (8, 22), (40, 22), radius_x=16, radius_y=18, sweep=True, large_arc=False)
        self.add_arc('shoulder-right', (40, 22), (32, 34), radius_x=13, radius_y=13, sweep=True, large_arc=False)
        self.add_line('taper-right', (32, 34), (32, 36))
        self.add_line('neck-right', (32, 36), (32, 40))
        self.add_arc('base-right', (32, 40), (28, 42), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('base-bottom', (28, 42), (20, 42))
        self.add_arc('base-left', (20, 42), (16, 40), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('neck-left', (16, 40), (16, 36))
        self.add_line('taper-left', (16, 36), (16, 34))
        self.add_arc('shoulder-left', (16, 34), (8, 22), radius_x=13, radius_y=13, sweep=True, large_arc=False)
        self.add_contour('outline', 'dome', 'shoulder-right', 'taper-right', 'neck-right', 'base-right', 'base-bottom', 'base-left', 'neck-left', 'taper-left', 'shoulder-left', closed=True)
        self.add_line('base-seam', (16, 36), (32, 36))
        self.relate("connect", 'base-seam', 'outline')
