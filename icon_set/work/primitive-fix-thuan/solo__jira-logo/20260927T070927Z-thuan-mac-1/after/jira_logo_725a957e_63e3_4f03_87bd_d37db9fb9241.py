"""Three rounded L-shaped chevrons of increasing size stack diagonally, each pointing to the upper right.

Plan: Three northeast elbows repeat diagonally with increasing arm length.
Keyshape: SQUARE; exact SOLO48 envelope from the contract.
Construction reference: Previously inspected corner-down-right: joined elbow strokes.
Simplification: Outlined L ribbons become monoline elbows.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '725a957e-63e3-4f03-87bd-d37db9fb9241'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__jira-logo/20260927T070927Z-thuan-mac-1/reference/jira logo_725a957e-63e3-4f03-87bd-d37db9fb9241.svg'
AUTHOR = 'gpt-6'


class JiraLogo(Solo48):
    icon_id = 'jira-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('jira', 'atlassian', 'project-management', 'logo', 'brand', 'agile', 'tickets')

    def build(self):
        # Three staggered, rounded corner ribbons echo the source logo.
        for i,(x,y,length) in enumerate(((6,30,12),(16,18,14),(26,6,16))):
            self.add_line(f'bar-{i}',(x,y),(x+length-4,y))
            self.add_arc(f'bend-{i}',(x+length-4,y),(x+length,y+4),radius_x=4)
            self.add_line(f'drop-{i}',(x+length,y+4),(x+length,y+12))
            self.add_contour(f'ribbon-{i}',f'bar-{i}',f'bend-{i}',f'drop-{i}')
