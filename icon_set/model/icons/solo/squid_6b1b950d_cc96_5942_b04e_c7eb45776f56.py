'squid: Widened the mantle and separated all four arm roots. Keyshape SQUARE; SOLO48 stroke 4. Reviewed at 48 px in both themes.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6b1b950d-cc96-5942-b04e-c7eb45776f56'
SOURCE_PATH = 'pictographic-primitives/animals/squid_6b1b950d-cc96-5942-b04e-c7eb45776f56.svg'
AUTHOR = 'gpt-6'

class Squid(Solo48):
    icon_id = 'squid'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('squid', 'tentacles', 'sea', 'ocean', 'marine', 'cephalopod', 'fins', 'calamari')

    def build(self) -> None:
        self.add_line('mantle-left', (10, 28), (10, 20))
        self.add_arc('fin-left', (10, 20), (6, 16), radius_x=4, sweep=True)
        self.add_arc('point-left', (6, 16), (24, 6), radius_x=32, sweep=True)
        self.add_arc('point-right', (24, 6), (42, 16), radius_x=32, sweep=True)
        self.add_arc('fin-right', (42, 16), (38, 20), radius_x=4, sweep=True)
        self.add_line('mantle-right', (38, 20), (38, 28))
        self.add_contour('mantle', 'mantle-left', 'fin-left', 'point-left', 'point-right', 'fin-right', 'mantle-right')
        self.add_line('collar', (10, 28), (38, 28))
        self.relate('connect', 'mantle', 'collar')
        for side in (-1, 1):
            p = lambda x, y: (24 + side * x, y)
            tag = 'left' if side < 0 else 'right'
            self.add_arc(tag + '-outer-arm', p(14, 28), p(18, 38), radius_x=4, radius_y=10, sweep=side < 0)
            self.relate('connect', tag + '-outer-arm', 'mantle')
            self.relate('connect', tag + '-outer-arm', 'collar')
            self.add_line(tag + '-inner-root', p(4, 28), p(4, 38))
            self.add_arc(tag + '-inner-curl', p(4, 38), p(10, 42), radius_x=8, sweep=side < 0)
            self.add_contour(tag + '-inner-arm', tag + '-inner-root', tag + '-inner-curl')
            self.relate('connect', tag + '-inner-arm', 'collar')
