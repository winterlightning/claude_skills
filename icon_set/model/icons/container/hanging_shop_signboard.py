"""A rectangular shop sign hung from a beam with a right-hand post.

HRECT_XL: visible (0, 4, 64, 60); centerline (2, 6)-(62, 58).
Reference: batch_05 source render. Lucide signpost attached support and smartphone quarter-circle enclosure construction..
Right-hand post deliberately preserves the asymmetrical source structure.
Hosting measured with compose.py: plus: pass; heart: does not clear; check: does not clear.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class HangingShopSignboard(Container64):
    icon_id = "hanging-shop-signboard"
    keyshape = Keyshape.HRECT_XL
    aliases = ()
    keywords = ('hanging', 'shop', 'signboard')

    def build(self) -> None:
        self.add_line('panel-0', (5, 18), (49, 18))
        self.add_arc('panel-1', (49, 18), (52, 21), radius_x=3, sweep=True)
        self.add_line('panel-2', (52, 21), (52, 47))
        self.add_arc('panel-3', (52, 47), (49, 50), radius_x=3, sweep=True)
        self.add_line('panel-4', (49, 50), (5, 50))
        self.add_arc('panel-5', (5, 50), (2, 47), radius_x=3, sweep=True)
        self.add_line('panel-6', (2, 47), (2, 21))
        self.add_arc('panel-7', (2, 21), (5, 18), radius_x=3, sweep=True)
        self.add_contour('panel', 'panel-0', 'panel-1', 'panel-2', 'panel-3', 'panel-4', 'panel-5', 'panel-6', 'panel-7', closed=True)
        self.add_line('beam', (2, 6), (56, 6))
        self.add_arc('post-corner', (56, 6), (62, 12), radius_x=6, sweep=True)
        self.add_line('post', (62, 12), (62, 58))
        self.add_contour('support', 'beam', 'post-corner', 'post', closed=False)
        self.add_line('hanger-left', (12, 6), (12, 18))
        self.add_line('hanger-right', (44, 6), (44, 18))
        self.relate("connect", 'support', 'hanger-left')
        self.relate("connect", 'support', 'hanger-right')
        self.relate("connect", 'panel', 'hanger-left')
        self.relate("connect", 'panel', 'hanger-right')
