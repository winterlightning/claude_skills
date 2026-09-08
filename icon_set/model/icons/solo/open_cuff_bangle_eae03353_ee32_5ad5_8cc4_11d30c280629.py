"""An open cuff with a broad curved band and round tips. HRECT_XL extremes (2,5)-(46,43); mirrored elliptical quarters preserve the opening. No useful exact Lucide match."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eae03353-ee32-5ad5-8cc4-11d30c280629'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-05/bracelet_eae03353-ee32-5ad5-8cc4-11d30c280629.svg'
AUTHOR = 'astra-chatgpt'


class OpenCuffBangle(Solo48):
    icon_id = 'open-cuff-bangle'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('bracelet', 'bangle', 'cuff', 'jewellery', 'jewelry', 'wrist', 'accessory', 'band')

    def build(self) -> None:
        self.add_arc('outer-left', (14, 5), (2, 24), radius_x=12, radius_y=19, sweep=False)
        self.add_arc('outer-bottom', (2, 24), (46, 24), radius_x=22, radius_y=19, sweep=False)
        self.add_arc('outer-right', (46, 24), (34, 5), radius_x=12, radius_y=19, sweep=False)
        self.add_arc('tip-right', (34, 5), (34, 13), radius_x=4, radius_y=4, sweep=False)
        self.add_arc('inner-right', (34, 13), (38, 24), radius_x=4, radius_y=11, sweep=True)
        self.add_arc('inner-bottom', (38, 24), (10, 24), radius_x=14, radius_y=11, sweep=True)
        self.add_arc('inner-left', (10, 24), (14, 13), radius_x=4, radius_y=11, sweep=True)
        self.add_arc('tip-left', (14, 13), (14, 5), radius_x=4, radius_y=4, sweep=False)
        self.add_contour('band', 'outer-left', 'outer-bottom', 'outer-right', 'tip-right', 'inner-right', 'inner-bottom', 'inner-left', 'tip-left', closed=True)
