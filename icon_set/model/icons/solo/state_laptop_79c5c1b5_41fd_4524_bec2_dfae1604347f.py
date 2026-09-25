from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "79c5c1b5-41fd-4524-bec2-dfae1604347f"
SOURCE_PATH = "icon_set/work/todo-references/state laptop_79c5c1b5-41fd-4524-bec2-dfae1604347f.svg"
AUTHOR = "gpt-6"
class StateLaptop(Solo48):
    """An open laptop with a blank screen and flared keyboard base."""
    icon_id = "state-laptop"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("symbol", "state", "other", "primitives-generate")
    aliases = ("laptop", "notebook computer")
    keywords = ("computer", "screen")
    def build(self):
        # Symmetric screen and flared base, axis24, corner radius4.
        # Exact centerline extremes (4,8)-(44,40); hinge nodes shared.
        axis,r=24,4
        left,right=axis-16,axis+16
        self.add_line("top",(left+r,8),(right-r,8))
        self.add_arc("tr",(right-r,8),(right,12),radius_x=r)
        self.add_line("right",(right,12),(right,28))
        self.add_line("flare-right",(right,28),(44,36))
        self.add_arc("br",(44,36),(40,40),radius_x=r)
        self.add_line("bottom",(40,40),(8,40))
        self.add_arc("bl",(8,40),(4,36),radius_x=r)
        self.add_line("flare-left",(4,36),(left,28))
        self.add_line("left",(left,28),(left,12))
        self.add_arc("tl",(left,12),(left+r,8),radius_x=r)
        self.add_contour("outline","top","tr","right","flare-right","br","bottom","bl","flare-left","left","tl",closed=True)
        self.add_line("hinge",(left,28),(right,28))
        self.relate("connect","hinge","outline")
