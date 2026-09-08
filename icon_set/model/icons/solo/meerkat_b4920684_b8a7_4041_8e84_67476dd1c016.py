"""Alert meerkat with an upright torso, pointed snout, tucked forepaw, grounded hind foot and long tail. A complete animal silhouette replaces the floating wavy stroke. No useful Lucide meerkat match; right-facing asymmetry."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b4920684-b8a7-4041-8e84-67476dd1c016'
SOURCE_PATH = 'pictographic-primitives/animals/meerkat_b4920684-b8a7-4041-8e84-67476dd1c016.svg'
AUTHOR = 'gpt-6'


class Meerkat(Solo48):
    icon_id = 'meerkat'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('meerkat', 'animal')

    def build(self) -> None:
        # VRECT_XL: authored to its exact SOLO48 centerline bounds.
        self.add_line('tail-tip', (5, 46), (16, 39))
        self.add_arc('haunch', (16, 39), (19, 29), radius_x=13, radius_y=13, sweep=False)
        self.add_line('back', (19, 29), (21, 13))
        self.add_arc('ear', (21, 13), (21, 7), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('crown', (21, 7), (29, 2), radius_x=8, radius_y=5, sweep=True)
        self.add_line('snout-top', (29, 2), (43, 7))
        self.add_line('nose', (43, 7), (40, 14))
        self.add_line('jaw', (40, 14), (33, 17))
        self.add_arc('throat', (33, 17), (30, 23), radius_x=6, radius_y=6, sweep=False)
        self.add_arc('chest', (30, 23), (34, 33), radius_x=14, radius_y=14, sweep=True)
        self.add_line('belly', (34, 33), (31, 39))
        self.add_line('ankle', (31, 39), (36, 46))
        self.add_line('foot', (36, 46), (25, 46))
        self.add_line('tail-base', (25, 46), (5, 46))
        self.add_contour('outline', 'tail-tip', 'haunch', 'back', 'ear', 'crown', 'snout-top', 'nose', 'jaw', 'throat', 'chest', 'belly', 'ankle', 'foot', 'tail-base', closed=True)
        self.add_line('forepaw-1', (30, 23), (26, 28))
        self.add_contour('forepaw', 'forepaw-1', closed=False)
        self.relate("connect", 'forepaw', 'outline')
        self.add_dot('eye', (31, 10))
