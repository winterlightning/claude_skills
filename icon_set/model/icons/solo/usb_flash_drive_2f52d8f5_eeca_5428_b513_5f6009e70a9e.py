"""An upright USB flash drive has a two-contact metal plug and rounded body.

Keyshape VRECT_M: visible extremes (9, 0, 39, 48).
Tall keyshape preserves memory-stick silhouette. Lucide cable: stepped connector; memory-stick: sparse repeated contact marks. Pins reduced to round dots."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2f52d8f5-eeca-5428-b513-5f6009e70a9e'
SOURCE_PATH = 'pictographic-primitives/computers/batch-06/flash drive_2f52d8f5-eeca-5428-b513-5f6009e70a9e.svg'
AUTHOR = 'astra-chatgpt'


class UsbFlashDrive(Solo48):
    icon_id = 'usb-flash-drive'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ()
    keywords = ('usb', 'flash drive', 'memory stick', 'thumb drive', 'storage', 'portable', 'data', 'hardware')

    def build(self) -> None:
        self.add_line('body-top1', (17, 18), (31, 18))
        self.add_arc('body-ne', (31, 18), (37, 24), radius_x=6, sweep=True)
        self.add_line('body-right', (37, 24), (37, 40))
        self.add_arc('body-se', (37, 40), (31, 46), radius_x=6, sweep=True)
        self.add_line('body-bottom0', (31, 46), (17, 46))
        self.add_arc('body-sw', (17, 46), (11, 40), radius_x=6, sweep=True)
        self.add_line('body-left', (11, 40), (11, 24))
        self.add_arc('body-nw', (11, 24), (17, 18), radius_x=6, sweep=True)
        self.add_contour('body', 'body-top1', 'body-ne', 'body-right', 'body-se', 'body-bottom0', 'body-sw', 'body-left', 'body-nw', closed=True)
        self.add_polyline('plug', (17, 18), (15, 18), (15, 2), (33, 2), (33, 18), (31, 18), closed=False)
        self.relate("connect", 'body', 'plug')
        self.add_dot('pin-left', (21, 10))
        self.add_dot('pin-right', (27, 10))
