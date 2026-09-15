"""Short-haired judoka with crossing gi lapels.

Fresh SOLO48 construction, not scaled from AVATAR64. Human reference:
icon_set/references/human_ref/user.svg; Lucide user-round/shirt construction.
VRECT_L exact envelope; detached head bottom 20, body top 28.
Small facial marks omitted; clothing/headwear carry the intended meaning.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c83c8db2-b81d-59b8-9e32-0a97d91dc9fc'
SOURCE_PATH = 'pictographic-primitives/avatars/avatar judo athlete man_c83c8db2-b81d-59b8-9e32-0a97d91dc9fc.svg'
AUTHOR='gpt-6'

class AvatarJudoAthleteMan(Solo48):
    icon_id='avatar-judo-athlete-man'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='people/occupations'
    aliases=()
    keywords=('avatar', 'judo', 'athlete', 'man', 'bust', 'occupation', 'body')

    def build(self):
        # Plan: independent head, garment, and intrinsic clothing/tool details.
        # Paired body/hair parts derive from one axis; shared nodes keep real joins.
        self.add_arc('head-top',(16,12),(32,12),radius_x=8)
        self.add_arc('head-bottom',(32,12),(16,12),radius_x=8)
        self.add_contour('head','head-top','head-bottom',closed=True)
        top=20+8  # exact 4-unit head/body ink gap
        self.add_polyline('body',(8,44),(8,top+4),(12,top),(24,top),(36,top),(40,top+4),(40,44))
        self.add_polyline('lapel',(12,top),(24,40),(28,44))
        self.add_line('cross-lapel',(36,top),(24,40))
        self.relate('connect','body','lapel')
        self.relate('connect','body','cross-lapel')
        self.relate('connect','lapel','cross-lapel')
