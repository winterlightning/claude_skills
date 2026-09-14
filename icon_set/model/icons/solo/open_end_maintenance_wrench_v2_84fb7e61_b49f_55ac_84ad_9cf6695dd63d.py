"""An open-end wrench with a broad crescent jaw and diagonal rounded-end handle; minor surface marks omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '84fb7e61-b49f-55ac-84ad-9cf6695dd63d'
SOURCE_PATH = 'pictographic-primitives/tools/tools wrench_84fb7e61-b49f-55ac-84ad-9cf6695dd63d.svg'
AUTHOR = 'gpt-6'

class OpenEndMaintenanceWrenchV2(Solo48):
    icon_id = 'open-end-maintenance-wrench-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ()
    keywords = ('wrench', 'open-end wrench', 'spanner', 'repair', 'maintenance', 'mechanic', 'fix', 'tool')

    def build(self) -> None:


        self.add_arc('crown',(30,6),(18,18),radius_x=12,sweep=False)
        self.add_line('neck-a',(18,18),(20,24))
        self.add_line('handle-a',(20,24),(6,36))
        self.add_arc('butt',(6,36),(12,42),radius_x=6,sweep=False)
        self.add_line('handle-b',(12,42),(24,28))
        self.add_line('neck-b',(24,28),(30,30))
        self.add_arc('chin',(30,30),(42,18),radius_x=12,sweep=False)
        self.add_line('lip-a',(42,18),(42,10))
        self.add_line('jaw-a',(42,10),(34,18))
        self.add_line('jaw-seat',(34,18),(28,12))
        self.add_line('jaw-b',(28,12),(36,6))
        self.add_line('lip-b',(36,6),(30,6))
        self.add_contour('outline','crown','neck-a','handle-a','butt','handle-b','neck-b','chin','lip-a','jaw-a','jaw-seat','jaw-b','lip-b',closed=True)
