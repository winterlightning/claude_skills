"""A wider smartphone storefront with an open screen and roomy awning panels.

VRECT_XL: ink (4,0)-(60,64). Body centerline width increases from 34 to 40.
Lucide store and smartphone originals and atomic-debug informed mirrored panels
and rounded phone corners. Remove the optional awning band and bezel divider
so the screen remains one open area. Keep four panels and a centered home dot.
Symbol plan: canopy owns mirrored panel seams and cardinal phone attachments;
phone owns its paired corners and home mark. Parent remains unchanged.
Hosting (compose.py): plus blocked; heart blocked; check blocked.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (smartphone-with-store-awning VRECT_XL -> VRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = 'e8d293a0-8723-40a8-943c-5339aa55feb8'
SOURCE_PATH = 'container_icons/svg/smartphone-with-store-awning-e8d293a0-8723-40a8-943c-5339aa55feb8.svg'
AUTHOR = 'claude-opus-5-5'


class SmartphoneWithStoreAwning(Container64):
    icon_id = 'smartphone-with-store-awning'
    keyshape = Keyshape.VRECT_L
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('smartphone', 'store', 'awning', 'shopping')

    def build(self) -> None:
        self.add_line('canopy-top', (16, 4), (48, 4))
        self.add_arc('canopy-ne', (48, 4), (52, 8), radius_x=4)
        self.add_line('canopy-right', (52, 8), (54, 16))
        self.add_arc('lobe-0', (54, 16), (43, 16), radius_x=6)
        self.add_arc('lobe-1', (43, 16), (31, 16), radius_x=6)
        self.add_arc('lobe-2', (31, 16), (21, 16), radius_x=6)
        self.add_arc('lobe-3', (21, 16), (10, 16), radius_x=6)
        self.add_line('canopy-left', (10, 16), (12, 8))
        self.add_arc('canopy-nw', (12, 8), (16, 4), radius_x=4)
        self.add_line('panel-seam-0', (24, 4), (21, 16))
        self.add_line('panel-seam-1', (32, 4), (31, 16))
        self.add_line('panel-seam-2', (40, 4), (43, 16))
        self.add_line('body-right', (48, 22), (48, 54))
        self.add_arc('body-se', (48, 54), (42, 60), radius_x=6)
        self.add_line('body-base', (42, 60), (22, 60))
        self.add_arc('body-sw', (22, 60), (16, 54), radius_x=6)
        self.add_line('body-left', (16, 54), (16, 22))
        self.add_dot('home', (32, 52))
        self.add_contour('canopy', 'canopy-top', 'canopy-ne', 'canopy-right', 'lobe-0', 'lobe-1', 'lobe-2', 'lobe-3', 'canopy-left', 'canopy-nw', closed=True)
        self.add_contour('body', 'body-right', 'body-se', 'body-base', 'body-sw', 'body-left')
        self.relate('connect', 'panel-seam-0', 'canopy')
        self.relate('connect', 'panel-seam-1', 'canopy')
        self.relate('connect', 'panel-seam-2', 'canopy')
        self.relate('connect', 'body', 'canopy')
