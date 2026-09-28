"""Fresh SOLO48 revision of cobra-pose from the claimed reference.

The original and rejected drawing were compared before this construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts
from icon_set.model.icons.solo._payments_batch02 import small_dollar

SOURCE_ICON_ID = 'e18c7496-bcce-5643-bbc0-85abc5f004c0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cobra-pose/20260927T071330Z-thuan-mac-1/reference/yoga cobra pose_e18c7496-bcce-5643-bbc0-85abc5f004c0.svg'
AUTHOR = 'gpt-6'

class CobraPose(Solo48):
    icon_id = 'cobra-pose'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    categories = ("sports", "primitives")
    aliases = ()
    keywords = ('cobra', 'pose', 'yoga', 'exercise')

    def build(self) -> None:

        # Full reclining legs and upturned chest, with head over the torso axis.
        ellipse(self,'head',36,10,4)
        poly(self,'legs',(4,40),(20,36),(28,30))
        path(self,'torso',(28,30),('A',10,12,False,(34,22)))
        line(self,'arm',(34,22),(44,40))
        contacts(self)
        self.mark_human_figure('person',head='head',torso='torso-1',torso_junction='end')
