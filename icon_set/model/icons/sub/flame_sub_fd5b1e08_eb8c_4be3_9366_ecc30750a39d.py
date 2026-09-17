"""Flame: A flame has a rounded base, a tall curling upper tip, and a smaller pointed tongue beside a deep inward notch on the right. Generate this component alone; exclude Shield Frame.

Construction: A leaning high tip, a curved left flank and round base surround the source deep right notch; no interior flame is added.
Keyshape: VRECT_L; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'fd5b1e08-eb8c-4be3-9366-ecc30750a39d'
SOURCE_PATH = 'pictographic-primitives/state/shield with flame_fd5b1e08-eb8c-4be3-9366-ecc30750a39d.svg'
AUTHOR = 'gpt-6'


class FlameSub(Sub32):
    icon_id = 'flame-sub'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives/shape'
    aliases = ()
    keywords = ('flame', 'rounded', 'base', 'tall', 'curling', 'upper', 'tip', 'smaller')

    def build(self):
        self.add_arc('left-tip',(16,2),(12,12),radius_x=8,radius_y=10)
        self.add_arc('left-side',(12,12),(6,20),radius_x=6,radius_y=8,sweep=False)
        self.add_arc('left-base',(6,20),(16,30),radius_x=10,sweep=False)
        self.add_arc('right-base',(16,30),(26,20),radius_x=10,sweep=False)
        self.add_line('right-point',(26,20),(26,14))
        self.add_arc('notch',(26,14),(18,18),radius_x=8,radius_y=4)
        self.add_arc('right-upper',(18,18),(16,2),radius_x=4,radius_y=12,sweep=False)
        self.add_contour('flame','left-tip','left-side','left-base','right-base','right-point','notch','right-upper',closed=True)
