"""A car seat with a smooth continuous back and rounded cushion. Repaired in place from bad-stroke feedback."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a0d65c65-f181-4b40-b0ec-6cdf61983966'
SOURCE_PATH = 'pictographic-primitives/symbol/seat car_a0d65c65-f181-4b40-b0ec-6cdf61983966.svg'
AUTHOR = 'gpt-6'


class CarSeat(Solo48):
    icon_id = 'car-seat'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol",)
    aliases = ()
    keywords = ('seat', 'car-seat', 'chair', 'vehicle', 'interior', 'passenger', 'driver', 'automotive')

    def build(self) -> None:
        # One upholstery contour: paired vertical back walls, tangent quarter
        # ellipses at the seat, and a semicircular cushion nose (Lucide armchair).
        # SQUARE centerline extremes: (6, 6)-(42, 42).
        self.add_arc('back-top', (6, 10), (14, 10), radius_x=4)
        self.add_line('back-inner', (14, 10), (14, 22))
        self.add_arc('seat-transition', (14, 22), (28, 34),
                     radius_x=14, radius_y=12, sweep=False)
        self.add_line('cushion-top', (28, 34), (38, 34))
        self.add_arc('cushion-front', (38, 34), (38, 42), radius_x=4)
        self.add_line('cushion-bottom', (38, 42), (26, 42))
        self.add_arc('back-bottom', (26, 42), (6, 22), radius_x=20)
        self.add_line('back-outer', (6, 22), (6, 10))
        self.add_contour('seat', 'back-top', 'back-inner', 'seat-transition',
                         'cushion-top', 'cushion-front', 'cushion-bottom',
                         'back-bottom', 'back-outer', closed=True)
