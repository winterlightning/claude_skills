"""An upright spark plug with a terminal, insulator, hex collar, shank and hooked electrode. Lucide plug informed axial construction. Tall keyshape provides stacked parts; tiny ribs and threads omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8caafeb7-46da-587d-a88f-a19b89dab303'
SOURCE_PATH = 'pictographic-primitives/transportation/car tool spark plug_8caafeb7-46da-587d-a88f-a19b89dab303.svg'
SOURCE_REFERENCES = (('8caafeb7-46da-587d-a88f-a19b89dab303', 'pictographic-primitives/transportation/car tool spark plug_8caafeb7-46da-587d-a88f-a19b89dab303.svg'),)
AUTHOR = 'gpt-6'

class SparkPlug(Solo48):
    icon_id = 'spark-plug'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('spark plug', 'ignition', 'engine', 'car', 'tool', 'mechanic', 'automotive', 'repair')

    def build(self) -> None:
        self.add_polyline('collar',(8,24),(12,20),(16,20),(32,20),(36,20),(40,24),(36,28),(30,28),(18,28),(12,28),(8,24),closed=True)
        self.add_polyline('insulator',(16,20),(16,12),(20,12),(28,12),(32,12),(32,20))
        self.add_polyline('terminal',(20,12),(20,4),(28,4),(28,12))
        self.add_polyline('shank',(18,28),(18,36),(24,36),(30,36),(30,28))
        self.add_polyline('electrode',(30,36),(36,36),(36,44),(20,44))
        for a,b in [('insulator','collar'),('terminal','insulator'),('shank','collar'),('electrode','shank')]:
            self.relate('connect',a,b)
