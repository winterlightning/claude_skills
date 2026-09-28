"""Fresh Broccoli Vegetable."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '57d07ae0-a586-52f2-b0d1-5f36b6fe1c7b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/broccoli_57d07ae0-a586-52f2-b0d1-5f36b6fe1c7b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'broccoli-crown-and-stalk'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('broccoli', 'vegetable', 'floret', 'stalk', 'greens', 'produce', 'food')

    def build(self):
        # Plan: Broccoli with three broad crown lobes and tapered thick stalk. Lucide broccoli coherent organic curves. Tiny center vein omitted. Mirrored envelope (6,6)-(42,42).
        self.add_bezier('crown',(16,26),((12,31),(6,27),(6,20)),((6,13),(11,10),(16,13)),((15,8),(19,6),(24,6)),((29,6),(33,8),(32,13)),((37,10),(42,13),(42,20)),((42,27),(36,31),(32,26)),((29,29),(19,29),(16,26)))
        self.add_contour('florets','crown',closed=True)
        self.add_bezier('stalk',(16,26),((19,31),(18,37),(18,42)))
        self.add_line('base',(18,42),(30,42))
        self.add_bezier('stalk-r',(30,42),((30,37),(29,31),(32,26)))
        for a,b in (('stalk','florets'),('stalk','base'),('base','stalk-r'),('stalk-r','florets')):self.relate('connect',a,b)
