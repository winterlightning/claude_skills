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
        # The face itself is heart shaped; smaller hearts sit inside as eyes.
        self.add_bezier('face',(24,11),((19,4),(8,4),(6,14)),((4,24),(14,34),(24,42)),((34,34),(44,24),(42,14)),((40,4),(29,4),(24,11)))
        self.add_contour('heart-face','face',closed=True)
        for side,x in (('left',17),('right',31)):
            self.add_bezier('eye-'+side,(x,20),((x-2,17),(x-5,17),(x-5,21)),((x-5,24),(x-1,26),(x,27)),((x+1,26),(x+5,24),(x+5,21)),((x+5,17),(x+2,17),(x,20)))
            self.add_contour('eye-heart-'+side,'eye-'+side,closed=True)
        self.add_arc('smile',(20,32),(28,32),radius_x=4,radius_y=3,sweep=False)
