"""Three smooth stones decreasing upward. Square extremes 6,6–42,42. Shared axis and elliptical lobes; no useful exact Lucide match; omit occluded back edges."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '11d2f019-0f49-57bc-845a-b927c3976eed'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__spa-stone-stack/20260927T093533Z-thuan-mac-1/reference/spa stone_11d2f019-0f49-57bc-845a-b927c3976eed.svg'
AUTHOR = 'gpt-6'

class SpaStoneStack(Solo48):
    icon_id = 'spa-stone-stack'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "spas"
    categories = ("primitives", "spas")
    aliases = ()
    keywords = ('spa', 'wellness', 'spa-stone-stack')

    def build(self):
        self.add_arc('top-top', (12,13), (36,13), radius_x=12, radius_y=7)
        self.add_arc('top-bottom', (36,13), (12,13), radius_x=12, radius_y=7)
        self.add_contour('top', 'top-top', 'top-bottom', closed=True)
        self.add_arc('middle-upper-left', (12,13), (8,25), radius_x=4, radius_y=12, sweep=False)
        self.add_arc('middle-lower', (8,25), (40,25), radius_x=16, radius_y=7, sweep=False)
        self.add_arc('middle-upper-right', (40,25), (36,13), radius_x=4, radius_y=12, sweep=False)
        self.add_contour('middle', 'middle-upper-left', 'middle-lower', 'middle-upper-right')
        self.add_arc('base-left', (8,25), (6,34), radius_x=2, radius_y=9, sweep=False)
        self.add_arc('base-bottom', (6,34), (42,34), radius_x=18, radius_y=8, sweep=False)
        self.add_arc('base-right', (42,34), (40,25), radius_x=2, radius_y=9, sweep=False)
        self.add_contour('base', 'base-left', 'base-bottom', 'base-right')
        self.relate('connect', 'top', 'middle')
        self.relate('connect', 'middle', 'base')
