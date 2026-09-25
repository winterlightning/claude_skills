"""A tapered bucket with paint spilling over its right rim. SQUARE extremes (6,6)-(42,42). Lucide paint-bucket informs the connected overflow silhouette; retain the source upright bucket, thick rim and two wavy drip lobes. The spill is intentionally asymmetric."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aebdb949-dd90-42b9-8053-6c7b6b0e29e8'
SOURCE_PATH = 'pictographic-primitives/symbol/paint_aebdb949-dd90-42b9-8053-6c7b6b0e29e8.svg'
AUTHOR = 'gpt-6'


class PaintBucketSpill(Solo48):
    icon_id = 'paint-bucket-spill'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    aliases = ()
    keywords = ('paint', 'bucket', 'spill', 'fill', 'color', 'drip', 'decorate', 'design')

    def build(self) -> None:
        self.add_arc('lip-tl',(6,10),(10,6),radius_x=4)
        self.add_line('lip-top',(10,6),(32,6))
        self.add_arc('spill-top',(32,6),(42,16),radius_x=10)
        self.add_line('spill-right',(42,16),(42,24))
        self.add_arc('spill-br',(42,24),(38,28),radius_x=4)
        self.add_arc('spill-bl',(38,28),(34,24),radius_x=4)
        self.add_line('spill-rise',(34,24),(32,21))
        self.add_arc('drip',(32,21),(24,21),radius_x=4)
        self.add_line('drip-left',(24,21),(24,15))
        self.add_line('lip-inner',(24,15),(10,15))
        self.add_arc('lip-bl',(10,15),(6,11),radius_x=4)
        self.add_line('lip-left',(6,11),(6,10))
        self.add_contour('paint','lip-tl','lip-top','spill-top','spill-right','spill-br','spill-bl','spill-rise','drip','drip-left','lip-inner','lip-bl','lip-left',closed=True)
        self.add_polyline('bucket',(10,15),(14,42),(36,42),(38,28))
        self.relate('connect','paint','bucket')
