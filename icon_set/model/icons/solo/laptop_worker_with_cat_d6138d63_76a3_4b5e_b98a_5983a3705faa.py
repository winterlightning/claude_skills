"""A seated person holds an open laptop across bent legs, facing left. A cat sits upright beside the worker on the right, with pointed ears, a projecting muzzle and a curved back.
Lucide user and laptop construction; pointed ears and curved haunch informed by cat. Bent legs and left-facing laptop retain the seated worker. Facial details, doubled limbs and chair omitted. Cat silhouette is deliberately asymmetric.
SQUARE: centerline extremes (6,6)-(42,42); freshly authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd6138d63-76a3-4b5e-b98a-5983a3705faa'
SOURCE_PATH = 'pictographic-primitives/work/work from home user pet cat_d6138d63-76a3-4b5e-b98a-5983a3705faa.svg'
AUTHOR = 'gpt-6'


class LaptopWorkerWithCat(Solo48):
    icon_id = 'laptop-worker-with-cat'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "work"
    categories = ("work", "primitives")
    aliases = ()
    keywords = ('person', 'laptop', 'cat', 'pet', 'home', 'work')

    def build(self) -> None:
        self.add_arc('head-top', (16, 10), (24, 10), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('head-bottom', (24, 10), (16, 10), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_polyline('worker', (20, 23), (20, 30), (14, 30), (10, 42), closed=False)
        self.add_polyline('laptop', (6, 18), (10, 30), (20, 30), closed=False)
        self.relate("connect", 'laptop', 'worker')
        self.add_polyline('cat-front', (30, 42), (32, 42), (32, 32), (29, 30), (32, 28), (32, 20), (37, 24), (42, 20), (42, 38), closed=False)
        self.add_arc('cat-haunch', (42, 38), (38, 42), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('cat-base', (38, 42), (32, 42))
        self.relate("connect", 'cat-front', 'cat-haunch')
        self.relate("connect", 'cat-haunch', 'cat-base')
        self.relate("connect", 'cat-base', 'cat-front')
