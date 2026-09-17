"""Fresh Whole Garlic Bulb."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '828112ef-2027-4582-9d01-a81708c75614'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/garlic_828112ef-2027-4582-9d01-a81708c75614.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-lobed-garlic-bulb'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('garlic', 'bulb', 'clove', 'vegetable', 'ingredient', 'produce', 'food')

    def build(self):
        # Plan: Garlic bulb with tall flat-cut neck and two ribs defining three cloves. Lucide apple coherent bulging curves. Shared mirrored rib endpoints, no fine texture. Envelope (8,4)-(40,44).
        self.add_polyline('neck',(20,12),(20,4),(28,4),(28,12))
        self.add_bezier('right',(28,12),((34,16),(40,22),(40,32)),((40,40),(34,44),(28,44)))
        self.add_line('base',(28,44),(20,44))
        self.add_bezier('left',(20,44),((14,44),(8,40),(8,32)),((8,22),(14,16),(20,12)))
        for a,b in (('neck','right'),('right','base'),('base','left'),('left','neck')):self.relate('connect',a,b)
        for side in (-1,1):
         x=24+side*4
         self.add_bezier(f'rib-{side}',(x,12),((24+side*8,24),(24+side*10,36),(x,44)))
         self.relate('connect',f'rib-{side}','neck');self.relate('connect',f'rib-{side}','base');self.relate('connect',f'rib-{side}','left' if side==-1 else 'right')
