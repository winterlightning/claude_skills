# Independent revision; parent models preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'af38802b-7208-5060-b370-9b6f0871299d'
SOURCE_PATH = 'pictographic-primitives/computers/batch-04/mouse_af38802b-7208-5060-b370-9b6f0871299d.svg'
AUTHOR = 'gpt-6'

class CordedComputerMouseVariant2(Solo48):
    icon_id = 'corded-computer-mouse-v2'
    variant_of = 'corded-computer-mouse'
    variant_label = 'Exact keyshape envelope and clear spacing'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('mouse', 'corded', 'wired', 'cable', 'click', 'input', 'peripheral', 'computer')

    def build(self) -> None:
        # VRECT_L (8,4)-(40,44). Shared capsule axis and elliptical cap radii;
        # button seam and cable meet the same cap endpoints.
        x, left, right, upper, lower, rx, ry = 24, 8, 40, 24, 32, 16, 12
        self.add_arc('ne',(x,12),(right,upper),radius_x=rx,radius_y=ry)
        self.add_line('right',(right,upper),(right,lower))
        self.add_arc('se',(right,lower),(x,44),radius_x=rx,radius_y=ry)
        self.add_arc('sw',(x,44),(left,lower),radius_x=rx,radius_y=ry)
        self.add_line('left',(left,lower),(left,upper))
        self.add_arc('nw',(left,upper),(x,12),radius_x=rx,radius_y=ry)
        self.add_contour('body','ne','right','se','sw','left','nw',closed=True)
        self.add_line('cord',(x,4),(x,12))
        self.add_polyline('buttons',(left,upper),(x,upper),(right,upper))
        self.add_line('divider',(x,12),(x,upper))
        for part in ('cord','buttons','divider'):self.relate('connect','body',part)
        self.relate('connect','buttons','divider')
