"""Standing horse, left-facing; centerline extremes (6,6)-(42,42). Two profile legs and one tail retained; overlapping legs and tail strands omitted. No useful Lucide subject match."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3c4b5ee0-ba80-504c-8490-3598f2217ea8'
SOURCE_PATH = 'pictographic-primitives/animals/animal horse_3c4b5ee0-ba80-504c-8490-3598f2217ea8.svg'
AUTHOR = 'gpt-6'


class StandingHorse(Solo48):
    icon_id = 'standing-horse'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('horse', 'pony', 'stallion', 'equine', 'animal', 'farm', 'riding', 'profile')

    def build(self) -> None:
        # Standing horse, left-facing; centerline extremes (6,6)-(42,42). Two profile legs and one tail retained; overlapping legs and tail strands omitted. No useful Lucide subject match.
        self.add_polyline('head', (18, 6), (14, 12), (6, 17), (6, 22), (10, 25), (16, 22), (16, 31), (13, 42), closed=False)
        self.add_polyline('back-neck', (18, 6), (23, 20), (35, 20), closed=False)
        self.add_arc('rump', (35, 20), (40, 25), radius_x=5, radius_y=5, sweep=True)
        self.add_line('rear-leg', (40, 25), (39, 42))
        self.add_contour('rear', 'rump', 'rear-leg', closed=False)
        self.add_polyline('belly', (13, 42), (20, 42), (23, 32), (32, 32), (32, 42), (39, 42), closed=False)
        self.add_polyline('tail', (40, 25), (42, 28), (42, 36), closed=False)
        self.relate("connect", 'head', 'back-neck')
        self.relate("connect", 'back-neck', 'rear')
        self.relate("connect", 'head', 'belly')
        self.relate("connect", 'rear', 'belly')
        self.relate("connect", 'tail', 'rear')
