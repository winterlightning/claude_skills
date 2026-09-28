"""Square envelope; opened the forehead and lower-jaw band around the solid eye and retained the wedge snout.

SQUARE: visible ink (4, 4, 44, 44). Square envelope preserves the subject’s near-equal overall width and height.
No useful exact local Lucide match; retained the inspected parent silhouette.
"""
# Independent revision; parent models preserved.
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '9623465e-0b09-52b2-a673-4a555e6456b1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__shark-head/20260927T091435Z-thuan-mac-1/reference/tiger shark_9623465e-0b09-52b2-a673-4a555e6456b1.svg'
AUTHOR = "gpt-6"

class SharkHead(Solo48):
    icon_id = 'shark-head'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('shark', 'head', 'jaw', 'teeth', 'fish', 'sea', 'predator', 'bite')

    def build(self) -> None:
        self.add_bezier('back', (6, 6), ((13, 6), (20, 11), (28, 10)))
        self.add_arc('snout-top', (28, 10), (42, 25), radius_x=30)
        self.add_arc('snout-bottom', (42, 25), (40, 31), radius_x=10)
        self.add_line('mouth-top', (40, 31), (24, 30))
        self.add_line('jaw-1', (24, 30), (32, 40))
        self.add_line('jaw-2', (32, 40), (14, 40))
        self.add_line('jaw-3', (14, 40), (6, 42))
        self.add_contour('profile', 'back', 'snout-top', 'snout-bottom', 'mouth-top', 'jaw-1', 'jaw-2', 'jaw-3')
        self.add_line('gill', (10, 23), (10, 29))
        self.add_dot('eye', (28, 22))
