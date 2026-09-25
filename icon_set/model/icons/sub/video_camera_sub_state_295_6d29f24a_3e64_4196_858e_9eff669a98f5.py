"""Video Camera: A rectangular camera body joins a flared right-facing lens hood in one angular outline. A deep notch separates the top of the body from the hood's upper slope.

Construction: Square-edged source video camera has one continuous silhouette with the right wedge.
Keyshape: HRECT_L; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '6d29f24a-3e64-4196-858e-9eff669a98f5'
SOURCE_PATH = 'pictographic-primitives/state/video_6d29f24a-3e64-4196-858e-9eff669a98f5.svg'
AUTHOR = 'gpt-6'


class VideoCameraSubState295(Sub32):
    icon_id = 'video-camera-sub-state-295'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('video', 'camera', 'rectangular', 'body', 'joins', 'flared', 'right', 'facing')

    def build(self):
        self.add_polyline('camera',(2,6),(22,6),(22,12),(30,8),(30,24),(22,20),(22,26),(2,26),closed=True)
