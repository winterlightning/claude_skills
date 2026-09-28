"""controls-rewind-video: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ebe0d398-8e66-5e3c-8648-fb9e091f93f2'
SOURCE_PATH = 'pictographic-primitives/video/controls rewind_ebe0d398-8e66-5e3c-8648-fb9e091f93f2.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class ControlsRewindVideo(Solo48):
    icon_id = 'controls-rewind-video'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video'
    categories = ('video', 'primitives')
    aliases = ()
    keywords = ('controls', 'rewind', 'video')

    def build(self):
        # Plan: VRECT_L; three clean sides and exact horizontal symmetry.
        # Reference: Lucide pencil: deliberate straight edges; simple geometric triangle.
        self.add_polyline('triangle',(40,4),(8,24),(40,44),closed=True)
