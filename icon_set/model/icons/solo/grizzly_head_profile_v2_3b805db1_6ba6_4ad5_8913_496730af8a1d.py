# Variant of grizzly-head-profile; parent file remains unchanged.
'Bear head with the neck joined to both endpoints of the head contour. HRECT_XL (2,5)-(46,43) preserves the profile. Roaring jaws and eye retained. Deliberate right-facing asymmetry.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3b805db1-6ba6-4ad5-8913-496730af8a1d'
SOURCE_PATH = 'pictographic-primitives/animals/grizzly head side_3b805db1-6ba6-4ad5-8913-496730af8a1d.svg'
AUTHOR = 'gpt-6'

class GrizzlyHeadProfileVariant2(Solo48):
    icon_id = 'grizzly-head-profile-v2'
    variant_of = 'grizzly-head-profile'
    variant_label = 'Connected neck outline'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('bear', 'grizzly', 'head', 'profile', 'roar', 'snout', 'wildlife', 'animal')

    def build(self) -> None:
        self.add_line('head-1', (2, 17), (10, 13))
        self.add_line('head-2', (10, 13), (8, 9))
        self.add_arc('head-3', (8, 9), (12, 5), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('head-4', (12, 5), (18, 11), radius_x=6, radius_y=6, sweep=True)
        self.add_line('head-5', (18, 11), (23, 11))
        self.add_arc('head-6', (23, 11), (35, 17), radius_x=13, radius_y=13, sweep=True)
        self.add_line('head-7', (35, 17), (46, 22))
        self.add_line('head-8', (46, 22), (43, 28))
        self.add_arc('head-9', (43, 28), (37, 30), radius_x=7, radius_y=7, sweep=True)
        self.add_line('head-10', (37, 30), (31, 30))
        self.add_arc('head-11', (31, 30), (28, 33), radius_x=3, radius_y=3, sweep=False)
        self.add_arc('head-12', (28, 33), (31, 36), radius_x=3, radius_y=3, sweep=False)
        self.add_line('head-13', (31, 36), (40, 38))
        self.add_line('head-14', (40, 38), (32, 43))
        self.add_arc('head-15', (32, 43), (23, 40), radius_x=10, radius_y=10, sweep=False)
        self.add_line('head-16', (23, 40), (15, 43))
        self.add_contour('head', 'head-1', 'head-2', 'head-3', 'head-4', 'head-5', 'head-6', 'head-7', 'head-8', 'head-9', 'head-10', 'head-11', 'head-12', 'head-13', 'head-14', 'head-15', 'head-16', closed=False)
        self.add_dot('eye', (29, 21))
        self.add_line('neck-top', (2,17), (2,29))
        self.add_arc('neck-1', (2,29), (15,43), radius_x=18, radius_y=18, sweep=False)
        self.add_contour('neck', 'neck-top', 'neck-1', closed=False)
        self.relate('connect','neck','head')
