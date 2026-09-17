"""Thai Massage Stretch.

Plan: Kneeling therapist behind hands-and-knees recipient. Shared full_body_ref.png proportions; r4 heads with exact 8-unit head-outline to upper-torso gaps. Bounds (4,8)-(44,40).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '876d5973-30e6-5ce8-bd9e-b8d430fe7ad0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/thai massage pose_876d5973-30e6-5ce8-bd9e-b8d430fe7ad0.svg'
AUTHOR = 'gpt-6'


class ThaiMassageStretch(Solo48):
    icon_id = 'thai-massage-stretch'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/health'
    aliases = ()
    keywords = ('thai', 'massage', 'stretch')

    def build(self):
        for p,x,y in [('therapist',8,12),('recipient',40,22)]:
            self.add_arc(p+'-head-top',(x-4,y),(x+4,y),radius_x=4)
            self.add_arc(p+'-head-bottom',(x+4,y),(x-4,y),radius_x=4)
            self.add_contour(p+'-head',p+'-head-top',p+'-head-bottom',closed=True)
        self.add_line('therapist-torso',(8,24),(8,28))
        self.add_arc('therapist-lower-back',(8,28),(4,32),radius_x=4)
        self.add_line('therapist-knee',(4,32),(12,40))
        self.add_line('therapist-foot',(12,40),(4,40))
        self.add_contour('therapist-body','therapist-torso','therapist-lower-back','therapist-knee','therapist-foot')
        self.add_line('therapist-arm',(8,28),(20,28))
        self.add_line('recipient-torso',(28,22),(20,22))
        self.add_line('recipient-thigh',(20,22),(20,28))
        self.add_line('recipient-knee',(20,28),(20,40))
        self.add_contour('recipient-rear-leg','recipient-thigh','recipient-knee')
        self.add_polyline('recipient-arm',(28,22),(28,40),(44,40))
        self.relate('connect','therapist-body','therapist-arm')
        self.relate('connect','therapist-arm','recipient-rear-leg')
        self.relate('connect','recipient-torso','recipient-rear-leg')
        self.relate('connect','recipient-torso','recipient-arm')
        self.mark_human_figure('therapist',head='therapist-head',torso='therapist-torso',torso_junction='start')
        self.mark_human_figure('recipient',head='recipient-head',torso='recipient-torso',torso_junction='start')
