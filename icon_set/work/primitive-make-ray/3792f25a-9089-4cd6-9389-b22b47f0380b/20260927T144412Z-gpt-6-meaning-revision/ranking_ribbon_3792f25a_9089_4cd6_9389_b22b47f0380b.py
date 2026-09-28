"""ranking ribbon: repaired SOLO48 composition.
Plan: Mirrored alternating star points.
Keyshape: HRECT_L reserves ribbon width and room above it for the star.
Reduction: Fold seams removed; ribbon is a single notched band, separated from the star to avoid crowded crossings.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '3792f25a-9089-4cd6-9389-b22b47f0380b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__ranking-ribbon/20260927T144036Z-thuan-mac-1/reference/ranking ribbon_3792f25a-9089-4cd6-9389-b22b47f0380b.svg'
AUTHOR = "gpt-6"
CONSTRUCTION_REFERENCES = 'star'

class Drawing(Solo48):
    icon_id = 'ranking-ribbon'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'rewards'
    categories = ('rewards', 'primitives')
    aliases = ()
    keywords = ('ranking', 'ribbon')

    def build(self):
        # A five-point rank star sits above a bowed banner with folded tips.
        self.add_polyline('star',(24,8),(27,13),(34,14),(29,17),(30,22),(24,20),(18,22),(19,17),(14,14),(21,13),closed=True)
        self.add_bezier('banner-top',(10,32),((18,29),(30,29),(38,32)))
        self.add_line('banner-right',(38,32),(38,40))
        self.add_bezier('banner-bottom',(38,40),((30,38),(18,38),(10,40)))
        self.add_line('banner-left',(10,40),(10,32))
        self.add_contour('ribbon','banner-top','banner-right','banner-bottom','banner-left',closed=True)
        self.add_polyline('tail-left',(10,32),(4,40))
        self.add_polyline('tail-right',(38,32),(44,40))
        self.relate('connect','tail-left','ribbon')
        self.relate('connect','tail-right','ribbon')

