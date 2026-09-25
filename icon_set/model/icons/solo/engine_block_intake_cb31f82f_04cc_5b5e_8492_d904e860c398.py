"""A chamfered engine with a rectangular intake, left port and right connector. Broad keyshape preserves asymmetric fittings. No useful exact Lucide match; small cast details omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cb31f82f-04cc-5b5e-8492-d904e860c398'
SOURCE_PATH = 'pictographic-primitives/transportation/car engine_cb31f82f-04cc-5b5e-8492-d904e860c398.svg'
SOURCE_REFERENCES = (('cb31f82f-04cc-5b5e-8492-d904e860c398', 'pictographic-primitives/transportation/car engine_cb31f82f-04cc-5b5e-8492-d904e860c398.svg'),)
AUTHOR = 'gpt-6'

class EngineBlockIntake(Solo48):
    icon_id = 'engine-block-intake'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('engine', 'motor', 'engine block', 'car', 'mechanic', 'repair', 'dashboard', 'automotive')

    def build(self) -> None:
        self.add_polyline('intake',(14,8),(34,8),(34,16),(30,16),(18,16),(14,16),(14,8),closed=True)
        self.add_polyline('block',(12,24),(18,24),(30,24),(36,24),(36,32),(36,40),(20,40),(12,32),(12,24),closed=True)
        for x in (18,30):
            self.add_line(f'support-{x}',(x,16),(x,24))
            self.relate('connect',f'support-{x}','intake')
            self.relate('connect',f'support-{x}','block')
        self.add_polyline('port',(12,24),(4,24),(4,32),(12,32))
        self.relate('connect','port','block')
        self.add_polyline('end',(44,24),(44,32),(44,40))
        self.add_line('connector',(36,32),(44,32))
        self.relate('connect','connector','end')
        self.relate('connect','connector','block')
