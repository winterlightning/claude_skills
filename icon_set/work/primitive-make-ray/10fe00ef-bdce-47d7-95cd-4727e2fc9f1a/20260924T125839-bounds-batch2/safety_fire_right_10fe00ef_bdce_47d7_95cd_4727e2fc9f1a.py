"""safety fire right.
Right-pointing arrow above two flame trails.
Square extremes come from arrowhead, shaft and lower trail; direction is intentionally asymmetric.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '10fe00ef-bdce-47d7-95cd-4727e2fc9f1a'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_33/safety fire right_10fe00ef-bdce-47d7-95cd-4727e2fc9f1a.svg'
AUTHOR = 'gpt-6'
# Plan: Right-pointing evacuation arrow with three flowing flame trails underneath.
# Reference: rotate-cw: joined arrowhead principles; no useful local flame-trail match.
# Reduction: Reduced bottom flame outline to one smooth tongue; three trails retained.

class AuthoredIcon(Solo48):
    icon_id = 'safety-fire-right'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('safety', 'fire', 'right')

    def build(self) -> None:
        self.add_line('arrow-shaft',(6,16),(42,16))
        self.add_polyline('arrow-head',(32,6),(42,16),(32,26))
        self.relate('connect','arrow-shaft','arrow-head')
        self.add_bezier('flame-middle',(6,28),((12,28),(16,28),(22,24)))
        self.add_bezier('flame-bottom',(6,42),((10,34),(16,42),(22,36)))

# Repair plan: Right-pointing arrow above two flame trails.
# Omissions: Outlined arrow reduced to an open arrow; enclosed lower flame opened; one trail omitted.
# Construction references: No additional useful local Lucide match used.
# Keyshape and proportions: Square extremes come from arrowhead, shaft and lower trail; direction is intentionally asymmetric.
