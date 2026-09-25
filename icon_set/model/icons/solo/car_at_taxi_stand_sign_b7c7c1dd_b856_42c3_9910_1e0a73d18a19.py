"""car-at-taxi-stand-sign: reconstructed on SOLO48 from its reference."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b7c7c1dd-b856-42c3-9910-1e0a73d18a19'
SOURCE_PATH = 'pictographic-primitives/transportation/taxi station_b7c7c1dd-b856-42c3-9910-1e0a73d18a19.svg'
AUTHOR = 'gpt-6'

class CarAtTaxiStandSign(Solo48):
    icon_id = 'car-at-taxi-stand-sign'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('taxi stand', 'taxi rank', 'taxi station', 'car', 'sign', 'pick up', 'parking', 'transport')

    def build(self) -> None:
        self.add_polyline('sign', (6, 6), (14, 6), (14, 18), (10, 18), (6, 18), closed=True)
        self.add_line('post', (10, 18), (10, 42))
        self.add_polyline('car', (22, 26), (26, 18), (38, 18), (42, 26), (42, 34), (38, 34), (26, 34), (22, 34), closed=True)
        self.add_line('windscreen', (22, 26), (42, 26))
        self.add_line('tyre-left', (26, 34), (26, 42))
        self.add_line('tyre-right', (38, 34), (38, 42))
        self.add_polyline('ground', (6, 42), (10, 42), (26, 42), (38, 42), (42, 42))
        for i, a in enumerate(self.primitives):
            for b in self.primitives[i + 1:]:
                if a.start in (b.start, b.end) or a.end in (b.start, b.end):
                    self.relate('connect', a.element_id, b.element_id)
