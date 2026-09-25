"""A diagonal flared flashlight casts three short light rays; tiny switch omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '23a67709-106e-52c7-8f6e-a86374ca7b1b'
SOURCE_PATH = 'pictographic-primitives/tools/handheld torch_23a67709-106e-52c7-8f6e-a86374ca7b1b.svg'
AUTHOR = 'gpt-6'

class FlashlightWithRays(Solo48):
    icon_id = 'flashlight-with-rays'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "tools"
    aliases = ()
    keywords = ('flashlight', 'torch', 'light', 'beam', 'rays', 'lamp', 'handheld', 'illumination')

    def build(self) -> None:
        self.add_polyline('body',(6,32),(18,20),(18,12),(26,20),(36,30),(28,30),(16,42),closed=True)
        self.add_line('ray-middle',(36,12),(42,6))
        self.add_line('ray-top',(26,6),(26,8))
        self.add_line('ray-right',(40,22),(42,22))
