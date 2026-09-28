"""Fresh SOLO48 revision of chair-pose from the claimed reference.

The original and rejected drawing were compared before this construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts
from icon_set.model.icons.solo._payments_batch02 import small_dollar

SOURCE_ICON_ID = 'cfd5ff88-dde9-5378-9cfa-f993404a30bf'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__chair-pose/20260927T071330Z-thuan-mac-1/reference/yoga chair awkward pose_cfd5ff88-dde9-5378-9cfa-f993404a30bf.svg'
AUTHOR = 'gpt-6'

class ChairPose(Solo48):
    icon_id = 'chair-pose'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('chair', 'pose', 'yoga', 'exercise')

    def build(self) -> None:

        ellipse(self,'head',13,12,5)
        poly(self,'raised-arm',(28,4),(28,20),(18,24))
        line(self,'torso',(18,24),(30,34))
        poly(self,'legs',(30,34),(14,34),(24,44),(40,44))
        contacts(self)
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
