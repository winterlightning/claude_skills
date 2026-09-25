"""A lobed brain outline has a short angled stem at its lower right. A bent drinking straw descends through the open top to a wavy liquid line inside the brain.
Lucide brain lobed outline; physical straw and liquid retained, interior folds omitted. Deliberate asymmetric stem.
Keyshape SQUARE; centerline extremes (6,6)-(42,42). Square envelope balances the complete scene. Source inspected as a standalone physical or conceptual subject."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '27c05dd5-6a4f-5904-912f-06a8c4d4b149'
SOURCE_PATH = 'pictographic-primitives/work/creative juice brain_27c05dd5-6a4f-5904-912f-06a8c4d4b149.svg'
AUTHOR = 'gpt-6'


class BrainWithDrinkingStraw(Solo48):
    icon_id = 'brain-with-drinking-straw'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "work"
    aliases = ()
    keywords = ('brain', 'straw', 'drink', 'creativity', 'thinking', 'juice')

    def build(self) -> None:
        self.add_arc('lobe-upper', (22, 12), (14, 20), radius_x=8, radius_y=8, sweep=False, large_arc=False)
        self.add_arc('lobe-left', (14, 20), (6, 30), radius_x=8, radius_y=10, sweep=False, large_arc=False)
        self.add_arc('lobe-bottom-left', (6, 30), (17, 37), radius_x=11, radius_y=7, sweep=False, large_arc=False)
        self.add_arc('lobe-bottom', (17, 37), (28, 37), radius_x=7, radius_y=7, sweep=False, large_arc=False)
        self.add_line('stem-1', (28, 37), (37, 42))
        self.add_line('stem-2', (37, 42), (34, 34))
        self.add_arc('lobe-right', (34, 34), (40, 19), radius_x=10, radius_y=10, sweep=False, large_arc=False)
        self.add_arc('lobe-top-right', (40, 19), (40, 15), radius_x=7, radius_y=7, sweep=False, large_arc=False)
        self.add_contour('brain', 'lobe-upper', 'lobe-left', 'lobe-bottom-left', 'lobe-bottom', 'stem-1', 'stem-2', 'lobe-right', 'lobe-top-right', closed=False)
        self.add_polyline('straw', (42, 6), (32, 6), (28, 26), closed=False)
        self.add_arc('liquid', (18, 27), (28, 26), radius_x=10, radius_y=3, sweep=True, large_arc=False)
        self.relate("connect", 'liquid', 'straw')
