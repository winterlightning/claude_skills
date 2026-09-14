"""Ponytailed judoka with crossing gi lapels.

Fresh SOLO48 construction, not scaled from AVATAR64. Human reference:
icon_set/references/human_ref/user.svg; Lucide user-round/shirt construction.
VRECT_L exact envelope; detached head bottom 20, body top 28.
Small facial marks omitted; clothing/headwear carry the intended meaning.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID=None
SOURCE_PATH='work/head-solo/batch-01/references/avatar-judo-athlete-woman.svg'
AUTHOR='gpt-6'

class AvatarJudoAthleteWoman(Solo48):
    icon_id='avatar-judo-athlete-woman'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='people/occupations'
    aliases=()
    keywords=('avatar', 'judo', 'athlete', 'woman', 'bust', 'occupation', 'body')

    def build(self):
        # Plan: independent head, garment, and intrinsic clothing/tool details.
        # Paired body/hair parts derive from one axis; shared nodes keep real joins.
        self.add_arc('head-top',(16,12),(32,12),radius_x=8)
        self.add_arc('head-bottom',(32,12),(16,12),radius_x=8)
        self.add_contour('head','head-top','head-bottom',closed=True)
        self.add_bezier('ponytail',(32,12),((40,12),(32,16),(38,20)))
        self.relate('connect','head','ponytail')
        top=20+8  # exact 4-unit head/body ink gap
        self.add_polyline('body',(8,44),(8,top+4),(12,top),(24,top),(36,top),(40,top+4),(40,44))
        self.add_polyline('lapel',(12,top),(24,40),(28,44))
        self.add_line('cross-lapel',(36,top),(24,40))
        self.relate('connect','body','lapel')
        self.relate('connect','body','cross-lapel')
        self.relate('connect','lapel','cross-lapel')
