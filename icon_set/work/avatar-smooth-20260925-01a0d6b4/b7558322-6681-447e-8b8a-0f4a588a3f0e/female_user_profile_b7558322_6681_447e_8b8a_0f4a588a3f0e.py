from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='b7558322-6681-447e-8b8a-0f4a588a3f0e'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__female-user-profile/20260925T034349Z-thuan-mac/reference/woman_b7558322-6681-447e-8b8a-0f4a588a3f0e.svg'
AUTHOR='gpt-6'
HUMAN_REFERENCE='icon_set/references/human_ref/user.svg'
CONSTRUCTION_REFERENCES='Lucide original/user-round.svg and atomic-debug/user-round.svg; shared circular jaw, tangent shoulder arcs and open bottom.'
PLAN='Smooth parted fringe and bob hair around a circular jaw, touching broad rounded shoulders. Remove the detached neck gap and tiny hair-end kinks.'
class Drawing(Solo48):
    icon_id='female-user-profile'
    keyshape=Keyshape.VRECT_L
    category='avatars'
    semantic_role='MAIN'
    semantic_kind='noun'
    aliases=()
    keywords=('woman', 'female', 'user', 'profile', 'parted hair')
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
        self.add_line('hair-left-root',(14,18),(14,14))
        self.add_arc('crown',(14,14),(34,14),radius_x=10)
        self.add_line('hair-right-root',(34,14),(34,18))
        self.add_arc('jaw',(34,18),(14,18),radius_x=10)
        self.add_contour('head','hair-left-root','crown','hair-right-root','jaw',closed=True)
        self.add_bezier('parted-fringe',(14,18),((20,18),(22,13),(24,13)),((26,13),(28,18),(34,18)))
        self.relate('connect','head','parted-fringe')
        for side in (-1,1):
            p=lambda x,y:(x,y) if side==-1 else (48-x,y)
            name='hair-'+str(side)
            self.add_bezier(name,p(14,18),(p(14,21),p(12,24),p(10,24)))
            self.relate('connect','head',name);self.relate('connect','parted-fringe',name)
        self.relate('connect','head','body')
