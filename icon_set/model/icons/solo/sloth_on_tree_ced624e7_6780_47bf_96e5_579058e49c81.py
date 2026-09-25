from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ced624e7-6780-47bf-96e5-579058e49c81'
SOURCE_PATH = 'pictographic-primitives/animals/sloth on tree_ced624e7-6780-47bf-96e5-579058e49c81.svg'
AUTHOR = 'gpt-6'


class SlothOnBranch(Solo48):
    icon_id = 'sloth-on-branch'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('sloth', 'branch', 'hanging', 'tree', 'slow', 'animal', 'rainforest', 'wildlife')

    def build(self) -> None:
        self.add_arc('head-top', (4,17), (22,17), radius_x=9, radius_y=9)
        self.add_arc('head-bottom', (22,17), (4,17), radius_x=9, radius_y=9)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)

        self.add_line('back-top',(13,8),(28,8))
        self.add_bezier('back',(28,8),((38,8),(44,15),(44,24)))
        self.add_polyline('hind-leg',(44,24),(44,30),(40,30))
        self.add_bezier('hind-paw',(40,30),((36,30),(36,25),(36,20)))
        for a,b in (('head','back-top'),('back-top','back'),('back','hind-leg'),('hind-leg','hind-paw')):self.relate('connect',a,b)
        self.add_line('forearm',(22,17),(22,36));self.relate('connect','forearm','head')
        self.add_arc('forepaw',(22,36),(30,36),radius_x=4,sweep=False);self.relate('connect','forepaw','forearm')
        self.add_line('fingers',(30,36),(30,32));self.relate('connect','forepaw','fingers')
        self.add_line('branch',(4,26),(13,26));self.relate('connect','branch','head')
        self.add_dot('nose',(13,17))
