from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '31365d03-9337-46e3-ba44-717c5d44d4ea'
SOURCE_PATH = 'pictographic-primitives/transportation/scooter fast_31365d03-9337-46e3-ba44-717c5d44d4ea.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = [{'source_icon_id': '31365d03-9337-46e3-ba44-717c5d44d4ea', 'source_path': 'pictographic-primitives/transportation/scooter fast_31365d03-9337-46e3-ba44-717c5d44d4ea.svg'}]

class SpeedingKickScooter(Solo48):
    icon_id = 'speeding-kick-scooter'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('kick scooter', 'scooter', 'fast', 'speed', 'e-scooter', 'micromobility', 'motion', 'ride')

    def build(self):
        for x,side in ((9,'rear'),(39,'front')):
            self.add_arc(side+'-wheel-a',(x,30),(x,40),radius_x=5)
            self.add_arc(side+'-wheel-b',(x,40),(x,30),radius_x=5)
            self.add_contour(side+'-wheel',side+'-wheel-a',side+'-wheel-b',closed=True)
        
        self.add_polyline('handle-column',(25,8),(31,8),(35,19),(39,30))
        self.add_polyline('deck',(9,30),(21,30),(27,30))
        self.add_arc('deck-bend',(27,30),(35,22),radius_x=8,sweep=False)
        self.add_line('riser',(35,22),(35,19))
        self.add_contour('front-step','deck-bend','riser')
        for a,b in (('deck','rear-wheel'),('deck','front-step'),('front-step','handle-column'),('handle-column','front-wheel')):self.relate('connect',a,b)
        
        self.add_line('speed-upper',(8,10),(17,10))
        self.add_line('speed-lower',(4,18),(17,18))
