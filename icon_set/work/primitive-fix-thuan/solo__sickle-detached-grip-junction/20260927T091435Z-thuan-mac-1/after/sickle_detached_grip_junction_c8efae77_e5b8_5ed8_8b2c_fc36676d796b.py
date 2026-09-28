"""Sickle Harvesting Tool.
Plan: Deep crescent joined by a short connector to a distinct rounded grip. Extrema (6,6)-(42,42).
Reference: Supplied original; no useful exact local Lucide match. Sparse outline and shared attachment principles.
Reduction: Fine handle seam omitted; short connector preserves the separate grip.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c8efae77-e5b8-5ed8-8b2c-fc36676d796b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__sickle-detached-grip-junction/20260927T091435Z-thuan-mac-1/reference/forensic science sickle_c8efae77-e5b8-5ed8-8b2c-fc36676d796b.svg'
AUTHOR = 'gpt-6'

class Batch29Icon(Solo48):
    icon_id = 'sickle-detached-grip-junction'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "farming"
    categories = ("farming", "primitives")
    aliases = ()
    keywords = ('sickle', 'harvesting', 'tool')

    def build(self):

        self.add_bezier('outer',(18,6),((34,6),(42,13),(42,22)),((42,34),(30,37),(24,32)))
        self.add_bezier('inner',(24,32),((36,25),(32,13),(18,6)))
        self.add_contour('blade','outer','inner',closed=True)
        self.add_line('connector',(24,32),(20,36))
        self.relate('connect','blade','connector')
        self.add_line('grip-a-1',(20, 36),(14, 42))
        self.add_arc('grip-round',(14,42),(6,34),radius_x=8)
        self.add_line('grip-b',(6,34),(12,28))
        self.add_arc('grip-top',(12,28),(20,36),radius_x=6)
        self.add_contour('grip','grip-a-1','grip-round','grip-b','grip-top',closed=True)
        self.relate('connect','grip','connector')
