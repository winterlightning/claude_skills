"""A laptop storefront with a three-scallop awning.

Symbol plan: symmetric x24 device, repeated radius6 awning scallops, vertical
screen sides and a wide rounded laptop base. HRECT_L centerline extremes
(4,8)-(44,40). Shared endpoints own each real awning/side/base attachment.
Lucide store original and atomic-debug informed the scalloped canopy; laptop
informed the broad curved base and screen sides. Source supplies the integrated
online storefront. Omit the small base recess and extra awning seam for clarity.
No human or text elements. The source's three scallops remain explicit.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9f4bfb12-0d40-5a5f-a7aa-e2b3371ced5e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/ecommerce/e commerce shop_9f4bfb12-0d40-5a5f-a7aa-e2b3371ced5e.svg'
AUTHOR = 'gpt-6'


class LaptopStorefront(Solo48):
    icon_id = 'laptop-storefront'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'ecommerce'
    aliases = ('online-store-laptop',)
    keywords = ('laptop', 'storefront', 'awning', 'shop', 'online', 'commerce')

    def build(self):
        axis, radius, step = 24, 6, 12
        self.add_polyline('canopy',(6,16),(10,8),(38,8),(42,16))
        members=[]
        for index in range(3):
            x=42-index*step
            name=f'scallop-{index}'
            self.add_arc(name,(x,16),(x-step,16),radius_x=radius)
            members.append(name)
        self.add_contour('awning-edge',*members)
        self.relate('connect','canopy','awning-edge')
        for side in (-1,1):
            x=axis+side*18
            self.add_line(f'screen-{side}',(x,16),(x,30))
            self.relate('connect','canopy',f'screen-{side}')
            self.relate('connect','awning-edge',f'screen-{side}')
        self.add_line('base-top-left',(4,30),(6,30))
        self.add_line('base-top-middle',(6,30),(42,30))
        self.add_line('base-top-right',(42,30),(44,30))
        self.add_arc('base-right',(44,30),(34,40),radius_x=10)
        self.add_line('base-bottom',(34,40),(14,40))
        self.add_arc('base-left',(14,40),(4,30),radius_x=10)
        self.add_contour('base','base-top-left','base-top-middle','base-top-right','base-right','base-bottom','base-left',closed=True)
        for side in (-1,1):self.relate('connect',f'screen-{side}','base')
