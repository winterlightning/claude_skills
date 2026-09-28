"""Reconstructed slanted cylindrical marshmallow on a roasting stick."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "51eb3863-a02f-4624-ba65-ff48208cd5b7"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__cylindrical-marshmallow-on-slanted-stick/20260926T165410Z-thuan-mac/reference/marshmallow_51eb3863-a02f-4624-ba65-ff48208cd5b7.svg"
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = "cylindrical-marshmallow-on-slanted-stick"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ("marshmallow", "cylinder", "stick", "roasting")
    def build(self):
        # Cylindrical body leans up-right; an inset curved end seam defines its cap.
        self.add_bezier("cylinder", (18,8), ((20,6),(22,6),(24,6)), ((27,6),(30,7),(32,9)), ((38,11),(42,14),(42,18)), ((42,25),(34,37),(26,38)), ((19,39),(11,34),(9,28)), ((7,24),(10,20),(18,8)))
        self.add_bezier("end-seam", (18,8), ((20,15),(30,22),(40,21)))
        self.add_line("stick", (14,31),(6,42))
        self.relate("connect", "stick", "cylinder")
        self.relate("connect", "end-seam", "cylinder")
