'A wider smartphone storefront with an open screen and roomy awning panels.\n\nVRECT_XL: ink (4,0)-(60,64). Body centerline width increases from 34 to 40.\nLucide store and smartphone originals and atomic-debug informed mirrored panels\nand rounded phone corners. Remove the optional awning band and bezel divider\nso the screen remains one open area. Keep four panels and a centered home dot.\nSymbol plan: canopy owns mirrored panel seams and cardinal phone attachments;\nphone owns its paired corners and home mark. Parent remains unchanged.\nHosting (compose.py): plus blocked; heart blocked; check blocked.\n'
from ...keyshapes import Keyshape
from ._base import Container64
SOURCE_ICON_ID = 'e8d293a0-8723-40a8-943c-5339aa55feb8'
SOURCE_PATH = 'container_icons/svg/smartphone-with-store-awning-e8d293a0-8723-40a8-943c-5339aa55feb8.svg'
AUTHOR = 'gpt-6'

class SmartphoneWithStoreAwning(Container64):
    icon_id = 'smartphone-with-store-awning'
    keyshape = Keyshape.VRECT_XL
    category = 'container'
    aliases = ()
    keywords = ('smartphone', 'store', 'awning', 'shopping')

    def build(self):
        # Plan: broaden the phone and remove the optional top band and bottom
        # bezel divider. Four panel seams share one axis and mirrored nodes.
        axis, top, lip = 32, 2, 14
        self.add_line('canopy-top', (12, top), (52, top))
        self.add_arc('canopy-ne', (52, top), (56, 6), radius_x=4)
        self.add_line('canopy-right', (56, 6), (58, lip))
        edges = (58, 46, 32, 18, 6)
        lobes = []
        for j, (right, left) in enumerate(zip(edges, edges[1:])):
            name = f'lobe-{j}'
            self.add_arc(name, (right, lip), (left, lip), radius_x=(right-left)//2)
            lobes.append(name)
        self.add_line('canopy-left', (6, lip), (8, 6))
        self.add_arc('canopy-nw', (8, 6), (12, top), radius_x=4)
        self.add_contour('canopy', 'canopy-top', 'canopy-ne', 'canopy-right',
                         *lobes, 'canopy-left', 'canopy-nw', closed=True)
        for j, (upper_x, lower_x) in enumerate(((20,18),(axis,axis),(44,46))):
            name = f'panel-seam-{j}'
            self.add_line(name, (upper_x, top), (lower_x, lip))
            self.relate('connect', name, 'canopy')
        left, right, radius, bottom = 12, 52, 6, 62
        self.add_line('body-right', (right,20), (right,bottom-radius))
        self.add_arc('body-se', (right,bottom-radius), (right-radius,bottom), radius_x=radius)
        self.add_line('body-base', (right-radius,bottom), (left+radius,bottom))
        self.add_arc('body-sw', (left+radius,bottom), (left,bottom-radius), radius_x=radius)
        self.add_line('body-left', (left,bottom-radius), (left,20))
        self.add_contour('body', 'body-right', 'body-se', 'body-base', 'body-sw', 'body-left')
        self.relate('connect', 'body', 'canopy')
        self.add_dot('home', (axis,54))
