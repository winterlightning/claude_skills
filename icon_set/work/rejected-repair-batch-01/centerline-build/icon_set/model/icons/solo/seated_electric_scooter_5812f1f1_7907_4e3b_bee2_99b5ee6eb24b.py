from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5812f1f1-7907-4e3b-bee2-99b5ee6eb24b'
SOURCE_PATH = 'pictographic-primitives/transportation/scooter_5812f1f1-7907-4e3b-bee2-99b5ee6eb24b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = [{'source_icon_id': '5812f1f1-7907-4e3b-bee2-99b5ee6eb24b', 'source_path': 'pictographic-primitives/transportation/scooter_5812f1f1-7907-4e3b-bee2-99b5ee6eb24b.svg'}, {'source_icon_id': '5bb1d819-f639-5710-b79c-4a5588a93413', 'source_path': 'pictographic-primitives/transportation/scooter_5bb1d819-f639-5710-b79c-4a5588a93413.svg'}, {'source_icon_id': 'd6210a26-eb50-487c-ac0e-92d2740ac02c', 'source_path': 'pictographic-primitives/transportation/scooter_d6210a26-eb50-487c-ac0e-92d2740ac02c.svg'}]

class SeatedElectricScooter(Solo48):
    icon_id = 'seated-electric-scooter'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('e-scooter', 'electric scooter', 'seated scooter', 'scooter', 'micromobility', 'ride', 'two wheels', 'commute')

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
        
        self.add_polyline('seat',(12,20),(17,20),(22,20))
        self.add_line('seat-post',(17,20),(21,30))
        self.relate('connect','seat','seat-post')
        self.relate('connect','seat-post','deck')
