"""A side-view dustpan with upright rounded handle and wedge pan; perspective seams omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f3734474-3def-4324-9642-c04a47b601f1'
SOURCE_PATH = 'pictographic-primitives/tools/duspan_f3734474-3def-4324-9642-c04a47b601f1.svg'
AUTHOR = 'gpt-6'

class Dustpan(Solo48):
    icon_id = 'dustpan'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ()
    keywords = ('dustpan', 'cleaning', 'sweep', 'dirt', 'housekeeping', 'scoop', 'janitor', 'chores')

    def build(self) -> None:
        self.add_polyline('pan',(6,42),(22,28),(42,28),(42,42),closed=True)
        self.add_line('rear',(28,28),(28,10))
        self.add_arc('cap',(28,10),(36,10),radius_x=4)
        self.add_line('front',(36,10),(36,28))
        self.add_contour('handle','rear','cap','front')
        self.relate('connect','handle','pan')
