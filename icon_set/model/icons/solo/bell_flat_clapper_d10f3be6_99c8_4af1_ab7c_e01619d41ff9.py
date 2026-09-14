"""Dome bell with a flat clapper. Lucide bell: curved shoulders, flared lip and detached clapper; minimal source silhouette retained.

SOLO48 VRECT_L, live visible envelope (6, 2, 42, 46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd10f3be6-99c8-4af1-ab7c-e01619d41ff9'
SOURCE_PATH = 'pictographic-primitives/symbol/ring_d10f3be6-99c8-4af1-ab7c-e01619d41ff9.svg'
AUTHOR = 'gpt-6'


class BellFlatClapper(Solo48):
    icon_id = 'bell-flat-clapper'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('bell', 'notification', 'alert', 'alarm', 'reminder', 'ring', 'sound', 'news')

    def build(self) -> None:

        self.add_arc('dome',(12,16),(36,16),radius_x=12)
        self.add_line('right-side',(36,16),(36,22))
        self.add_arc('right-flare',(36,22),(40,34),radius_x=20,sweep=False)
        self.add_line('lip',(40,34),(8,34))
        self.add_arc('left-flare',(8,34),(12,22),radius_x=20,sweep=False)
        self.add_line('left-side',(12,22),(12,16))
        self.add_contour('bell','dome','right-side','right-flare','lip','left-flare','left-side',closed=True)
        self.add_line('clapper',(20,42),(28,42))
