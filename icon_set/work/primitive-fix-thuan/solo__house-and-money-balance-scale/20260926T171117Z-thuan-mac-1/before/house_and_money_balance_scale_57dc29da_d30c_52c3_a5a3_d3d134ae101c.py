"""House and Money Balance Scale. Tilted scale balances a circular coin against a house. Omit the tiny currency mark and house door; retain the coin, house and unequal beam height that communicate property value. Deliberate imbalance.
Keyshape SQUARE, visible extremes (4, 4, 44, 44); centerline envelope inset by 2.
Construction: Lucide scale: central upright and suspended loads; house: pitched-roof outline. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '57dc29da-d30c-52c3-a5a3-d3d134ae101c'
SOURCE_PATH = 'pictographic-primitives/real-estate/real estate market scale_57dc29da-d30c-52c3-a5a3-d3d134ae101c.svg'
AUTHOR = 'gpt-6'


class HouseAndMoneyBalanceScale(Solo48):
    icon_id = 'house-and-money-balance-scale'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "real-estate"
    categories = ("real-estate", "primitives")
    aliases = ()
    keywords = ('house', 'and', 'money', 'balance', 'scale')

    def build(self) -> None:
        self.add_line('beam-1', (6, 14), (24, 10))
        self.add_line('beam-2', (24, 10), (42, 6))
        self.add_contour('beam', 'beam-1', 'beam-2', closed=False)
        self.add_line('upright', (24, 10), (24, 42))
        self.add_line('base-1', (16, 42), (24, 42))
        self.add_line('base-2', (24, 42), (32, 42))
        self.add_contour('base', 'base-1', 'base-2', closed=False)
        self.relate("connect", 'beam', 'upright')
        self.relate("connect", 'base', 'upright')
        self.add_line('coin-hanger', (6, 14), (10, 25))
        self.relate("connect", 'beam', 'coin-hanger')
        self.add_arc('coin-ne', (10, 25), (14, 29), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('coin-se', (14, 29), (10, 33), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('coin-sw', (10, 33), (6, 29), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('coin-nw', (6, 29), (10, 25), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('coin', 'coin-ne', 'coin-se', 'coin-sw', 'coin-nw', closed=True)
        self.relate("connect", 'coin', 'coin-hanger')
        self.add_line('house-hanger', (42, 6), (37, 20))
        self.relate("connect", 'beam', 'house-hanger')
        self.add_line('house-1', (37, 20), (42, 25))
        self.add_line('house-2', (42, 25), (42, 34))
        self.add_line('house-3', (42, 34), (32, 34))
        self.add_line('house-4', (32, 34), (32, 25))
        self.add_line('house-5', (32, 25), (37, 20))
        self.add_contour('house', 'house-1', 'house-2', 'house-3', 'house-4', 'house-5', closed=True)
        self.relate("connect", 'house', 'house-hanger')
