"""An upright fist grips a horizontal fountain pen whose pointed nib faces left. Four fingers curl across the barrel, the thumb folds below them, and the wrist descends from the hand.
Lucide pen-tool nib and hand/pointer knuckle construction. Three grouped knuckles replace four fingers; creases and nib slit omitted. Pointed nib remains left-facing.
SQUARE: centerline extremes (6,6)-(42,42); freshly authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '83ff3171-53c2-4300-a683-6306ba8fe250'
SOURCE_PATH = 'pictographic-primitives/work/workflow coaching hand pen_83ff3171-53c2-4300-a683-6306ba8fe250.svg'
AUTHOR = 'gpt-6'


class HandHoldingFountainPen(Solo48):
    icon_id = 'hand-holding-fountain-pen'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "work"
    aliases = ()
    keywords = ('hand', 'pen', 'fountain', 'writing', 'grip', 'nib')

    def build(self) -> None:
        self.add_polyline('nib', (6, 14), (14, 8), (18, 10), (18, 18), (14, 20), closed=True)
        self.add_polyline('left-hand', (24, 42), (24, 34), (18, 28), (18, 18), (18, 10), closed=False)
        self.add_arc('knuckle-18', (18, 10), (26, 10), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('knuckle-26', (26, 10), (34, 10), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('knuckle-34', (34, 10), (42, 10), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('palm-right', (42, 10), (42, 30))
        self.add_arc('palm-heel', (42, 30), (36, 36), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_line('wrist-right', (36, 36), (36, 42))
        self.relate("connect", 'left-hand', 'nib')
        self.relate("connect", 'left-hand', 'knuckle-18')
        self.relate("connect", 'knuckle-18', 'knuckle-26')
        self.relate("connect", 'knuckle-26', 'knuckle-34')
        self.relate("connect", 'knuckle-34', 'palm-right')
        self.relate("connect", 'palm-right', 'palm-heel')
        self.relate("connect", 'palm-heel', 'wrist-right')
        self.add_line('finger-26', (26, 10), (26, 18))
        self.relate("connect", 'finger-26', 'knuckle-26')
        self.relate("connect", 'finger-26', 'knuckle-18')
        self.add_line('finger-34', (34, 10), (34, 18))
        self.relate("connect", 'finger-34', 'knuckle-34')
        self.relate("connect", 'finger-34', 'knuckle-26')
