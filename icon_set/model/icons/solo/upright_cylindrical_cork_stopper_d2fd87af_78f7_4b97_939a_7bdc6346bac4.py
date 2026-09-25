"""An upright cork stopper with elliptical top and sparse grain. VRECT_M 10,4..38,44 preserves tall cylindrical proportions. Shared rim nodes and mirrored side walls. Source supplies grain; Lucide cylinder supplies elliptical rim construction. Omit top scratch and reduce body grain to two marks."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = 'd2fd87af-78f7-4b97-939a-7bdc6346bac4'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_13/cork_d2fd87af-78f7-4b97-939a-7bdc6346bac4.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'upright-cylindrical-cork-stopper'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ('Cylindrical Wine Bottle Cork',)
    keywords = ('cork', 'stopper', 'bottle', 'wine', 'cylinder', 'seal', 'material')
    def build(self):
        self.add_arc("top-back",(10,10),(38,10),radius_x=14,radius_y=6)
        self.add_line("right-wall",(38,10),(38,38))
        self.add_arc("bottom",(38,38),(10,38),radius_x=14,radius_y=6)
        self.add_line("left-wall",(10,38),(10,10))
        self.add_contour("body","top-back","right-wall","bottom","left-wall",closed=True)
        self.add_arc("top-front",(10,10),(38,10),radius_x=14,radius_y=6,sweep=False)
        self.relate("connect","body","top-front")
        self.add_line("grain-left",(20,25),(20,28))
        self.add_line("grain-right",(28,32),(28,34))
