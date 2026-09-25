"""A person sits behind a desk with an open laptop on its left side. A dog occupies the foreground at the lower right, with a left-facing muzzle, drooping ear and rounded back.
Lucide user/laptop construction and dog drooping ear. Desk, laptop, worker and foreground muzzle retained. Fur and facial detail omitted; the back is merged into the drooping outer-ear silhouette. Dog faces left.
SQUARE: centerline extremes (6,6)-(42,42); freshly authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3129a564-9364-48f9-a6ca-252c1dbb68a6'
SOURCE_PATH = 'pictographic-primitives/work/work from home user pet dog_3129a564-9364-48f9-a6ca-252c1dbb68a6.svg'
AUTHOR = 'gpt-6'


class DeskWorkerWithDog(Solo48):
    icon_id = 'desk-worker-with-dog'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "work"
    categories = ("work", "primitives")
    aliases = ()
    keywords = ('person', 'laptop', 'dog', 'pet', 'desk', 'home')

    def build(self) -> None:
        self.add_arc('head-top', (22, 10), (30, 10), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('head-bottom', (30, 10), (22, 10), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_arc('shoulder', (18, 28), (22, 24), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_polyline('desk', (6, 42), (6, 28), (18, 28), closed=False)
        self.relate("connect", 'desk', 'shoulder')
        self.add_polyline('laptop', (8, 16), (12, 28), (18, 28), closed=False)
        self.relate("connect", 'laptop', 'desk')
        self.relate("connect", 'laptop', 'shoulder')
        self.add_polyline('dog-face', (32, 42), (32, 40), (26, 40), (26, 32), (30, 32), closed=False)
        self.add_arc('dog-crown', (30, 32), (40, 32), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('ear', (40, 32), (40, 40))
        self.relate("connect", 'ear', 'dog-crown')
        self.add_arc('dog-back', (40, 40), (42, 42), radius_x=2, radius_y=2, sweep=False, large_arc=False)
        self.relate("connect", 'dog-face', 'dog-crown')
        self.relate("connect", 'dog-back', 'ear')
