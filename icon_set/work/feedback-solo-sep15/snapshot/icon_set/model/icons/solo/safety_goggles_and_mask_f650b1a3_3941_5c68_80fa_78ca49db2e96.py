"""A head wearing joined goggles and a respirator; ears and tiny straps omitted, mask straps join the goggles physically."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f650b1a3-3941-5c68-80fa-78ca49db2e96'
SOURCE_PATH = 'pictographic-primitives/tools/equipment safety mask_f650b1a3-3941-5c68-80fa-78ca49db2e96.svg'
AUTHOR = 'gpt-6'

class SafetyGogglesAndMask(Solo48):
    icon_id = 'safety-goggles-and-mask'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ()
    keywords = ('safety', 'goggles', 'mask', 'respirator', 'protective', 'ppe', 'equipment', 'face')

    def build(self) -> None:
        self.add_arc('crown',(8,20),(40,20),radius_x=16)
        self.add_polyline('goggles',(8,20),(8,30),(12,32),(24,28),(36,32),(40,30),(40,20),(8,20))
        self.relate('connect','crown','goggles')
        self.add_arc('mask-bottom',(36,32),(12,32),radius_x=12)
        self.relate('connect','mask-bottom','goggles')
