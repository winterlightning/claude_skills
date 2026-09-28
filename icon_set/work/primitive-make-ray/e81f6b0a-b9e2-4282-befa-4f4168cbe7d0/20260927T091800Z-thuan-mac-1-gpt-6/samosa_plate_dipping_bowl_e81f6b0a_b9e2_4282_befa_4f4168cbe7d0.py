"""Samosas on Plate with Dipping Bowl."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'e81f6b0a-b9e2-4282-befa-4f4168cbe7d0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__samosa-plate-dipping-bowl/20260927T091411Z-thuan-mac-1/reference/exotic food samosa_e81f6b0a-b9e2-4282-befa-4f4168cbe7d0.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'samosa-plate-dipping-bowl'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('samosa', 'plate', 'dipping', 'bowl')

    # Revision plan: The rejected drawing lost the second samosa. Restore the paired pastries above the plate, with the cup high at left. No useful Lucide food match.
    # Revision plan: The rejected drawing lost the second samosa. Restore the paired pastries above the plate, with the cup high at left. No useful Lucide food match.
    # Revision plan: The rejected drawing lost the second samosa. Restore the paired pastries above the plate, with the cup high at left. No useful Lucide food match.
    # Revision plan: The rejected drawing lost the second samosa. Restore the paired pastries above the plate, with the cup high at left. No useful Lucide food match.
    # Revision plan: The rejected drawing lost the second samosa. Restore the paired pastries above the plate, with the cup high at left. No useful Lucide food match.
    def build(self):
        # A broad plate under two pastries; cup sits at upper left as in source.
        self.add_arc('cup-rim', (5, 10), (17, 10), radius_x=6, radius_y=2, sweep=True)
        self.add_arc('cup-body', (17, 10), (5, 10), radius_x=6, radius_y=8, sweep=True)
        self.add_contour('cup', 'cup-rim', 'cup-body', closed=True)
        self.add_polyline('pastry-left', (18, 28), (25, 17), (32, 28), closed=True)
        self.add_polyline('pastry-right', (32, 28), (37, 17), (42, 28), closed=True)
        self.relate('connect', 'pastry-left', 'pastry-right')
        self.add_arc('plate', (4, 36), (44, 36), radius_x=20, radius_y=4, sweep=False)
