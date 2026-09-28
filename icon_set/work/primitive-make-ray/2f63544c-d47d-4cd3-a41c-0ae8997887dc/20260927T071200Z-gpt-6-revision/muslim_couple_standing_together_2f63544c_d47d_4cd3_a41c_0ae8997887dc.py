"""Muslim Couple Standing Together.

Symbol plan: Two front-facing people in continuous draped clothing, one headscarf and one round cap. Drop tiny sleeve lines and layered cloth edges.
HRECT_L centerline extremes (4,8)-(44,40); exact envelope selected for the subject's proportions.
Construction reference: human_ref/user.svg and full_body_ref.png: circular jaws and simple clothing silhouettes. Continuous clothed figures, not detached stick figures or one centered avatar.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '2f63544c-d47d-4cd3-a41c-0ae8997887dc'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__muslim-couple-standing-together/20260927T070927Z-thuan-mac-1/reference/muslim couple_2f63544c-d47d-4cd3-a41c-0ae8997887dc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'muslim-couple-standing-together'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('muslim', 'person', 'headscarf', 'clothing', 'portrait', 'islam', 'community', 'people')

    def build(self) -> None:
        # Two separate standing figures, with a draped scarf and a capped head.
        for name,cx in (('woman',12),('man',36)):
            left,right=cx-8,cx+8
            self.add_arc(name+'-crown',(left,16),(right,16),radius_x=8)
            self.add_line(name+'-right',(right,16),(right,36))
            self.add_arc(name+'-hem-right',(right,36),(right-4,40),radius_x=4)
            self.add_arc(name+'-hem-left',(left+4,40),(left,36),radius_x=4)
            self.add_line(name+'-left',(left,36),(left,16))
            self.add_contour(name+'-cloak',name+'-left',name+'-crown',
                             name+'-right',name+'-hem-right',closed=False)
            self.add_contour(name+'-left-hem',name+'-hem-left')
            self.add_arc(name+'-jaw',(right,16),(left,16),radius_x=8)
            self.relate('connect',name+'-jaw',name+'-cloak')
            self.relate('connect',name+'-left-hem',name+'-cloak')
        self.add_line('cap-brim',(28,16),(44,16))
        self.relate('connect','cap-brim','man-cloak')
        self.relate('connect','cap-brim','man-jaw')
