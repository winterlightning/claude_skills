"""Curled silhouette, muzzle and two stripes in a broad tail. No useful local raccoon match; circular construction re-authored from the supplied image. Four stripes reduced to two."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'dcf6e72c-8224-5fad-bb7d-737e07df48dd'
SOURCE_PATH = 'pictographic-primitives/animals/raccoon_dcf6e72c-8224-5fad-bb7d-737e07df48dd.svg'
AUTHOR = 'gpt-6'

class CurledRaccoon(Solo48):
    icon_id = 'curled-raccoon'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('raccoon', 'curled', 'tail', 'stripes', 'mask', 'animal', 'wildlife', 'nocturnal')

    def build(self) -> None:
        self.add_line('nose-top', (6, 14), (10, 14))
        self.add_arc('forehead', (10, 14), (24, 6), radius_x=14, radius_y=8)
        self.add_arc('back', (24, 6), (42, 24), radius_x=18)
        self.add_arc('tail-outer', (42, 24), (24, 42), radius_x=18)
        self.add_line('tail-base', (24, 42), (14, 42))
        self.add_arc('tail-round', (14, 42), (6, 34), radius_x=8)
        self.add_line('tail-tip-rise', (6, 34), (6, 28))
        self.add_line('tail-tip', (6, 28), (10, 28))
        self.add_line('tail-inner-left', (10, 28), (16, 32))
        self.add_line('tail-inner-mid', (16, 32), (24, 34))
        self.add_arc('tail-inner-turn', (24, 34), (34, 24), radius_x=10, sweep=False)
        self.add_contour('outline', 'nose-top', 'forehead', 'back', 'tail-outer', 'tail-base', 'tail-round', 'tail-tip-rise', 'tail-tip', 'tail-inner-left', 'tail-inner-mid', 'tail-inner-turn')
        self.add_line('nose-front', (6, 14), (6, 19))
        self.add_arc('muzzle', (6, 19), (12, 25), radius_x=6, sweep=False)
        self.add_line('cheek', (12, 25), (22, 25))
        self.add_contour('face', 'nose-front', 'muzzle', 'cheek')
        self.relate('connect', 'face', 'outline')
        self.add_line('ear', (24, 6), (24, 10))
        self.relate('connect', 'ear', 'outline')
        self.add_line('stripe-one', (14, 42), (16, 32))
        self.add_line('stripe-two', (24, 42), (24, 34))
        self.relate('connect', 'stripe-one', 'outline')
        self.relate('connect', 'stripe-two', 'outline')
        self.add_dot('eye', (18, 16))
