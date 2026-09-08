"""An upright egg held in a shallow rounded cup. The rim is simplified to a single horizontal lip.

Keyshape: VRECT_XL; centerline extremes recorded in build.
Construction reference: Lucide egg: a mirrored rounded crown; reauthored as an ellipse with an enclosing bowl.. Mirrored about x=32.
Hosting measured with compose.py: plus valid, heart valid, check valid.
"""
from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class SoftBoiledEggInCup(Container64):
    icon_id = 'soft-boiled-egg-in-cup'
    keyshape = Keyshape.VRECT_XL
    aliases = ()
    keywords = ('soft', 'boiled', 'egg', 'in', 'cup')

    def build(self) -> None:
        # Centerline (6,2)-(58,62).
        self.add_arc('egg-crown',(12,42),(52,42),radius_x=20,radius_y=40)
        self.add_line('cup-rim',(6,42),(58,42))
        self.add_arc('cup-bowl',(58,42),(6,42),radius_x=26,radius_y=20)
        self.relate('connect','egg-crown','cup-rim')
        self.relate('connect','cup-bowl','cup-rim')
