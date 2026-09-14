"""Rounded mirrored fists with curled thumbs and one impact mark. HRECT_L fits the horizontal gesture. Fine finger creases omitted.
Lucide hand, crown and user/laptop construction; independently revised on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7eb37a5d-4cd8-4996-8500-94d9331cc88f'
SOURCE_PATH = 'pictographic-primitives/work/workflow teamwork fistbump_7eb37a5d-4cd8-4996-8500-94d9331cc88f.svg'
AUTHOR = 'gpt-6'

class FistBumpVariant2(Solo48):
    icon_id = 'fist-bump-v2'
    variant_of = 'fist-bump'
    variant_label = 'Cleaner silhouette and spacing'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/work'
    aliases = ()
    keywords = ('fist', 'bump', 'hands', 'greeting', 'teamwork', 'contact')

    def build(self) -> None:
        self.add_line('left-top', (4, 20), (14, 20))
        self.add_arc('left-knuckles', (14, 20), (14, 40), radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_arc('left-thumb-curl', (14, 40), (4, 30), radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_line('left-thumb-tip', (4, 30), (12, 30))
        self.add_contour('left-hand', 'left-top', 'left-knuckles', 'left-thumb-curl', 'left-thumb-tip', closed=False)
        self.add_line('left-wrist', (4, 40), (14, 40))
        self.relate("connect", 'left-hand', 'left-wrist')
        self.add_line('right-top', (44, 20), (34, 20))
        self.add_arc('right-knuckles', (34, 20), (34, 40), radius_x=10, radius_y=10, sweep=False, large_arc=False)
        self.add_arc('right-thumb-curl', (34, 40), (44, 30), radius_x=10, radius_y=10, sweep=False, large_arc=False)
        self.add_line('right-thumb-tip', (44, 30), (36, 30))
        self.add_contour('right-hand', 'right-top', 'right-knuckles', 'right-thumb-curl', 'right-thumb-tip', closed=False)
        self.add_line('right-wrist', (44, 40), (34, 40))
        self.relate("connect", 'right-hand', 'right-wrist')
        self.relate("connect", 'left-hand', 'right-hand')
        self.add_line('impact', (24, 8), (24, 10))
