"""A tapered food cover with an arched handle and a shallow serving tray.

Keyshape VRECT_XL: (4, 0, 60, 64); preserves the reference proportions.
Reference: batch_11 source render; Lucide concierge-bell informs the handle-cover-tray hierarchy.
Authored on the shared vertical axis except for directional subjects.
No decorative details added; all identifying source parts retained.
Hosting: plus does not clear, heart passes, check passes.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class RestaurantFoodCloche(Container64):
    icon_id = 'restaurant-food-cloche'
    keyshape = Keyshape.VRECT_XL
    aliases = ('serving-cloche', 'food-cover')
    keywords = ('restaurant', 'food', 'cloche')

    def build(self) -> None:
        self.add_arc('handle', (22, 12), (42, 12), radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_line('cover-top', (20, 12), (44, 12))
        self.add_arc('shoulder-right', (44, 12), (52, 20), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_line('side-right', (52, 20), (56, 52))
        self.add_line('cover-bottom', (56, 52), (8, 52))
        self.add_line('side-left', (8, 52), (12, 20))
        self.add_arc('shoulder-left', (12, 20), (20, 12), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_contour('cover', 'cover-top', 'shoulder-right', 'side-right', 'cover-bottom', 'side-left', 'shoulder-left', closed=True)
        self.relate("connect", 'handle', 'cover')
        self.add_line('tray-top', (6, 52), (58, 52))
        self.add_line('tray-r', (58, 52), (58, 56))
        self.add_arc('tray-br', (58, 56), (52, 62), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_line('tray-bottom', (52, 62), (12, 62))
        self.add_arc('tray-bl', (12, 62), (6, 56), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_line('tray-l', (6, 56), (6, 52))
        self.add_contour('tray', 'tray-top', 'tray-r', 'tray-br', 'tray-bottom', 'tray-bl', 'tray-l', closed=True)
        self.relate("connect", 'cover', 'tray')
