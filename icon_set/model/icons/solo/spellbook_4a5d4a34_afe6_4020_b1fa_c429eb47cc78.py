"""spellbook.
Open book with a six-ray magic asterisk on its wider left page.
Horizontal envelope; left page widened to give the magic symbol real clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4a5d4a34-afe6-4020-b1fa-c429eb47cc78'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_35/spellbook_4a5d4a34-afe6-4020-b1fa-c429eb47cc78.svg'
AUTHOR = 'gpt-6'
# Plan: Open spellbook with a star on its left page and a lower cover edge.
# References: book-open: mirrored page contours with a central gutter.
# Reduction: No defining parts omitted.

class AuthoredIcon(Solo48):
    icon_id = 'spellbook'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('spellbook',)

    def build(self) -> None:
        self.add_polyline('book',(4,8),(24,8),(30,14),(36,8),(44,8),(44,36),(36,36),(30,40),(24,36),(4,36),closed=True)
        self.add_line('spine',(30,14),(30,40))
        self.relate('connect','book','spine')
        self.add_polyline('sparkle-h',(13,23),(17,23),(21,23))
        self.add_polyline('star-d1',(15,19),(17,23),(19,27))
        self.add_polyline('star-d2',(15,27),(17,23),(19,19))
        self.relate('connect','sparkle-h','star-d1')
        self.relate('connect','sparkle-h','star-d2')
        self.relate('connect','star-d1','star-d2')

# Repair plan: Open book with a six-ray magic asterisk on its wider left page.
# Omissions: Five-point outlined star reduced to six rays; lower page seam omitted.
# Construction references: Lucide book-open original and atomic-debug: connected pages and central spine.
# Keyshape and proportions: Horizontal envelope; left page widened to give the magic symbol real clearance.
