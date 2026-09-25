"""A chamfered engine with a top cap and left connector. Broad keyshape suits the engine silhouette; no useful exact Lucide match. Deliberate cast corners retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '01799e2a-1842-529a-aa77-97d0b896a43d'
SOURCE_PATH = 'pictographic-primitives/transportation/car engine_01799e2a-1842-529a-aa77-97d0b896a43d.svg'
SOURCE_REFERENCES = (('01799e2a-1842-529a-aa77-97d0b896a43d', 'pictographic-primitives/transportation/car engine_01799e2a-1842-529a-aa77-97d0b896a43d.svg'),)
AUTHOR = 'gpt-6'

class EngineWarningSymbol(Solo48):
    icon_id = 'engine-warning-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('engine', 'check engine', 'warning', 'motor', 'dashboard', 'car', 'malfunction', 'indicator')

    def build(self) -> None:
        self.add_polyline('block',(12,16),(26,16),(34,16),(38,22),(44,22),(44,40),(22,40),(12,30),(12,28),(12,16),closed=True)
        self.add_polyline('cap',(20,8),(26,8),(32,8))
        self.add_line('neck',(26,8),(26,16))
        self.add_polyline('port',(4,20),(4,28),(4,36))
        self.add_line('connector',(4,28),(12,28))
        for a,b in [('neck','cap'),('neck','block'),('connector','port'),('connector','block')]:
            self.relate('connect',a,b)
