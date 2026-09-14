# Bounds-only review variant; parent preserved.
"""Move every authored point down by 2 units together. Keep dimensions, arcs, shared endpoints and spacing unchanged. VRECT_L centerline box (8,4)-(40,44), ink (6,2)-(42,46)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0fcbdb00-a505-4fa6-95a8-0fa24ac7895a'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird vulture_0fcbdb00-a505-4fa6-95a8-0fa24ac7895a.svg'
AUTHOR = 'gpt-6'

class VultureVariant3(Solo48):
    icon_id = 'vulture-v3'
    variant_of = 'vulture'
    variant_label = 'Exact keyshape bounds'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals/birds'
    aliases = ()
    keywords = ('vulture', 'scavenger', 'bird', 'neck', 'beak', 'standing', 'carrion', 'wildlife')

    def build(self) -> None:
        self.add_arc('head', (26, 11), (40, 11), radius_x=7, radius_y=7, sweep=True)
        self.add_line('beak', (40, 11), (40, 17))
        self.add_line('chin', (40, 17), (32, 17))
        self.add_line('neck', (32, 17), (32, 23))
        self.add_arc('throat', (32, 23), (25, 30), radius_x=7, radius_y=7, sweep=True)
        self.add_arc('shoulder', (25, 30), (18, 18), radius_x=10, radius_y=10, sweep=False)
        self.add_arc('wing-back', (18, 18), (8, 42), radius_x=40, radius_y=40, sweep=False)
        self.add_line('wing-tip', (8, 42), (23, 36))
        self.add_arc('wing-front', (23, 36), (25, 30), radius_x=10, radius_y=10, sweep=False)
        self.add_contour('wing', 'shoulder', 'wing-back', 'wing-tip', 'wing-front', closed=True)
        self.add_line('nape', (26, 11), (26, 19))
        self.add_contour('neck-head', 'nape', closed=False)
        self.add_contour('head-neck', 'head', 'beak', 'chin', 'neck', 'throat', closed=False)
        self.relate('connect', 'head-neck', 'wing')
        self.add_line('foot-leg', (23, 36), (26, 44))
        self.add_line('foot', (26, 44), (34, 44))
        self.add_contour('leg', 'foot-leg', 'foot', closed=False)
        self.relate('connect', 'wing', 'leg')
