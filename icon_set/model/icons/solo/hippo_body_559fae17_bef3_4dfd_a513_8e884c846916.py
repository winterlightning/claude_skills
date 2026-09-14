"""Left-facing hippo with barrel body, rounded muzzle, pricked ear and two broad visible legs; smile omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '559fae17-bef3-4dfd-a513-8e884c846916'
SOURCE_PATH = 'pictographic-primitives/animals/hippo body_559fae17-bef3-4dfd-a513-8e884c846916.svg'
AUTHOR = 'gpt-6'


class StandingHippo(Solo48):
    icon_id = 'standing-hippo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('hippo', 'hippopotamus', 'standing', 'body', 'animal', 'zoo', 'river', 'wildlife')

    def build(self) -> None:
        # Keyshape ink extremes: (0, 6, 48, 42); centerlines inset by stroke radius 2.
        self.add_arc('body-1', (6, 21), (9, 14), radius_x=7, radius_y=7, sweep=True)
        self.add_line('body-2', (9, 14), (17, 14))
        self.add_line('body-3', (17, 14), (20, 8))
        self.add_line('body-4', (20, 8), (24, 14))
        self.add_line('body-5', (24, 14), (34, 14))
        self.add_arc('body-6', (34, 14), (42, 26), radius_x=12, radius_y=12, sweep=True)
        self.add_line('body-7', (42, 26), (42, 40))
        self.add_line('body-8', (42, 40), (37, 40))
        self.add_line('body-9', (37, 40), (37, 32))
        self.add_line('body-10', (37, 32), (23, 32))
        self.add_line('body-11', (23, 32), (23, 40))
        self.add_line('body-12', (23, 40), (14, 40))
        self.add_line('body-13', (14, 40), (14, 32))
        self.add_arc('body-14', (14, 32), (9, 29), radius_x=5, radius_y=5, sweep=False)
        self.add_line('body-15', (9, 29), (6, 29))
        self.add_line('body-16', (6, 29), (6, 21))
        self.add_contour('body', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', 'body-8', 'body-9', 'body-10', 'body-11', 'body-12', 'body-13', 'body-14', 'body-15', 'body-16', closed=True)
