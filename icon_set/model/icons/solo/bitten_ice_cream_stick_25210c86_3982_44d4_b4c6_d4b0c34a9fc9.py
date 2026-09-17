"""Bitten Ice Cream Bar."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '25210c86-3982-44d4-b4c6-d4b0c34a9fc9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/ice cream bite_25210c86-3982-44d4-b4c6-d4b0c34a9fc9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bitten-ice-cream-stick'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('ice cream', 'popsicle', 'bite', 'stick', 'frozen', 'dessert', 'treat')

    def build(self):
        # Plan: Rounded frozen bar with a large concave upper-right bite and centered capsule stick. Shared stick/bar junctions. Lucide rounded corner construction; bite deliberately asymmetric. Bounds (10,4)-(38,44).
        self.add_line('top',(18,4),(26,4))
        self.add_arc('bite',(26,4),(38,16),radius_x=12,sweep=False)
        self.add_line('right',(38,16),(38,26))
        self.add_arc('br',(38,26),(32,32),radius_x=6)
        self.add_line('b1',(32,32),(28,32));self.add_line('b2',(28,32),(20,32));self.add_line('b3',(20,32),(16,32))
        self.add_arc('bl',(16,32),(10,26),radius_x=6)
        self.add_line('left',(10,26),(10,12))
        self.add_arc('tl',(10,12),(18,4),radius_x=8)
        self.add_contour('bar','top','bite','right','br','b1','b2','b3','bl','left','tl',closed=True)
        self.add_line('stick-l',(20,32),(20,40))
        self.add_arc('stick-bottom',(20,40),(28,40),radius_x=4,sweep=False)
        self.add_line('stick-r',(28,40),(28,32))
        self.add_contour('stick','stick-l','stick-bottom','stick-r');self.relate('connect','stick','bar')
