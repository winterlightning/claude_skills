"""One solid outlined person beside a person with an interrupted outline. Bounds (6,6)-(42,42). Both circular heads radius4, body tops y22 give exact4-unit head/body ink clearance.
Construction reference: Human user.svg and full_body_ref.png: circular heads and coherent body outlines.
Omissions: Fine dash pattern simplified to a large clear interruption; heads remain outlined."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '58fce536-ad33-4c76-86df-d52bb405808c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__missing-person-pair/20260927T142540Z-thuan-mac-1/reference/safety missing people_58fce536-ad33-4c76-86df-d52bb405808c.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='missing-person-pair'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "wayfinding"
    categories = ("wayfinding", "primitives")
    aliases=()
    keywords=('safety', 'missing', 'people')
    def build(self):
        # Two full stick figures; the second has a visible break in its torso.
        for name,x in (('present',12),('missing',36)):
            self.add_arc(name+'-head-top',(x-4,10),(x+4,10),radius_x=4)
            self.add_arc(name+'-head-bottom',(x+4,10),(x-4,10),radius_x=4)
            self.add_contour(name+'-head',name+'-head-top',name+'-head-bottom',closed=True)
        self.add_line('present-torso',(12,22),(12,34))
        self.add_line('present-left-arm',(12,26),(6,31))
        self.add_line('present-right-arm',(12,26),(18,31))
        self.add_line('present-left-leg',(12,34),(8,42))
        self.add_line('present-right-leg',(12,34),(16,42))
        self.relate('connect','present-torso','present-left-arm','present-right-arm',
                    'present-left-leg','present-right-leg')
        self.mark_human_figure('present',head='present-head',torso='present-torso',torso_junction='start')
        self.add_line('missing-torso-upper',(36,22),(36,27))
        self.add_line('missing-torso-lower',(36,37),(36,39))
        self.add_line('missing-left-arm',(36,25),(30,31))
        self.add_line('missing-right-arm',(36,25),(42,31))
        self.add_line('missing-left-leg',(36,39),(32,42))
        self.add_line('missing-right-leg',(36,39),(40,42))
        self.relate('connect','missing-torso-upper','missing-left-arm','missing-right-arm')
        self.relate('connect','missing-torso-lower','missing-left-leg','missing-right-leg')
        self.mark_human_figure('missing',head='missing-head',torso='missing-torso-upper',torso_junction='start')
