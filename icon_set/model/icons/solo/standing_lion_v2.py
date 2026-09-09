# Variant of standing-lion; parent file remains unchanged.
"""Standing lion with an offset muzzle inside a tall teardrop mane, larger rectangular legs and an upcurved tail. The mane is no longer a circular head or eye. Far legs omitted; deliberate left-facing asymmetry."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '48ee2f2f-fef8-43a6-b301-d910d4dce828'
SOURCE_PATH = 'pictographic-primitives/animals/lion body_48ee2f2f-fef8-43a6-b301-d910d4dce828.svg'
AUTHOR = 'gpt-6'

class StandingLionVariant2(Solo48):
    icon_id = 'standing-lion-v2'
    variant_of = 'standing-lion'
    variant_label = 'Larger rectangular legs'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('standing', 'lion', 'animal')

    def build(self) -> None:
        self.add_arc('mane-crown', (9, 13), (16, 5), radius_x=7, radius_y=8, sweep=True)
        self.add_arc('mane-right', (16, 5), (26, 17), radius_x=10, radius_y=12, sweep=True)
        self.add_line('mane-side', (26, 17), (26, 19))
        self.add_arc('mane-low', (26, 19), (15, 34), radius_x=11, radius_y=15, sweep=True)
        self.add_arc('mane-left', (15, 34), (7, 29), radius_x=8, radius_y=5, sweep=True)
        self.add_contour('mane', 'mane-crown', 'mane-right', 'mane-side', 'mane-low', 'mane-left', closed=False)
        self.add_line('snout-top', (2, 20), (4, 20))
        self.add_line('forehead', (4, 20), (9, 13))
        self.add_arc('face-top', (9, 13), (18, 21), radius_x=9, radius_y=8, sweep=True)
        self.add_arc('face-low', (18, 21), (12, 29), radius_x=6, radius_y=8, sweep=True)
        self.add_line('jaw', (12, 29), (7, 29))
        self.add_arc('nose-low', (7, 29), (2, 24), radius_x=5, radius_y=5, sweep=True)
        self.add_line('nose', (2, 24), (2, 20))
        self.add_contour('head', 'snout-top', 'forehead', 'face-top', 'face-low', 'jaw', 'nose-low', 'nose', closed=True)
        self.relate('connect', 'head', 'mane')
        self.add_dot('eye', (11, 21))
        self.add_line('back', (26, 19), (35, 19))
        self.add_arc('rump', (35, 19), (42, 26), radius_x=7, radius_y=7, sweep=True)
        self.add_line('hind-shin', (42, 26), (42, 43))
        self.add_line('hind-foot', (42, 43), (34, 43))
        self.add_line('hind-inner', (34, 43), (34, 31))
        self.add_line('belly', (34, 31), (26, 31))
        self.add_line('fore-inner', (26, 31), (26, 43))
        self.add_line('fore-foot', (26, 43), (18, 43))
        self.add_line('fore-shin', (18, 43), (18, 33))
        self.add_contour('body', 'back', 'rump', 'hind-shin', 'hind-foot', 'hind-inner', 'belly', 'fore-inner', 'fore-foot', 'fore-shin', closed=False)
        self.relate('connect', 'body', 'mane')
        self.add_arc('tail', (42, 26), (46, 12), radius_x=4, radius_y=14, sweep=False)
        self.relate('connect', 'tail', 'body')
