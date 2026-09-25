"""A waste bin has straight sides, rounded lower corners, and a broad flat lid extending beyond its body. A small rounded rectangular handle rises centrally above the lid."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c4f5e438-1f3e-48c9-a099-e32f75678ef0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/trash_c4f5e438-1f3e-48c9-a099-e32f75678ef0.svg'
AUTHOR = 'gpt-6'


class Batch032Icon(Solo48):
    icon_id = 'waste-disposal-trash-bin-batch-032'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ('waste-disposal-trash-bin',)
    keywords = ('batch-032',)

    def build(self):
        # Symbol plan: Bin with shared lid attachments, centered handle and straight body; extrema (8,4)-(40,44).

        self.add_polyline('lid',(8,12),(12,12),(16,12),(32,12),(36,12),(40,12))
        self.add_line('handle-left',(16,12),(16,6))
        self.add_arc('handle-tl',(16,6),(18,4),radius_x=2)
        self.add_line('handle-top',(18,4),(30,4))
        self.add_arc('handle-tr',(30,4),(32,6),radius_x=2)
        self.add_line('handle-right',(32,6),(32,12))
        self.add_contour('handle','handle-left','handle-tl','handle-top','handle-tr','handle-right')
        self.add_bezier('body',(12,12),((12,22),(12,34),(12,40)),((12,43),(18,44),(20,44)))
        self.add_line('base',(20,44),(28,44))
        self.add_bezier('body-right',(28,44),((30,44),(36,43),(36,40)),((36,34),(36,22),(36,12)))
        self.add_contour('bucket','body','base','body-right')
        self.relate('connect','lid','handle')
        self.relate('connect','lid','bucket')
