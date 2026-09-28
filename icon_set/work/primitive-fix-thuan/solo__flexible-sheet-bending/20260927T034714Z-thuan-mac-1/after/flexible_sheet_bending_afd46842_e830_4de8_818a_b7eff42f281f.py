"""Flexible Sheet Bending.

Plan: VRECT centerlines (8,4)-(40,44); two coherent bowed edges share one width and identical curve controls translated horizontally.
Construction references: Supplied bent-sheet silhouette; no useful exact Lucide match.
Reduction: Preserved a short detached echo stroke to show the sheet folding back.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'afd46842-e830-4de8-818a-b7eff42f281f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__flexible-sheet-bending/20260927T034714Z-thuan-mac-1/reference/bendable_afd46842-e830-4de8-818a-b7eff42f281f.svg'
SOURCE_ICON_IDS = ('afd46842-e830-4de8-818a-b7eff42f281f',)
SOURCE_PATHS = ('pictographic-primitives/construction/bendable_afd46842-e830-4de8-818a-b7eff42f281f.svg',)
AUTHOR = 'gpt-6'


class FlexibleSheetBending(Solo48):
    icon_id = 'flexible-sheet-bending'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'construction'
    categories = ('construction', 'primitives')
    aliases = ()
    keywords = ('flexible', 'sheet', 'bending')

    def build(self) -> None:
        # The broad front sheet bends left; a detached right edge shows flexibility.
        self.add_line('top', (16, 4), (30, 4))
        self.add_bezier('front-right', (30, 4), ((32, 18), (30, 34), (24, 44)))
        self.add_line('bottom', (24, 44), (8, 44))
        self.add_bezier('front-left', (8, 44), ((16, 34), (16, 20), (16, 4)))
        self.add_contour('sheet', 'top', 'front-right', 'bottom', 'front-left', closed=True)
        self.add_bezier('back-edge', (40, 12), ((40, 20), (40, 26), (38, 32)))
