'Rising dashed curve: preserve the winding path and arrow direction using fewer longer, smoothly shaped dashes with clear gaps.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3fa5ffb0-58f1-4051-a2e2-5cee6442fff8'
SOURCE_PATH = 'pictographic-primitives/arrows/curve rise dash_3fa5ffb0-58f1-4051-a2e2-5cee6442fff8.svg'
AUTHOR = 'gpt-6'

class CurveRiseDash(Solo48):
    icon_id = 'curve-rise-dash'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('curve', 'rise', 'dash', 'arrows')

    def build(self) -> None:
        self.add_line('start',(4,23),(4,28))
        self.add_bezier('crest',(7,12),((9,9),(11,8),(13,8)),((17,8),(19,11),(20,14)))
        self.add_line('middle',(22,23),(22,28))
        self.add_bezier('bend',(25,37),((27,40),(29,40),(31,40)),((33,40),(35,39),(36,37)))
        self.add_line('shaft',(39,29),(39,15))
        self.add_polyline('head',(34,20),(39,15),(44,20))
        self.relate('connect','shaft','head')
