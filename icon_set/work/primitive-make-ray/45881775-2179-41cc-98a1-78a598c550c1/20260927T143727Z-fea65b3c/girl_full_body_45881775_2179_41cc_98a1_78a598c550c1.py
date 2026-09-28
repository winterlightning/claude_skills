"""Revision of the claimed reference after comparing original and rejected drawing."""
"""A front-facing girl with a visible centre part, blank circular face, side curls, short sleeves and long garment.
The hair lobes form the part without a tiny interior hole. The face touches the garment as in the source.
VRECT_L centreline bounds (8,4)-(40,44). Human reference: icon_set/references/human_ref/full_body_ref.png and user.svg.
No useful Lucide subject match; balanced arcs and mirrored garment sides follow the shared geometry style.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '45881775-2179-41cc-98a1-78a598c550c1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__girl-full-body/20260927T142529Z-thuan-mac-1/reference/girl full body_45881775-2179-41cc-98a1-78a598c550c1.svg'
AUTHOR = "gpt-6"
SOURCE_CATEGORY = 'avatars'

class BatchSolo(Solo48):
    icon_id = 'girl-full-body'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('avatars', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('girl', 'with', 'centre', 'parted', 'hair')

    def build(self):
        # Rounded paired hair lobes reveal a centre part above a blank circular face.
        self.add_bezier('head-top-1',(17,11),((17,7),(17,4),(19,4)))
        self.add_line('head-top-2',(19,4),(24,7))
        self.add_line('head-top-3',(24,7),(29,4))
        self.add_bezier('head-top-4',(29,4),((31,4),(31,7),(31,11)))
        self.add_arc('face-bottom',(31,11),(17,11),radius_x=7)
        self.add_contour('head','head-top-1','head-top-2','head-top-3','head-top-4','face-bottom',closed=True)
        self.add_arc('hair-left',(17,11),(8,17),radius_x=9)
        self.add_arc('hair-right',(40,17),(31,11),radius_x=9)
        self.relate('connect','head','hair-left')
        self.relate('connect','head','hair-right')
        # The face touches a broad upper garment, matching the source portrait.
        self.add_bezier('left-shoulder',(20,26),((17,23),(16,25),(16,28)))
        self.add_line('left-arm',(16,28),(12,37))
        self.add_line('left-cuff',(12,37),(20,37))
        self.add_line('left-torso',(20,37),(20,42))
        self.add_arc('left-hem',(20,42),(20,44),radius_x=2)
        self.add_line('hem',(20,44),(28,44))
        self.add_arc('right-hem',(28,44),(28,42),radius_x=2)
        self.add_line('right-torso',(28,42),(28,37))
        self.add_line('right-cuff',(28,37),(36,37))
        self.add_line('right-arm',(36,37),(32,28))
        self.add_bezier('right-shoulder',(32,28),((32,25),(31,23),(28,26)))
        self.add_line('body-top-right',(28,26),(24,26))
        self.add_line('body-top-left',(24,26),(20,26))
        self.add_line('neck',(24,18),(24,26))
        self.add_contour('dress','left-shoulder','left-arm','left-cuff','left-torso',
                         'left-hem','hem','right-hem','right-torso','right-cuff',
                         'right-arm','right-shoulder','body-top-right','body-top-left',closed=True)
        self.relate('connect','head','neck')
        self.relate('connect','neck','dress')
