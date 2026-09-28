"""truck-tall-cab: reconstructed on SOLO48 from the supplied transportation reference."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6e8fe73c-8e53-54a3-b333-d7a046bafd5f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__truck-tall-cab/20260927T032022Z-thuan-mac-1/reference/truck empty_6e8fe73c-8e53-54a3-b333-d7a046bafd5f.svg'
AUTHOR = 'gpt-6'


class TruckTallCab(Solo48):
    icon_id = 'truck-tall-cab'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    categories = ("transportation", "primitives")
    aliases = ()
    keywords = ('truck', 'lorry', 'delivery', 'cargo', 'empty truck', 'logistics', 'transport', 'vehicle')

    def build(self) -> None:
        # The chassis stops at the wheel circles, so their outlines stay clear.
        self.add_polyline('cargo', (4, 36), (4, 8), (26, 8), (26, 14))
        self.add_polyline('cab', (26, 14), (36, 14), (44, 28), (44, 36))
        self.add_line('cargo-divider', (26, 14), (26, 28))
        self.add_line('chassis-left', (4, 36), (12, 36))
        self.add_line('chassis-middle', (20, 36), (28, 36))
        self.add_line('chassis-right', (36, 36), (44, 36))
        for side, x in (('rear', 16), ('front', 32)):
            self.add_arc(side+'-upper', (x-4, 36), (x+4, 36), radius_x=4, sweep=True)
            self.add_arc(side+'-lower', (x+4, 36), (x-4, 36), radius_x=4, sweep=True)
            self.add_contour(side+'-wheel', side+'-upper', side+'-lower', closed=True)
        for a, b in (
            ('cargo', 'cab'), ('cargo', 'cargo-divider'),
            ('cargo', 'chassis-left'), ('cab', 'chassis-right'),
            ('chassis-left', 'rear-wheel'), ('chassis-middle', 'rear-wheel'),
            ('chassis-middle', 'front-wheel'), ('chassis-right', 'front-wheel'),
        ):
            self.relate('connect', a, b)
