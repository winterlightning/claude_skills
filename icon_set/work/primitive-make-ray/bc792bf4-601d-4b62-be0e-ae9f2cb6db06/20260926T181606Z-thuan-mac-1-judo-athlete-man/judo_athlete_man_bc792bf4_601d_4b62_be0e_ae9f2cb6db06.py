"""judo-athlete-man: revised SOLO48 drawing from the claimed source.

Comparison: The rejected generic bust did not match the source, which is a round head with a long sweep.
Revision: Redrew the circular head and asymmetric forehead sweep without the invented torso.
Human construction: icon_set/references/human_ref/user.svg; Lucide user-round supplies simple circular head and shoulder arcs.
The emitted primitives use a shared axis where the reference is symmetric.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'bc792bf4-601d-4b62-be0e-ae9f2cb6db06'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__judo-athlete-man/20260926T175531Z-thuan-mac-1/reference/judo athlete man_bc792bf4-601d-4b62-be0e-ae9f2cb6db06.svg'
AUTHOR = "gpt-6"

class JudoAthleteMan(Solo48):
    icon_id = 'judo-athlete-man'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('judo', 'athlete', 'man', 'avatars')

    def build(self):
        # One round cropped head and a long asymmetrical sweep across its forehead.
        cx, cy, radius = 24, 24, 20
        self.add_arc('head-top',(cx-radius,cy),(cx+radius,cy),radius_x=radius)
        self.add_arc('head-bottom',(cx+radius,cy),(cx-radius,cy),radius_x=radius)
        self.add_contour('head','head-top','head-bottom',closed=True)
        self.add_bezier('swept-fringe',(4,24),((9,16),(14,16),(20,19)),((26,25),(35,24),(44,24)))
        self.relate('connect','head','swept-fringe')
