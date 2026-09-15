"""Broadened the plug and body, retaining two contacts with eight-unit spacing and rounded lower corners.

VRECT_L: visible ink (6, 2, 42, 46). Upright envelope accommodates the object’s vertical construction.
Lucide cable: stepped plug and simple grip outline.
"""
# Independent revision; parent models preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2f52d8f5-eeca-5428-b513-5f6009e70a9e'
SOURCE_PATH = 'pictographic-primitives/computers/batch-06/flash drive_2f52d8f5-eeca-5428-b513-5f6009e70a9e.svg'
AUTHOR = 'gpt-6'

class UsbFlashDrive(Solo48):
    icon_id = 'usb-flash-drive'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('usb', 'flash drive', 'memory stick', 'thumb drive', 'storage', 'portable', 'data', 'hardware')

    def build(self) -> None:
        # VRECT_L (8,4)-(40,44). Shared axis and six-unit lower corners.
        # A 24-unit plug holds two equal contacts eight units apart.
        self.add_polyline('plug',(12,20),(12,4),(36,4),(36,20))
        self.add_polyline('top',(8,20),(12,20),(36,20),(40,20))
        self.add_line('right',(40,20),(40,38))
        self.add_arc('se',(40,38),(34,44),radius_x=6)
        self.add_line('bottom',(34,44),(14,44))
        self.add_arc('sw',(14,44),(8,38),radius_x=6)
        self.add_line('left',(8,38),(8,20))
        self.contours.clear()
        self.add_contour('plug','plug-1','plug-2','plug-3')
        self.add_contour('body','top-1','top-2','top-3','right','se','bottom','sw','left',closed=True)
        self.relate('connect','body','plug')
        for side,x in [('left',20),('right',28)]:self.add_dot('pin-'+side,(x,12))
