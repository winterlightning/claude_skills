"""Police car front; independently authored on SOLO48."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8f7bb524-ecd7-5e4a-9fb5-4d56729683d8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__police-car-front/20260927T153747Z-thuan-mac-1/reference/police_8f7bb524-ecd7-5e4a-9fb5-4d56729683d8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = [{'SOURCE_ICON_ID': '8f7bb524-ecd7-5e4a-9fb5-4d56729683d8', 'SOURCE_PATH': 'pictographic-primitives/transportation/police_8f7bb524-ecd7-5e4a-9fb5-4d56729683d8.svg', 'AUTHOR': 'gpt-6'}]

class PoliceCarFront(Solo48):
    icon_id = 'police-car-front'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('police', 'car', 'front')

    def build(self) -> None:
        # Frontal body, wide windshield, centered rooftop lamp and paired headlights.
        self.add_polyline('body', (6, 24), (42, 24), (42, 40), (6, 40), closed=True)
        self.add_polyline('windshield', (12, 24), (16, 14), (32, 14), (36, 24))
        self.relate('connect', 'body', 'windshield')
        self.add_polyline('lightbar', (20, 14), (20, 6), (28, 6), (28, 14))
        self.relate('connect', 'windshield', 'lightbar')
        self.add_dot('headlight-left', (14, 32))
        self.add_dot('headlight-right', (34, 32))
        self.add_line('wheel-left', (14, 40), (14, 42))
        self.add_line('wheel-right', (34, 40), (34, 42))
        self.relate('connect', 'body', 'wheel-left')
        self.relate('connect', 'body', 'wheel-right')
