"""Police car front; independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8f7bb524-ecd7-5e4a-9fb5-4d56729683d8'
SOURCE_PATH = 'pictographic-primitives/transportation/police_8f7bb524-ecd7-5e4a-9fb5-4d56729683d8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = [{'SOURCE_ICON_ID': '8f7bb524-ecd7-5e4a-9fb5-4d56729683d8', 'SOURCE_PATH': 'pictographic-primitives/transportation/police_8f7bb524-ecd7-5e4a-9fb5-4d56729683d8.svg', 'AUTHOR': 'gpt-6'}]

class PoliceCarFront(Solo48):
    icon_id = 'police-car-front'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('police', 'car', 'front')

    def build(self) -> None:
        # VRECT_L centerline (8,6)-(40,42). A stepped roof lightbar leaves room for three rays.
        self.add_polyline('body',(8,26),(12,26),(36,26),(40,26),(40,42),(34,42),(14,42),(8,42),closed=True)
        self.add_polyline('windscreen-lightbar',(12,26),(16,18),(18,18),(18,14),(30,14),(30,18),(32,18),(36,26))
        self.relate('connect','body','windscreen-lightbar')
        for name,x in [('left',14),('right',34)]:
            self.add_line(name+'-wheel',(x,42),(x,44))
            self.relate('connect',name+'-wheel','body')
        self.add_dot('left-headlight',(17,34))
        self.add_dot('right-headlight',(31,34))
        self.add_line('left-ray',(8,6),(10,6))
        self.add_dot('top-ray',(24,6))
        self.add_line('right-ray',(38,6),(40,6))
