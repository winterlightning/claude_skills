"""Broadened the grip and opened the USB tip for a centered mark with margin above and below.

VRECT_L: visible ink (6, 2, 42, 46). Upright envelope accommodates the object’s vertical construction.
Lucide cable: stepped connector and tangent cable bend.
"""
# Independent revision; parent models preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2ea382ae-7cf3-5969-808e-113864724cc1'
SOURCE_PATH = 'pictographic-primitives/computers/batch-06/usb cable_2ea382ae-7cf3-5969-808e-113864724cc1.svg'
AUTHOR = 'gpt-6'

class UsbCableConnector(Solo48):
    icon_id = 'usb-cable-connector'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('usb', 'cable', 'connector', 'plug', 'cord', 'charging', 'port', 'computer')

    def build(self) -> None:
        # VRECT_L (8,4)-(40,44). Broad rounded grip and stepped USB tip;
        # one shared cable attachment joins a tangent quarter-circle bend.
        cx=28
        self.add_polyline('tip',(18,22),(18,4),(38,4),(38,22))
        self.add_polyline('top',(16,22),(18,22),(38,22),(40,22))
        self.add_line('right',(40,22),(40,24))
        self.add_arc('se',(40,24),(cx,36),radius_x=12)
        self.add_arc('sw',(cx,36),(16,24),radius_x=12)
        self.add_line('left',(16,24),(16,22))
        # Flatten the top polyline into the surrounding contour.
        self.contours.clear()
        self.add_contour('tip','tip-1','tip-2','tip-3')
        self.add_contour('body','top-1','top-2','top-3','right','se','sw','left',closed=True)
        self.add_dot('tip-mark',(cx,13))
        self.add_arc('cable-bend',(cx,36),(20,44),radius_x=8)
        self.add_line('cable-end',(20,44),(8,44))
        self.add_contour('cable','cable-bend','cable-end')
        self.relate('connect','tip','body')
        self.relate('connect','body','cable')
