"""Revision of the claimed reference after comparing original and rejected drawing."""
"""Heart-shaped face with heart eyes.
Plan: SQUARE uses (6,6)-(42,42); large mirrored hearts sit above a pointed lower face.
Design changes: Heart eyes form the upper face lobes. Shallower eye clefts enlarge their internal openings; the central head cleft and pointed chin retain the heart-face structure. Compact smile retained.
References: Original reference supplies heart eyes, central cleft and pointed chin. Shared mirrored heart construction; human user.svg reviewed for facial vocabulary. No additional Lucide construction used.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='9e0a5c9e-1146-434d-a2ff-8fa7fe9193f8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__heart-shaped-face-with-heart-eyes-solo/20260927T142529Z-thuan-mac-1/reference/face smile hearts_9e0a5c9e-1146-434d-a2ff-8fa7fe9193f8.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id='heart-shaped-face-with-heart-eyes-solo'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('heart','eyes','love','smile')
    def build(self):
        # An outer heart encloses a pair of compact heart silhouettes.
        self.add_bezier('face',(24,12),((21,6),(17,6),(14,6)),((9,6),(6,10),(6,16)),((6,25),(14,35),(24,42)),((34,35),(42,25),(42,16)),((42,10),(39,6),(34,6)),((31,6),(27,6),(24,12)))
        self.add_contour('heart-face','face',closed=True)
        for side,x in (('left',18),('right',30)):
            self.add_polyline('eye-'+side,(x-2,20),(x,24),(x+2,20))
        self.add_dot('mouth',(24,30))
