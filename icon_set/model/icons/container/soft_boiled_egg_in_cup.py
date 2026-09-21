"""Widen the egg crown and lower the cup rim while retaining an egg-shaped top.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse
SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'gpt-6'

class SoftBoiledEggInCup(Container64):
    icon_id = 'soft-boiled-egg-in-cup'
    keyshape = Keyshape.VRECT_XL
    aliases = ()
    keywords = ()

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate("connect",a,b)
        self.add_arc('egg-crown',(6,50),(58,50),radius_x=26,radius_y=48)
        line('cup-rim',(6,50),(58,50));self.add_arc('cup-bowl',(58,50),(6,50),radius_x=26,radius_y=12)
        join('egg-crown','cup-rim');join('cup-bowl','cup-rim')
