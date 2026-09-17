"""USB Plug: A narrow rectangular metal connector projects above a wider rounded housing. The housing has short upright sides and a broad curved lower end, with no interior markings.

Construction: Blank USB connector retains rectangular upper plug and wide body with rounded bottom.
Keyshape: VRECT_L; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'e4b1f036-4c20-4e55-975c-b249f0a098fc'
SOURCE_PATH = 'pictographic-primitives/state/usb_e4b1f036-4c20-4e55-975c-b249f0a098fc.svg'
AUTHOR = 'gpt-6'


class UsbPlugState289(Sub32):
    icon_id = 'usb-plug-state-289'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives/shape'
    aliases = ()
    keywords = ('usb', 'plug', 'narrow', 'rectangular', 'metal', 'connector', 'projects', 'wider')

    def build(self):
        self.add_polyline('plug',(10,10),(10,2),(22,2),(22,10))
        self.add_line('top',(6,10),(26,10))
        self.add_line('right',(26,10),(26,22))
        self.add_arc('lower-right',(26,22),(18,30),radius_x=8)
        self.add_line('bottom',(18,30),(14,30))
        self.add_arc('lower-left',(14,30),(6,22),radius_x=8)
        self.add_line('left',(6,22),(6,10))
        self.add_contour('body','top','right','lower-right','bottom','lower-left','left',closed=True)
        self.relate('connect','body','plug')
