"""A video camera silhouette has a broad rectangular body and a flared lens housing projecting to the right. The lens joins the body through a narrower neck, with no interior controls."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'baf5f25a-a2ba-4e11-94e1-cc2061f683b6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/video_baf5f25a-a2ba-4e11-94e1-cc2061f683b6.svg'
AUTHOR = 'gpt-6'


class Batch032Icon(Solo48):
    icon_id = 'video-camera-with-flared-lens-batch-032'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    aliases = ('video-camera-with-flared-lens',)
    keywords = ('batch-032',)

    def build(self):
        # Symbol plan: One camera outline with broad body and right flared lens; extrema (4,10)-(44,38).

        self.add_polyline('outline',(4,10),(28,10),(28,18),(44,10),(44,38),(28,30),(28,38),(4,38),closed=True)
