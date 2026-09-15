'Rising dashed curve: preserve the winding path and arrow direction using fewer longer, smoothly shaped dashes with clear gaps.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '798bcbde-2493-4ba9-a894-3acb44b2dbd2'
SOURCE_PATH = 'pictographic-primitives/arrows/curve rise dash large head_798bcbde-2493-4ba9-a894-3acb44b2dbd2.svg'
AUTHOR = 'gpt-6'

class CurveRiseDashLargeHead(Solo48):
    icon_id = 'curve-rise-dash-large-head'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('curve', 'rise', 'dash', 'large', 'head', 'arrows')

    def build(self) -> None:
        self.add_bezier('start',(4,13),((6,11),(8,11),(10,12)))
        self.add_bezier('middle',(16,20),((18,23),(18,27),(18,30)))
        self.add_bezier('bend',(23,38),((25,40),(27,40),(29,40)),((32,40),(35,37),(36,34)))
        self.add_line('shaft',(38,26),(38,8))
        self.add_polyline('head',(32,14),(38,8),(44,14))
        self.relate('connect','shaft','head')
