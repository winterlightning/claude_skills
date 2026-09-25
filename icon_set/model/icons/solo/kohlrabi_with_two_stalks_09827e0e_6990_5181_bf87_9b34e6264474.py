"""Fresh Kohlrabi Root Vegetable."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '09827e0e-6990-5181-bf87-9b34e6264474'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/kohlrabi_09827e0e-6990-5181-bf87-9b34e6264474.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'kohlrabi-with-two-stalks'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('kohlrabi', 'root', 'vegetable', 'bulb', 'leaf', 'produce', 'food')

    def build(self):
        # Plan: Kohlrabi bulb with pointed root and two rising curved stalks. Lucide sprout paired stems; narrow leaf outlines simplified to strokes. Mirrored envelope (8,4)-(40,44).
        self.add_bezier('body',(8,30),((8,23),(12,20),(18,20)),((22,20),(26,20),(30,20)),((36,20),(40,23),(40,30)),((40,37),(32,38),(28,40)))
        self.add_polyline('root',(28,40),(24,44),(20,40))
        self.add_bezier('left',(20,40),((16,38),(8,37),(8,30)))
        for a,b in (('body','root'),('root','left'),('left','body')):self.relate('connect',a,b)
        for side in (-1,1):
         self.add_bezier(f'stalk-{side}',(24+side*6,20),((24+side*6,12),(24+side*9,6),(24+side*12,4)))
         self.relate('connect',f'stalk-{side}','body')
