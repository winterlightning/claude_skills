"""Left-facing farm cow with a sloping muzzle, curved belly and single-stroke legs. Four overlapping legs reduced to two and tail tuft omitted. No useful exact Lucide match; directional asymmetry retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a0220f3e-39f2-4fe3-a929-e532120865b6'
SOURCE_PATH = 'pictographic-primitives/animals/cattle_a0220f3e-39f2-4fe3-a929-e532120865b6.svg'
AUTHOR = 'gpt-6'


class StandingCow(Solo48):
    icon_id = 'standing-cow'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/animals"
    aliases = ()
    keywords = ('cow', 'cattle', 'farm', 'livestock', 'dairy', 'animal', 'bovine', 'standing')

    def build(self) -> None:
        # HRECT_L centerline extremes: (2,8)-(46,40).
        # Circular shoulder eases into the level back. Single-stroke legs
        # remove narrow internal slivers; the rear hock preserves the stance.
        self.add_line('horn-front', (10, 12), (9, 8))
        self.add_line('horn-back', (9, 8), (15, 12))
        self.add_arc('shoulder', (15, 12), (23, 14), radius_x=17, sweep=False)
        self.add_line('back', (23, 14), (38, 14))
        self.add_arc('rump', (38, 14), (42, 18), radius_x=4)
        self.add_line('rear', (42, 18), (42, 20))
        self.add_arc('haunch', (42, 20), (34, 28), radius_x=8)
        self.add_line('belly', (34, 28), (18, 28))
        self.add_arc('chest', (18, 28), (11, 24), radius_x=7, radius_y=4)
        self.add_line('throat', (11, 24), (8, 20))
        self.add_line('muzzle-bottom', (8, 20), (4, 21))
        self.add_arc('muzzle-tip', (4, 21), (2, 19), radius_x=2)
        self.add_line('face', (2, 19), (10, 12))
        self.add_contour(
            'outline', 'horn-front', 'horn-back', 'shoulder', 'back', 'rump',
            'rear', 'haunch', 'belly', 'chest', 'throat', 'muzzle-bottom',
            'muzzle-tip', 'face', closed=True,
        )
        self.add_line('front-leg', (18, 28), (18, 40))
        self.add_polyline('hind-leg', (34, 28), (38, 34), (38, 40))
        self.relate('connect', 'outline', 'front-leg')
        self.relate('connect', 'outline', 'hind-leg')
        self.add_arc('tail', (42, 18), (46, 30), radius_x=4, radius_y=12, sweep=False)
        self.relate('connect', 'outline', 'tail')
