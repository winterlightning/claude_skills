"""Narwhal swimming upward-right, with an integral tail and long tusk. SQUARE envelope supplied by tusk and tail. Source supplies silhouette and upward pose. No Lucide whale match. Omit the narrow tail notch and flipper crease to preserve openings; retain a single eye; body owns contiguous curves."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '92c799ca-6aa2-4c2b-b0a0-aee64eb0d86c'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_28/narwhal_92c799ca-6aa2-4c2b-b0a0-aee64eb0d86c.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'upturned-narwhal'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = []
    keywords = ['narwhal', 'whale', 'tusk', 'marine', 'animal', 'swimming']
    def build(self):
        self.add_bezier('back',(34,14),((18,6),(18,24),(12,30)))
        points=[(12,30),(6,26),(6,42),(16,42),(18,36)]
        for j,(a,b) in enumerate(zip(points,points[1:])): self.add_line(f'tail-{j}',a,b)
        self.add_bezier('belly',(18,36),((28,40),(42,34),(42,24)),((42,18),(38,14),(34,14)))
        self.add_contour('animal','back',*[f'tail-{j}' for j in range(4)],'belly',closed=True)
        self.add_dot('eye',(32,24))
        self.add_line('tusk',(34,14),(42,6))
        self.relate('connect','animal','tusk')
