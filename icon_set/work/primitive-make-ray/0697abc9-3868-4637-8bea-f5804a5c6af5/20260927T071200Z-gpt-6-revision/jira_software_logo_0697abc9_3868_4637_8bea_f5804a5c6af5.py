"""A diamond outline folds over itself like a ribbon, with a small inner diamond opening near its centre.

Plan: Diamond ribbon surrounding a small diamond opening.
Keyshape: SQUARE; exact SOLO48 envelope from the contract.
Construction reference: Previously inspected diamond: centered matching diagonal edges.
Simplification: Fold seams omitted for a clean ribbon band.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0697abc9-3868-4637-8bea-f5804a5c6af5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__jira-software-logo/20260927T070927Z-thuan-mac-1/reference/jira software logo_0697abc9-3868-4637-8bea-f5804a5c6af5.svg'
AUTHOR = "gpt-6"


class JiraSoftwareLogo(Solo48):
    icon_id = 'jira-software-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('jira-software', 'jira', 'atlassian', 'diamond', 'logo', 'brand', 'agile')

    def build(self):
        # The source is a softly asymmetric folded diamond, not a rigid badge.
        self.add_bezier('top-left',(6,24),((6,21),(14,14),(18,12)))
        self.add_bezier('crown',(18,12),((21,8),(23,6),(24,6)))
        self.add_bezier('upper-right',(24,6),((27,6),(35,18),(42,22)))
        self.add_bezier('lower-right',(42,22),((42,26),(32,38),(26,42)))
        self.add_bezier('bottom',(26,42),((22,42),(20,40),(18,38)))
        self.add_bezier('lower-left',(18,38),((12,32),(6,27),(6,24)))
        self.add_contour('ribbon','top-left','crown','upper-right',
                         'lower-right','bottom','lower-left',closed=True)
        self.add_polyline('opening',(24,18),(30,24),(24,30),(18,24),closed=True)
