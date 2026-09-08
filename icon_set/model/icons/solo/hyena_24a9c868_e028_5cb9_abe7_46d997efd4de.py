"""Standing hyena; centerline extremes (2,8)-(46,40). High shoulders, low rump and pointed ear retained; far legs and face details omitted for clearance."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '24a9c868-e028-5cb9-abe7-46d997efd4de'
SOURCE_PATH = 'pictographic-primitives/animals/hyena_24a9c868-e028-5cb9-abe7-46d997efd4de.svg'
AUTHOR = 'gpt-6'


class StandingHyena(Solo48):
    icon_id = 'standing-hyena'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('hyena', 'standing', 'body', 'profile', 'animal', 'wildlife', 'africa', 'scavenger')

    def build(self) -> None:
        # Standing hyena; centerline extremes (2,8)-(46,40). High shoulders, low rump and pointed ear retained; far legs and face details omitted for clearance.
        self.add_arc('rump', (6, 28), (16, 19), radius_x=10, radius_y=10, sweep=True)
        self.add_line('back', (16, 19), (31, 14))
        self.add_arc('chest', (36, 26), (32, 34), radius_x=10, radius_y=10, sweep=False)
        self.add_arc('belly', (25, 30), (13, 30), radius_x=16, radius_y=16, sweep=True)
        self.add_line('ear-muzzle-1', (31, 14), (33, 8))
        self.add_line('ear-muzzle-2', (33, 8), (37, 16))
        self.add_line('ear-muzzle-3', (37, 16), (46, 21))
        self.add_line('ear-muzzle-4', (46, 21), (43, 27))
        self.add_line('ear-muzzle-5', (43, 27), (36, 26))
        self.add_line('front-leg-1', (32, 34), (32, 40))
        self.add_line('front-leg-2', (32, 40), (25, 40))
        self.add_line('front-leg-3', (25, 40), (25, 30))
        self.add_line('hind-leg-1', (13, 30), (12, 40))
        self.add_line('hind-leg-2', (12, 40), (6, 40))
        self.add_line('hind-leg-3', (6, 40), (6, 28))
        self.add_contour('body', 'rump', 'back', 'ear-muzzle-1', 'ear-muzzle-2', 'ear-muzzle-3', 'ear-muzzle-4', 'ear-muzzle-5', 'chest', 'front-leg-1', 'front-leg-2', 'front-leg-3', 'belly', 'hind-leg-1', 'hind-leg-2', 'hind-leg-3', closed=True)
        self.add_arc('tail', (6, 28), (2, 34), radius_x=8, radius_y=8, sweep=False)
        self.relate("connect", 'body', 'tail')
