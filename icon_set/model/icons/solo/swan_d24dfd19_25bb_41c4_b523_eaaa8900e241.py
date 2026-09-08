"""Swan with an open round body loop and sweeping neck. Bounds (2,5)-(46,43). Lucide bird: continuous breast curve, omit the eye."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd24dfd19-25bb-41c4-b523-eaaa8900e241'
SOURCE_PATH = 'pictographic-primitives/animals/swan_d24dfd19-25bb-41c4-b523-eaaa8900e241.svg'
AUTHOR = 'gpt-6'


class LoopedSwan(Solo48):
    icon_id = 'looped-swan'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('swan', 'bird', 'neck', 'curve', 'pond', 'elegant', 'waterfowl', 'loop')

    def build(self) -> None:
        self.add_arc('body-inner',(18,37),(26,29),radius_x=8,sweep=False)
        self.add_arc('body-top',(26,29),(14,21),radius_x=12,radius_y=8,sweep=False)
        self.add_arc('body-back',(14,21),(2,29),radius_x=12,radius_y=8,sweep=False)
        self.add_arc('body-bottom-left',(2,29),(24,43),radius_x=22,radius_y=14,sweep=False)
        self.add_arc('body-bottom-right',(24,43),(46,31),radius_x=22,radius_y=12,sweep=False)
        self.add_arc('breast',(46,31),(38,27),radius_x=18,sweep=False)
        self.add_arc('inner-neck',(38,27),(31,15),radius_x=15,sweep=True)
        self.add_arc('inner-head',(31,15),(37,15),radius_x=3,radius_y=3,sweep=True)
        self.add_arc('face',(37,15),(44,20),radius_x=7,sweep=False)
        self.add_line('beak',(44,20),(44,15))
        self.add_arc('head-right',(44,15),(34,5),radius_x=10,sweep=False)
        self.add_arc('head-left',(34,5),(24,15),radius_x=10,sweep=False)
        self.add_contour('swan','body-inner','body-top','body-back','body-bottom-left','body-bottom-right','breast','inner-neck','inner-head','face','beak','head-right','head-left')
