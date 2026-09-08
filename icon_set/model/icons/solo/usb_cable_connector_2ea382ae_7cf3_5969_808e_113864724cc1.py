"""A USB plug has a rounded grip and cable curling left.

Keyshape VRECT_M: visible extremes (9, 0, 39, 48).
Lucide cable: rounded plug and tangent cord bend. Source leftward cable retained; decorative grip stripe omitted to keep the short body open."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2ea382ae-7cf3-5969-808e-113864724cc1'
SOURCE_PATH = 'pictographic-primitives/computers/batch-06/usb cable_2ea382ae-7cf3-5969-808e-113864724cc1.svg'


class UsbCableConnector(Solo48):
    icon_id = 'usb-cable-connector'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ()
    keywords = ('usb', 'cable', 'connector', 'plug', 'cord', 'charging', 'port', 'computer')

    def build(self) -> None:
        self.add_polyline('tip', (20, 16), (20, 2), (34, 2), (34, 16), closed=False)
        self.add_line('tip-mark', (27, 8), (27, 9))
        self.add_line('body-top', (17, 16), (20, 16))
        self.add_line('body-top-mid', (20, 16), (34, 16))
        self.add_line('body-shoulder', (34, 16), (37, 16))
        self.add_line('body-top-r', (37, 16), (37, 25))
        self.add_arc('body-round-r', (37, 25), (27, 35), radius_x=10, sweep=True)
        self.add_arc('body-round-l', (27, 35), (17, 25), radius_x=10, sweep=True)
        self.add_line('body-left', (17, 25), (17, 16))
        self.add_contour('body', 'body-top', 'body-top-mid', 'body-shoulder', 'body-top-r', 'body-round-r', 'body-round-l', 'body-left', closed=True)
        self.relate("connect", 'tip', 'body')
        self.add_line('cable-top', (27, 35), (27, 36))
        self.add_arc('cable-bend', (27, 36), (17, 46), radius_x=10, sweep=True)
        self.add_line('cable-end', (17, 46), (11, 46))
        self.add_contour('cable', 'cable-top', 'cable-bend', 'cable-end', closed=False)
        self.relate("connect", 'body', 'cable')
