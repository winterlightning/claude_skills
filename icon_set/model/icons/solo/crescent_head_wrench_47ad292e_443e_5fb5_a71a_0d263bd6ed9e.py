"""A broad open-jaw wrench with diagonal rounded-end handle; adjustment screw omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '47ad292e-443e-5fb5-a71a-0d263bd6ed9e'
SOURCE_PATH = 'pictographic-primitives/tools/tools crescent wrench_47ad292e-443e-5fb5-a71a-0d263bd6ed9e.svg'
AUTHOR = 'gpt-6'

class CrescentHeadWrench(Solo48):
    icon_id = 'crescent-head-wrench'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ()
    keywords = ('wrench', 'crescent wrench', 'spanner', 'adjustable', 'repair', 'mechanic', 'hardware', 'tool')

    def build(self) -> None:
        self.add_arc('crown',(18,6),(30,18),radius_x=12)
        self.add_line('outer-1',(30, 18),(28, 24))
        self.add_line('outer-2',(28, 24),(42, 36))
        self.add_arc('butt',(42,36),(36,42),radius_x=6)
        self.add_line('inner-1',(36, 42),(24, 28))
        self.add_line('inner-2',(24, 28),(18, 30))
        self.add_arc('chin',(18,30),(6,18),radius_x=12)
        self.add_line('jaw-1',(6, 18),(6, 10))
        self.add_line('jaw-2',(6, 10),(14, 18))
        self.add_line('jaw-3',(14, 18),(20, 12))
        self.add_line('jaw-4',(20, 12),(12, 6))
        self.add_line('jaw-5',(12, 6),(18, 6))
        self.add_contour('outline','crown','outer-1','outer-2','butt','inner-1','inner-2','chin','jaw-1','jaw-2','jaw-3','jaw-4','jaw-5',closed=True)
