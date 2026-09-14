from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8e4523ec-5930-5e16-9e3e-d4c8dc935285'
SOURCE_PATH = 'pictographic-primitives/transportation/scooter 1_8e4523ec-5930-5e16-9e3e-d4c8dc935285.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = [{'source_icon_id': '8e4523ec-5930-5e16-9e3e-d4c8dc935285', 'source_path': 'pictographic-primitives/transportation/scooter 1_8e4523ec-5930-5e16-9e3e-d4c8dc935285.svg'}]

class MopedFacingLeft(Solo48):
    icon_id = 'moped-facing-left'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('moped', 'scooter', 'motor scooter', 'vehicle', 'two wheels', 'side view', 'commute', 'delivery')

    def build(self):
        for x,side in ((9,'rear'),(39,'front')):
            self.add_arc(side+'-wheel-a',(x,30),(x,40),radius_x=5)
            self.add_arc(side+'-wheel-b',(x,40),(x,30),radius_x=5)
            self.add_contour(side+'-wheel',side+'-wheel-a',side+'-wheel-b',closed=True)
        
        self.add_polyline('handle-column',(17,8),(11,8),(10,19),(9,30))
        self.add_polyline('deck',(10,19),(18,30),(27,30),(39,30),(44,30))
        self.add_line('body-front',(27,30),(32,18))
        self.add_arc('rear-shell',(32,18),(44,30),radius_x=12)
        self.add_contour('body','body-front','rear-shell')
        self.add_polyline('seat',(27,18),(32,18),(38,18))
        for a,b in (('handle-column','rear-wheel'),('handle-column','deck'),('deck','front-wheel'),('body','deck'),('body','seat')):self.relate('connect',a,b)
