"""A tapered food cover with an arched handle and a shallow serving tray.

VRECT_XL preserves the tall cover: ink (4,0)-(60,64), centerline (6,2)-(58,62).
Reference: supplied failed SVG; Lucide concierge-bell original and atomic-debug
informed the handle, cover and tray hierarchy. The tray rim now supplies the
shared edge once; the duplicate cover bottom was removed. The subject remains
symmetric about x=32, with all identifying parts retained.

Hosting (compose.py): heart, check valid; plus blocked.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = 'restaurant-food-cloche'
SOURCE_PATH = 'icon_set/dist/failed/container64/restaurant-food-cloche.svg'
AUTHOR = 'gpt-6'


class RestaurantFoodCloche(Container64):
    icon_id = 'restaurant-food-cloche'
    keyshape = Keyshape.VRECT_XL
    aliases = ('serving-cloche', 'food-cover')
    keywords = ('restaurant', 'food', 'cloche')

    def build(self) -> None:
        # Plan: symmetric open dome and handle join one shared tray rim.
        axis, handle_radius, shoulder_radius = 32, 10, 8
        crown_y, shoulder_y, rim_y, bottom_y = 12, 20, 52, 62
        handle_left, handle_right = (axis - handle_radius, crown_y), (axis + handle_radius, crown_y)
        rim_left, rim_right = (axis - 24, rim_y), (axis + 24, rim_y)
        self.add_arc('handle', handle_left, handle_right, radius_x=handle_radius)
        self.add_line('cover-top-right', (axis + 12, crown_y), handle_right)
        self.add_line('cover-top-middle', handle_right, handle_left)
        self.add_line('cover-top-left', handle_left, (axis - 12, crown_y))
        self.add_arc('shoulder-right', (axis + 20, shoulder_y), (axis + 12, crown_y), radius_x=shoulder_radius, sweep=False)
        self.add_line('side-right', rim_right, (axis + 20, shoulder_y))
        self.add_line('side-left', (axis - 20, shoulder_y), rim_left)
        self.add_arc('shoulder-left', (axis - 12, crown_y), (axis - 20, shoulder_y), radius_x=shoulder_radius, sweep=False)
        self.add_contour('cover', 'side-right', 'shoulder-right', 'cover-top-right', 'cover-top-middle', 'cover-top-left', 'shoulder-left', 'side-left')
        self.relate('connect', 'handle', 'cover')
        self.add_line('tray-top-left', (axis - 26, rim_y), rim_left)
        self.add_line('tray-top-middle', rim_left, rim_right)
        self.add_line('tray-top-right', rim_right, (axis + 26, rim_y))
        self.add_line('tray-r', (axis + 26, rim_y), (axis + 26, bottom_y - 6))
        self.add_arc('tray-br', (axis + 26, bottom_y - 6), (axis + 20, bottom_y), radius_x=6)
        self.add_line('tray-bottom', (axis + 20, bottom_y), (axis - 20, bottom_y))
        self.add_arc('tray-bl', (axis - 20, bottom_y), (axis - 26, bottom_y - 6), radius_x=6)
        self.add_line('tray-l', (axis - 26, bottom_y - 6), (axis - 26, rim_y))
        self.add_contour('tray', 'tray-top-left', 'tray-top-middle', 'tray-top-right', 'tray-r', 'tray-br', 'tray-bottom', 'tray-bl', 'tray-l', closed=True)
        self.relate('connect', 'cover', 'tray')
