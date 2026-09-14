"""A right-facing fish with a forked tail and curved gill. HRECT_L extremes (6,8)-(42,40). Lucide fish informs the curved gill and clear head; source silhouette governs the simplified finless body."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ef113d95-603a-4326-bef0-b182c1dd8c4f'
SOURCE_PATH = 'pictographic-primitives/symbol/fish with two small circle_ef113d95-603a-4326-bef0-b182c1dd8c4f.svg'
AUTHOR = 'gpt-6'


class FishOutline(Solo48):
    icon_id = 'fish-outline'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('fish', 'sea', 'seafood', 'animal', 'aquarium', 'ocean', 'pet', 'food')

    def build(self) -> None:
        self.add_line('tail-top', (6,8), (14,17))
        self.add_arc('back-left', (14,17), (24,8), radius_x=10, radius_y=9)
        self.add_arc('back-right', (24,8), (42,24), radius_x=25, radius_y=40)
        self.add_arc('belly-right', (42,24), (24,40), radius_x=25, radius_y=40)
        self.add_arc('belly-left', (24,40), (14,31), radius_x=10, radius_y=9)
        self.add_line('tail-bottom-1', (14,31), (6,40))
        self.add_line('tail-bottom-2', (6,40), (7,24))
        self.add_line('tail-bottom-3', (7,24), (6,8))
        self.add_contour('outline', 'tail-top', 'back-left', 'back-right', 'belly-right', 'belly-left', 'tail-bottom-1', 'tail-bottom-2', 'tail-bottom-3', closed=True)
        self.add_arc('gill', (30,19), (30,29), radius_x=7, sweep=False)
