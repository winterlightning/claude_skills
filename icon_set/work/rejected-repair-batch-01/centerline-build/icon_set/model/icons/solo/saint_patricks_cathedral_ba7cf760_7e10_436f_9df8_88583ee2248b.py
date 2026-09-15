'Saint patricks cathedral: independent spacing revision.\n\nOpen the connector wall so the doorway clears both sides; preserve cross and spire.\nNative solo family, SQUARE keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ba7cf760-7e10-436f-9df8-88583ee2248b'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-01/saint patrick cathedral dublin 1_ba7cf760-7e10-436f-9df8-88583ee2248b.svg'
AUTHOR = 'gpt-6'

class Landmark(Solo48):
    icon_id = 'saint-patricks-cathedral'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'places/landmarks'
    aliases = ()
    keywords = ('saint patrick', 'dublin', 'cathedral', 'church', 'spire', 'gothic', 'landmark', 'religion')

    def build(self):
        self.add_polyline('outline',(6, 42),(6, 26),(16, 18),(28, 26),(34, 26),(34, 22),(38, 6),(42, 22),(42, 42),(22, 42),(14, 42),closed=True)
        self.add_polyline('cross-stem',(16, 6),(16, 10),(16, 18),closed=False)
        self.add_polyline('cross-bar',(12, 10),(16, 10),(20, 10),closed=False)
        self.add_polyline('door',(14, 42),(14, 34),(18, 30),(22, 34),(22, 42),closed=False)
        self.relate('connect','outline','cross-stem')
        self.relate('connect','cross-stem','cross-bar')
        self.relate('connect','outline','door')
