"""Light Bulb reconstructed from the supplied reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '35687e59-ecf7-59ae-9463-52874a252eed'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__light-bulb-35687e59-ecf7-59ae-9463-52874a252eed/20260927T072903Z-thuan-mac-1/reference/light bulb_35687e59-ecf7-59ae-9463-52874a252eed.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'light-bulb-35687e59-ecf7-59ae-9463-52874a252eed-solo'
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "lights"
    categories = ("lights", "primitives")
    aliases = ()
    keywords = ('bulb', 'light', 'lamp', 'electric', 'glass', 'base')
    keyshape = Keyshape.SQUARE

    def build(self):
        # A glass globe narrows to a separate, rounded screw socket.
        self.add_bezier('left-neck',(18,32),((18,27),(6,28),(6,19)))
        self.add_arc('glass-top',(6,19),(42,19),radius_x=18,radius_y=13)
        self.add_bezier('right-neck',(42,19),((42,28),(30,27),(30,32)))
        self.add_line('socket-right',(30,32),(30,38))
        self.add_arc('socket-br',(30,38),(26,42),radius_x=4)
        self.add_line('socket-base',(26,42),(22,42))
        self.add_arc('socket-bl',(22,42),(18,38),radius_x=4)
        self.add_line('socket-left',(18,38),(18,32))
        self.add_contour('bulb','left-neck','glass-top','right-neck','socket-right',
                         'socket-br','socket-base','socket-bl','socket-left',closed=True)
        self.add_line('socket-seam',(18,32),(30,32))
        self.relate('connect','bulb','socket-seam')
