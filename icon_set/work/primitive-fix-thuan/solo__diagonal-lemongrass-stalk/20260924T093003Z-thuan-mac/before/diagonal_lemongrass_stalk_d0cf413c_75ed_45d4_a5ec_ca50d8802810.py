"""Fresh Lemongrass Stalk."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd0cf413c-75ed-45d4-a5ec-ca50d8802810'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/lemongrass_d0cf413c-75ed-45d4-a5ec-ca50d8802810.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'diagonal-lemongrass-stalk'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('lemongrass', 'herb', 'stalk', 'bulb', 'leaf', 'seasoning', 'plant')

    def build(self):
        # Plan: Diagonal lemongrass with rounded basal bulb and long pointed leaf tips. Lucide leaf coherent taper; fine roots and narrow seam omitted. Envelope (6,6)-(42,42). Second narrow leaf reduced to a stroke.
        self.add_bezier('bulb',(6,34),((6,28),(15,23),(20,18)))
        self.add_polyline('leaves',(20,18),(30,12),(42,6),(34,26),(18,40))
        self.add_bezier('base',(18,40),((16,42),(14,42),(12,42)),((8,42),(6,39),(6,34)))
        for a,b in (('bulb','leaves'),('leaves','base'),('base','bulb')):self.relate('connect',a,b)

        self.add_line('leaf-tip',(30,12),(28,6));self.relate('connect','leaf-tip','leaves')
