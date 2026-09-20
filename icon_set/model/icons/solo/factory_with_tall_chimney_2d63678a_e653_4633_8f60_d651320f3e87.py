'Industrial Factory Building.\n\nSymbol plan: Flat factory roof, sloped right roof, tall chimney and open doorway; no invented windows.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: factory.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2d63678a-e653-4633-8f60-d651320f3e87'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/facility_2d63678a-e653-4633-8f60-d651320f3e87.svg'
AUTHOR = 'gpt-6'

class FactoryWithTallChimney(Solo48):
    icon_id = 'factory-with-tall-chimney'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('factory', 'with', 'tall', 'chimney')

    def build(self):
        # Flat factory roof, sloped right roof, tall chimney and open doorway; no invented windows.
        axis_x = 24
        p_6_22 = (6, 22)
        p_6_42 = (6, 42)
        p_20_32 = (20, 32)
        p_20_42 = (20, 42)
        p_28_22 = (28, 22)
        p_29_6 = (29, 6)
        p_30_32 = (30, 32)
        p_30_42 = (30, 42)
        p_37_6 = (37, 6)
        p_38_26 = (38, 26)
        p_42_28 = (42, 28)
        p_42_42 = (2 * axis_x - p_6_42[0], p_6_42[1])
        self.add_line('building-1', p_6_22, p_28_22)
        self.add_line('building-2', p_28_22, p_42_28)
        self.add_line('building-3', p_42_28, p_42_42)
        self.add_line('building-4', p_42_42, p_30_42)
        self.add_line('building-5', p_30_42, p_30_32)
        self.add_line('building-6', p_30_32, p_20_32)
        self.add_line('building-7', p_20_32, p_20_42)
        self.add_line('building-8', p_20_42, p_6_42)
        self.add_line('building-9', p_6_42, p_6_22)
        self.add_contour('building', 'building-1', 'building-2', 'building-3', 'building-4', 'building-5', 'building-6', 'building-7', 'building-8', 'building-9', closed=True)
        self.add_line('chimney-1', p_28_22, p_29_6)
        self.add_line('chimney-2', p_29_6, p_37_6)
        self.add_line('chimney-3', p_37_6, p_38_26)
        self.add_contour('chimney', 'chimney-1', 'chimney-2', 'chimney-3', closed=False)
        self.relate("connect", 'chimney', 'building')
