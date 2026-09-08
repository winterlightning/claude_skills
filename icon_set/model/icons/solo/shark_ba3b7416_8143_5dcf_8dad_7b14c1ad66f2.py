from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ba3b7416-8143-5dcf-8dad-7b14c1ad66f2'
SOURCE_PATH = 'pictographic-primitives/animals/shark_ba3b7416-8143-5dcf-8dad-7b14c1ad66f2.svg'
AUTHOR = 'gpt-6'


class SimpleShark(Solo48):
    icon_id = 'simple-shark'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/marine"
    aliases = ()
    keywords = ('shark', 'fish', 'fin', 'sea', 'ocean', 'predator', 'swim', 'marine')

    def build(self) -> None:
        self.add_line('upper-tail-1', (10, 22), (2, 14))
        self.add_line('upper-tail-2', (2, 14), (5, 24))
        self.add_line('upper-tail-3', (5, 24), (2, 34))
        self.add_line('upper-tail-4', (2, 34), (10, 28))
        self.add_line('upper-tail-5', (10, 28), (24, 32))
        self.add_line('upper-tail-6', (24, 32), (24, 40))
        self.add_line('upper-tail-7', (24, 40), (33, 33))
        self.add_arc('jaw', (33, 33), (46, 25), radius_x=13, radius_y=8, sweep=False, large_arc=False)
        self.add_arc('nose', (46, 25), (30, 17), radius_x=16, radius_y=8, sweep=False, large_arc=False)
        self.add_line('fin-1', (30, 17), (21, 8))
        self.add_line('fin-2', (21, 8), (21, 18))
        self.add_line('fin-3', (21, 18), (10, 22))
        self.add_contour('outline', 'upper-tail-1', 'upper-tail-2', 'upper-tail-3', 'upper-tail-4', 'upper-tail-5', 'upper-tail-6', 'upper-tail-7', 'jaw', 'nose', 'fin-1', 'fin-2', 'fin-3', closed=True)
        self.add_arc('gill', (34, 24), (34, 26), radius_x=4, radius_y=4, sweep=False, large_arc=False)
