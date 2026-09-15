'Beach parasol and sea: preserve the intentional tilt and flowing canopy; replace jagged waves with repeated smooth curves and separate the shoreline. Lucide umbrella informs the canopy.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9acf6d75-fd0b-5669-bda9-3051aa82ac0b'
SOURCE_PATH = 'pictographic-primitives/outdoors/beach parasol water_9acf6d75-fd0b-5669-bda9-3051aa82ac0b.svg'
AUTHOR = 'gpt-6'

class BeachParasolWater(Solo48):
    icon_id = 'beach-parasol-water'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('beach', 'parasol', 'water', 'outdoors')

    def build(self) -> None:
        # Intentional beach-parasol tilt; the canopy is curved, the sea is a smooth wave.
        self.add_bezier('canopy-left',(10,24),((10,16),(16,9),(24,9)))
        self.add_bezier('canopy-right',(24,9),((31,9),(38,11),(42,14)))
        self.add_line('hem-right',(42,14),(26,19))
        self.add_line('hem-left',(26,19),(10,24))
        self.add_contour('canopy','canopy-left','canopy-right','hem-right','hem-left',closed=True)
        self.add_line('finial',(22,6),(24,9))
        self.relate('connect','finial','canopy')
        self.add_line('pole',(26,19),(30,30))
        self.relate('connect','pole','canopy')
        self.add_bezier('sand-left',(21,30),((24,28),(27,30),(30,30)))
        self.add_line('sand-right',(30,30),(42,30))
        self.add_contour('sand','sand-left','sand-right')
        self.relate('connect','pole','sand')
        self.add_bezier('water',(6,42),((9,42),(9,39),(12,39)),((15,39),(15,42),(18,42)),((21,42),(21,39),(24,39)),((27,39),(27,42),(30,42)),((33,42),(33,39),(36,39)),((39,39),(39,42),(42,42)))
