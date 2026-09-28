"""Mother Nursing Baby.
Plan: (8,4)-(40,44). Large mother head over curved upper body, smaller baby cradled across chest. Mother head bottom16 to shoulder24; baby head bottom28 to torso36: both exact8 centerline gaps.
References: supplied original source; human_ref/user.svg and full_body_ref.png: round heads, curved shoulders and sparse held-child gesture.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2723da16-ddad-4fba-89e3-2da6909c1ad1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__mother-nursing-baby-2723da16/20260927T153322Z-thuan-mac-1/reference/mother baby 1_2723da16-ddad-4fba-89e3-2da6909c1ad1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'mother-nursing-baby-2723da16-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ('mother-nursing-baby',)
    keywords = ('mother', 'nursing', 'baby')

    def build(self):
        # The large mother head and lower cradling arm frame the smaller baby.
        def circle(name,cx,cy,r):
            self.add_arc(name+'-a',(cx-r,cy),(cx+r,cy),radius_x=r,sweep=True)
            self.add_arc(name+'-b',(cx+r,cy),(cx-r,cy),radius_x=r,sweep=True)
            self.add_contour(name,name+'-a',name+'-b',closed=True)
        circle('mother-head',20,12,8)
        self.add_arc('mother-shoulder',(20,29),(8,36),radius_x=12,sweep=False)
        self.add_line('mother-side',(8,36),(8,44))
        self.add_contour('mother-body','mother-shoulder','mother-side')
        circle('baby-head',36,28,4)
        self.add_line('baby-torso',(36,40),(36,44))
        self.add_bezier('cradle-arm',(8,44),((16,38),(28,38),(36,44)))
        self.relate('connect','mother-body','cradle-arm')
        self.relate('connect','cradle-arm','baby-torso')
        self.mark_human_figure('baby',head='baby-head',torso='baby-torso',torso_junction='start')
