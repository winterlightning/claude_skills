"""A light bulb with a broad rounded glass envelope narrowing into a short base. A horizontal seam separates the glass from the rounded bottom cap; the outline is vertically symmetrical.
Symmetric broad glass with tangent shoulder transitions and rounded socket; Lucide lightbulb construction. Tiny terminal omitted.
Keyshape VRECT_L; centerline extremes (8,6)-(40,42). Tall envelope fits the upright subject. Source inspected as a standalone physical or conceptual subject."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6af73469-938c-4006-9537-bc65e0be96b4'
SOURCE_PATH = 'pictographic-primitives/work/bulb 1_6af73469-938c-4006-9537-bc65e0be96b4.svg'
AUTHOR = 'gpt-6'


class BroadLightBulb(Solo48):
    icon_id = 'broad-light-bulb'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/work"
    aliases = ()
    keywords = ('bulb', 'light', 'lamp', 'idea', 'illumination', 'electricity')

    def build(self) -> None:
        self.add_arc('dome', (8, 20), (40, 20), radius_x=16, radius_y=16, sweep=True, large_arc=False)
        self.add_arc('shoulder-right', (40, 20), (34, 32), radius_x=15, radius_y=15, sweep=True, large_arc=False)
        self.add_arc('taper-right', (34, 32), (32, 36), radius_x=5, radius_y=5, sweep=False, large_arc=False)
        self.add_line('neck-right', (32, 36), (32, 40))
        self.add_arc('base-right', (32, 40), (28, 42), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('base-bottom', (28, 42), (20, 42))
        self.add_arc('base-left', (20, 42), (16, 40), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('neck-left', (16, 40), (16, 36))
        self.add_arc('taper-left', (16, 36), (14, 32), radius_x=5, radius_y=5, sweep=False, large_arc=False)
        self.add_arc('shoulder-left', (14, 32), (8, 20), radius_x=15, radius_y=15, sweep=True, large_arc=False)
        self.add_contour('outline', 'dome', 'shoulder-right', 'taper-right', 'neck-right', 'base-right', 'base-bottom', 'base-left', 'neck-left', 'taper-left', 'shoulder-left', closed=True)
        self.add_line('base-seam', (16, 36), (32, 36))
        self.relate("connect", 'base-seam', 'outline')
