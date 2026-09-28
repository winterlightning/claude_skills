"""Slender left-facing pike with a long body, small paired fins, and a forked tail. The source silhouette controls the fish; no exact local Lucide pike match was used."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '602f9a81-4306-4859-94c6-dc6f92e2061c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__slender-swimming-pike/20260927T172707Z-thuan-mac-1/reference/pike_602f9a81-4306-4859-94c6-dc6f92e2061c.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'slender-swimming-pike'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ["pike", "long swimming pike fish"]
    keywords = ["fish", "swimming", "fins", "tail", "aquatic"]
    def build(self):
        # A long pike body carries one dorsal fin, one ventral fin and a forked tail.
        self.add_bezier('back',(4,24),((10,18),(19,18),(27,18)))
        points=((27,18),(30,14),(34,18),(36,20),(44,10),
                (40,24),(44,38),(36,28),(34,30),(30,34),(27,30))
        for j,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'fins-{j}',a,b)
        self.add_bezier('belly',(27,30),((18,32),(10,30),(4,24)))
        self.add_contour('fish','back',*(f'fins-{j}' for j in range(1,11)),'belly',closed=True)
