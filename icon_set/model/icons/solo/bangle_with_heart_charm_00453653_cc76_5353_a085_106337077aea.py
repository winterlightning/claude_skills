"""Circular bangle with bottom heart charm. VRECT_XL (5,2)-(43,46) leaves room for the charm below the band. Symmetric lobes, informed by Lucide heart; no identity features omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '00453653-cc76-5353-a085-106337077aea'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-04/bracelet with heart_00453653-cc76-5353-a085-106337077aea.svg'
AUTHOR = 'astra-chatgpt'


class BangleWithHeartCharm(Solo48):
    icon_id = 'bangle-with-heart-charm'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('bracelet', 'bangle', 'heart', 'charm', 'jewellery', 'jewelry', 'love', 'accessory')

    def build(self) -> None:
        self.add_arc('band-left', (12, 34), (5, 21), radius_x=19, radius_y=19, sweep=True, large_arc=False)
        self.add_arc('band-top', (5, 21), (43, 21), radius_x=19, radius_y=19, sweep=True, large_arc=False)
        self.add_arc('band-right', (43, 21), (36, 34), radius_x=19, radius_y=19, sweep=True, large_arc=False)
        self.add_contour('band', 'band-left', 'band-top', 'band-right', closed=False)
        self.add_arc('charm-l', (24, 31), (12, 34), radius_x=6, radius_y=5, sweep=False, large_arc=False)
        self.add_line('charm-ls', (12, 34), (24, 46))
        self.add_line('charm-rs', (24, 46), (36, 34))
        self.add_arc('charm-r', (36, 34), (24, 31), radius_x=6, radius_y=5, sweep=False, large_arc=False)
        self.add_contour('charm', 'charm-l', 'charm-ls', 'charm-rs', 'charm-r', closed=True)
        self.relate("connect", 'band', 'charm')
