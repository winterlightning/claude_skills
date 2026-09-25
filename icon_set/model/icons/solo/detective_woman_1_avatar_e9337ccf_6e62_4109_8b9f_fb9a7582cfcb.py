from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='e9337ccf-6e62-4109-8b9f-fb9a7582cfcb'
SOURCE_PATH='pictographic-primitives/avatars/detective woman_e9337ccf-6e62-4109-8b9f-fb9a7582cfcb.svg'
SOURCE_HEAD_ICON_ID='detective-woman-1'
AUTHOR='gpt-6'
HUMAN_REFERENCE='icon_set/references/human_ref/user.svg'
CONSTRUCTION_REFERENCES='Lucide original/user-round.svg and atomic-debug/user-round.svg; shared circular jaw, tangent shoulder arcs and open bottom.'
PLAN='Round cap, smooth bob flips, circular jaw and broad curved V-neck shoulders. No extra visor seam or scarf tail.'
class DetectiveWoman1Avatar(Solo48):
    icon_id='detective-woman-1-avatar'
    keyshape=Keyshape.VRECT_L
    category = 'avatars'
    categories = ('primitives', 'avatars')
    semantic_role='MAIN'
    semantic_kind='noun'
    aliases=()
    keywords=('woman', 'detective', 'cap', 'portrait', 'bust')
    def build(self):
        # Entire avatar ink (6,2)-(42,46), centerline (8,4)-(40,44).
        # Jaw bottom 28, shoulder top 32: four centerline units, zero ink gap.
        top = 28 + HEAD_BODY_CENTERLINE_GAP
        self.add_line('body-left-side',(8,44),(8,40))
        self.add_arc('body-left-shoulder',(8,40),(16,top),radius_x=8)
        self.add_line('body-top',(16,top),(24,top))
        self.add_line('body-top-right',(24,top),(32,top))
        self.add_arc('body-right-shoulder',(32,top),(40,40),radius_x=8)
        self.add_line('body-right-side',(40,40),(40,44))
        self.add_contour('body','body-left-side','body-left-shoulder','body-top','body-top-right','body-right-shoulder','body-right-side')
        self.add_arc('crown',(12,16),(36,16),radius_x=12)
        self.add_arc('jaw',(36,16),(12,16),radius_x=12)
        self.add_contour('head','crown','jaw',closed=True)
        self.add_bezier('visor',(12,16),((18,18),(30,18),(36,16)))
        self.relate('connect','head','visor')
        for side in (-1,1):
            p=lambda x,y:(x,y) if side==-1 else (48-x,y)
            name='hair-'+str(side)
            self.add_bezier(name,p(12,16),(p(12,20),p(10,24),p(8,24)))
            self.relate('connect','head',name);self.relate('connect','visor',name)
        self.add_polyline('body-v-collar',(16,top),(24,42),(32,top))
        self.relate('connect','body','body-v-collar')
        self.relate('connect','head','body')
