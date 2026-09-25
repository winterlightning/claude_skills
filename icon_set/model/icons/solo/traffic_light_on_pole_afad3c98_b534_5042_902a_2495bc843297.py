from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'afad3c98-b534-5042-902a-2495bc843297'
SOURCE_PATH = 'pictographic-primitives/transportation/road traffic lights_afad3c98-b534-5042-902a-2495bc843297.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = [{'source_icon_id': 'afad3c98-b534-5042-902a-2495bc843297', 'source_path': 'pictographic-primitives/transportation/road traffic lights_afad3c98-b534-5042-902a-2495bc843297.svg'}]

class TrafficLightOnPole(Solo48):
    icon_id = 'traffic-light-on-pole'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('traffic light', 'signal', 'stoplight', 'pole', 'road', 'intersection', 'traffic', 'junction')

    def build(self):
        self.add_line('top',(19,4),(29,4))
        self.add_arc('upper-right',(29,4),(33,8),radius_x=4)
        self.add_polyline('right-wall',(33,8),(33,13),(33,23),(33,34))
        self.add_arc('lower-right',(33,34),(29,38),radius_x=4)
        self.add_polyline('bottom',(29,38),(24,38),(19,38))
        self.add_arc('lower-left',(19,38),(15,34),radius_x=4)
        self.add_polyline('left-wall',(15,34),(15,23),(15,13),(15,8))
        self.add_arc('upper-left',(15,8),(19,4),radius_x=4)
        self.add_contour('upper','upper-left','top','upper-right')
        self.add_contour('lower-right-corner','lower-right')
        self.add_contour('lower-left-corner','lower-left')
        for a,b in (('upper','right-wall'),('right-wall','lower-right-corner'),('lower-right-corner','bottom'),('bottom','lower-left-corner'),('lower-left-corner','left-wall'),('left-wall','upper')):self.relate('connect',a,b)
        for y in (13,21,29):self.add_dot(f'lamp-{y}',(24,y))
        for y in (13,23):
            self.add_line(f'left-visor-{y}',(8,y),(15,y))
            self.add_line(f'right-visor-{y}',(33,y),(40,y))
            self.relate('connect',f'left-visor-{y}','left-wall')
            self.relate('connect',f'right-visor-{y}','right-wall')
        self.add_line('pole',(24,38),(24,44))
        self.relate('connect','pole','bottom')
