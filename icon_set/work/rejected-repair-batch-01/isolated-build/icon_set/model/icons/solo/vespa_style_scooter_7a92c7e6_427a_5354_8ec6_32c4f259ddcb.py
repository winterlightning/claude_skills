from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7a92c7e6-427a-5354-8ec6-32c4f259ddcb'
SOURCE_PATH = 'pictographic-primitives/transportation/scooter sport_7a92c7e6-427a-5354-8ec6-32c4f259ddcb.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = [{'source_icon_id': '7a92c7e6-427a-5354-8ec6-32c4f259ddcb', 'source_path': 'pictographic-primitives/transportation/scooter sport_7a92c7e6-427a-5354-8ec6-32c4f259ddcb.svg'}]

class VespaStyleScooter(Solo48):
    icon_id = 'vespa-style-scooter'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('scooter', 'vespa', 'motor scooter', 'moped', 'retro', 'vehicle', 'two wheels', 'side view')

    def build(self):
        for x,side in ((9,'rear'),(39,'front')):
            self.add_arc(side+'-wheel-a',(x,30),(x,40),radius_x=5)
            self.add_arc(side+'-wheel-b',(x,40),(x,30),radius_x=5)
            self.add_contour(side+'-wheel',side+'-wheel-a',side+'-wheel-b',closed=True)
        
        self.add_polyline('handle-column',(25,8),(31,8),(35,19),(39,30))
        self.add_polyline('deck',(4,30),(9,30),(20,30),(27,30))
        self.add_arc('deck-bend',(27,30),(35,22),radius_x=8,sweep=False)
        self.add_line('riser',(35,22),(35,19))
        self.add_contour('front-step','deck-bend','riser')
        self.add_arc('rear-shell',(4,30),(20,14),radius_x=16)
        self.add_line('body-front',(20,14),(20,30))
        self.add_contour('body','rear-shell','body-front')
        self.add_line('seat',(8,14),(20,14))
        for a,b in (('deck','rear-wheel'),('deck','front-step'),('front-step','handle-column'),('handle-column','front-wheel'),('body','deck'),('body','seat')):self.relate('connect',a,b)
