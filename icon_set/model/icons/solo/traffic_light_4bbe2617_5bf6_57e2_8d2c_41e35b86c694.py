from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4bbe2617-5bf6-57e2-8d2c-41e35b86c694'
SOURCE_PATH = 'pictographic-primitives/transportation/road traffic lights_4bbe2617-5bf6-57e2-8d2c-41e35b86c694.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = [{'source_icon_id': '4bbe2617-5bf6-57e2-8d2c-41e35b86c694', 'source_path': 'pictographic-primitives/transportation/road traffic lights_4bbe2617-5bf6-57e2-8d2c-41e35b86c694.svg'}]

class TrafficLight(Solo48):
    icon_id = 'traffic-light'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('traffic light', 'signal', 'stoplight', 'road', 'intersection', 'traffic', 'lights', 'junction')

    def build(self):
        self.add_line('top',(16,4),(32,4))
        self.add_arc('upper-right',(32,4),(40,12),radius_x=8)
        self.add_line('right',(40,12),(40,36))
        self.add_arc('lower-right',(40,36),(32,44),radius_x=8)
        self.add_line('bottom',(32,44),(16,44))
        self.add_arc('lower-left',(16,44),(8,36),radius_x=8)
        self.add_line('left',(8,36),(8,12))
        self.add_arc('upper-left',(8,12),(16,4),radius_x=8)
        self.add_contour('housing','top','upper-right','right','lower-right','bottom','lower-left','left','upper-left',closed=True)
        for y in (14,24,34):self.add_dot(f'lamp-{y}',(24,y))
