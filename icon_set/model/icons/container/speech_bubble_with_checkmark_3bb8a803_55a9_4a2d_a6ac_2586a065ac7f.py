"""Checked message in a rounded bubble with lower-right tail.
HRECT_L extremes (2,10)-(62,54); body floor 42. Lucide message-square-text
informs continuous outline, tangent corners and detached message strokes.
Preserve whole subject per recorded user classification. Shared row step 8.
Hosting: plus-sign-state-131 and check-mark fail clearance; heart-state-63
is unresolved review (3 warnings). This filled message bubble hosts none of
these tested glyphs. Hosting reports are retained with queue batch evidence.
"""
from ._base import Container64
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '3bb8a803-55a9-4a2d-a6ac-2586a065ac7f'
SOURCE_PATH = 'pictographic-primitives/chat/criteria_3bb8a803-55a9-4a2d-a6ac-2586a065ac7f.svg'
AUTHOR = "gpt-6-astra"
class CheckedSpeechBubble(Container64):
    icon_id = "speech-bubble-with-checkmark"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "chat"
    categories = ("primitives", "chat")
    aliases = ["Speech Bubble with Checkmark"]
    keywords = ("speech", "bubble", "checkmark", "message")
    def build(self):
        self.add_line("top",(6,10),(58,10))
        self.add_arc("ne",(58,10),(62,14),radius_x=4)
        self.add_line("tail-1",(62,14),(62,54))
        self.add_line("tail-2",(62,54),(50,42))
        self.add_line("tail-3",(50,42),(6,42))
        self.add_arc("sw",(6,42),(2,38),radius_x=4)
        self.add_line("left",(2,38),(2,14))
        self.add_arc("nw",(2,14),(6,10),radius_x=4)
        self.add_contour("bubble","top","ne","tail-1","tail-2","tail-3","sw","left","nw",closed=True)
        self.add_polyline("check",(12,26),(17,31),(26,22))
        for i in range(2): self.add_line(f"message-{i}",(36,22+i*8),(52,22+i*8))
