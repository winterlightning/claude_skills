"""Four-patch quilt with two diagonal folds and shared seam intersections.
SQUARE fits the textile outline. Outer corners share radius 4; seams split
at real midpoint nodes. Opposite folds derive by half-turn about (24,24).
The folds are shortened to fit each patch. No useful Lucide quilt match.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = "343c4f47-d44e-4c96-b347-e1f2bda8a1e2"
SOURCE_PATH = "pictographic-primitives/_uncategorized_32/quilt_343c4f47-d44e-4c96-b347-e1f2bda8a1e2.svg"
AUTHOR = "gpt-6-astra"
class Drawing(Solo48):
    icon_id = "four-patch-quilt"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ("Decorative Quilt Pattern Square",)
    keywords = ("quilt", "patchwork", "blanket", "fabric", "seam", "textile")
    def build(self):
        # Four boundary quadrants expose the seam contact points.
        for j in range(4):
            def rot(p):
                x,y=p
                for _ in range(j): x,y=48-y,x
                return x,y
            self.add_line(f'edge-{j}-a',rot((24,6)),rot((38,6)))
            self.add_arc(f'edge-{j}-b',rot((38,6)),rot((42,10)),radius_x=4)
            self.add_line(f'edge-{j}-c',rot((42,10)),rot((42,24)))
        members=[f'edge-{j}-{k}' for j in range(4) for k in 'abc']
        self.add_contour('boundary',*members,closed=True)
        for j,point in enumerate(((24,6),(42,24),(24,42),(6,24))):
            self.add_line(f'seam-{j}',point,(24,24))
            self.relate('connect',f'seam-{j}',f'edge-{j}-a',f'edge-{(j-1)%4}-c')
        self.relate('connect',*[f'seam-{j}' for j in range(4)])
        for j in range(2):
            transform=lambda p:(48-p[0],48-p[1]) if j else p
            self.add_line(f'fold-{j}',transform((15,15)),transform((16,16)))
