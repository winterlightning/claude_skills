"""Left-facing round baby chick, crown tuft and folded wing. Lucide bird informs circular body and attached legs; asymmetry retains the raised tail."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3f1a2fcc-b8bd-5d0d-8a3f-ff4bd2741fbf'
SOURCE_PATH = 'pictographic-primitives/animals/chick_3f1a2fcc-b8bd-5d0d-8a3f-ff4bd2741fbf.svg'
AUTHOR = 'gpt-6'


class BabyChick(Solo48):
    icon_id = 'baby-chick'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/animals"
    aliases = ()
    keywords = ('chick', 'chicken', 'bird', 'baby', 'hatch', 'farm', 'easter', 'poultry')

    def build(self) -> None:
        # SQUARE centerline extremes recorded in batch-02-review.md.
        self.add_arc('crown', (8, 18), (26, 6), radius_x=18, radius_y=16, sweep=True)
        self.add_arc('back', (26, 6), (34, 18), radius_x=10, radius_y=12, sweep=True)
        self.add_arc('tail-dip', (34, 18), (46, 22), radius_x=8, radius_y=8, sweep=False)
        self.add_line('tail-tip', (46, 22), (46, 26))
        self.add_arc('body-right', (46, 26), (30, 42), radius_x=16, radius_y=16, sweep=True)
        self.add_line('belly', (30, 42), (24, 42))
        self.add_arc('body-left', (24, 42), (8, 26), radius_x=16, radius_y=16, sweep=True)
        self.add_line('beak-1', (8, 26), (2, 22))
        self.add_line('beak-2', (2, 22), (8, 18))
        self.add_contour('outline', 'crown', 'back', 'tail-dip', 'tail-tip', 'body-right', 'belly', 'body-left', 'beak-1', 'beak-2', closed=True)
        self.add_line('tuft', (26, 6), (22, 2))
        self.relate("connect", 'tuft', 'outline')
        self.add_arc('wing', (23, 23), (33, 31), radius_x=8, radius_y=8, sweep=False)
        self.add_line('leg-left', (24, 42), (20, 46))
        self.add_line('leg-right', (30, 42), (34, 46))
        self.relate("connect", 'outline', 'leg-left')
        self.relate("connect", 'outline', 'leg-right')
