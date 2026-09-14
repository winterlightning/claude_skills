'Tall building: equal facade windows and a centred doorway; combine overly close window rows into clear vertical windows.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a76b1092-d6c9-5a9e-96d8-28cb90a29bb6'
SOURCE_PATH = 'icons-json/office/building tall_a76b1092-d6c9-5a9e-96d8-28cb90a29bb6.json'
AUTHOR = 'gpt-6'

class BuildingTall(Solo48):
    icon_id = 'building-tall'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('building', 'tall', 'office')

    def build(self) -> None:
        self.add_polyline('building',(10,42),(10,6),(38,6),(38,42))
        self.add_polyline('ground',(6,42),(10,42),(20,42),(28,42),(38,42),(42,42))
        self.relate('connect','building','ground')
        self.add_polyline('door',(20,42),(20,34),(28,34),(28,42));self.relate('connect','door','ground')
        for i,x in enumerate((19,29)):
            self.add_line(f'window-{i}',(x,15),(x,24))
