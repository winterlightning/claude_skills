"""A waste bin has a wide horizontal lid with a rounded arch handle. Its sides taper toward a narrower flat base, and the lower corners are rounded around an empty front panel."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '167726ad-1712-4c93-9811-de2ccde29469'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/trash_167726ad-1712-4c93-9811-de2ccde29469.svg'
AUTHOR = 'gpt-6'


class Batch032Icon(Solo48):
    icon_id = 'waste-bin-with-lid-handle-batch-032'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/other"
    aliases = ('waste-bin-with-lid-handle',)
    keywords = ('batch-032',)

    def build(self):
        # Symbol plan: Bin with shared lid attachments, centered handle and tapered body; extrema (8,4)-(40,44).

        self.add_polyline('lid',(8,12),(12,12),(16,12),(32,12),(36,12),(40,12))
        self.add_arc('handle',(16,12),(32,12),radius_x=8)
        self.add_bezier('body',(12,12),((14,22),(16,34),(16,40)),((16,43),(18,44),(20,44)))
        self.add_line('base',(20,44),(28,44))
        self.add_bezier('body-right',(28,44),((30,44),(32,43),(32,40)),((32,34),(34,22),(36,12)))
        self.add_contour('bucket','body','base','body-right')
        self.relate('connect','lid','handle')
        self.relate('connect','lid','bucket')
