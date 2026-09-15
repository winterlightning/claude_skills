'Volcano flowing lava: independent spacing revision.\n\nEight-unit smoke neck; preserve a clear bent lava stream from the crater.\nNative solo family, HRECT_XL keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: cloud: broad curved smoke silhouette. Local Lucide originals and atomic-debug renders were inspected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '016ae680-3dc4-5b76-9bc4-37abb5d12188'
SOURCE_PATH = 'pictographic-primitives/weather/natural disaster volcano lava_016ae680-3dc4-5b76-9bc4-37abb5d12188.svg'
AUTHOR = 'gpt-6'

class VolcanoFlowingLava(Solo48):
    icon_id = 'volcano-flowing-lava'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/weather'
    aliases = ()
    keywords = ('volcano', 'lava', 'eruption', 'mountain', 'plume', 'disaster')

    def build(self) -> None:
        self.add_polyline("lava", (24,30),(22,35),(26,40))
        self.relate("connect", "lava", "mountain")
        self.add_polyline('mountain', (4, 40), (15, 30), (20, 30), (24, 30), (28, 30), (33, 30), (44, 40), closed=False)
        self.add_line('smoke-neck-left', (20, 30), (20, 22))
        self.add_line('smoke-base-left', (20, 22), (15, 22))
        self.add_arc('smoke-left', (15, 22), (10, 17), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_arc('smoke-top', (10, 17), (38, 17), radius_x=14, radius_y=9, sweep=True, large_arc=False)
        self.add_arc('smoke-right', (38, 17), (33, 22), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('smoke-base-right', (33, 22), (28, 22))
        self.add_line('smoke-neck-right', (28, 22), (28, 30))
        self.add_contour('smoke', 'smoke-neck-left', 'smoke-base-left', 'smoke-left', 'smoke-top', 'smoke-right', 'smoke-base-right', 'smoke-neck-right', closed=False)
        self.relate('connect', 'smoke', 'mountain')
