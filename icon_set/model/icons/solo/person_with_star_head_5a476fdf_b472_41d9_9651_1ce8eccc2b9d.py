"""A five-pointed star replaces the head of a front-facing bust. The star sits directly above a broad arch of shoulders, forming a single vertically balanced figure without facial details.
Lucide star silhouette and user shoulder construction. The star replaces the head, forming one conceptual portrait. Symmetric geometry; no facial detail.
SQUARE: centerline extremes (6,6)-(42,42); independently authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5a476fdf-b472-41d9-9651-1ce8eccc2b9d'
SOURCE_PATH = 'pictographic-primitives/work/human resources employee star_5a476fdf-b472-41d9-9651-1ce8eccc2b9d.svg'
AUTHOR = 'gpt-6'


class PersonWithStarHead(Solo48):
    icon_id = 'person-with-star-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "work"
    categories = ("work", "primitives")
    aliases = ()
    keywords = ('person', 'star', 'employee', 'talent', 'recognition', 'bust')

    def build(self) -> None:
        self.add_polyline('star', (24, 6), (28, 14), (37, 15), (30, 21), (32, 29), (24, 25), (16, 29), (18, 21), (11, 15), (20, 14), closed=True)
        self.add_arc('shoulder-left', (6, 42), (14, 38), radius_x=8, radius_y=4, sweep=True, large_arc=False)
        self.add_line('shoulder-top', (14, 38), (34, 38))
        self.add_arc('shoulder-right', (34, 38), (42, 42), radius_x=8, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('shoulders', 'shoulder-left', 'shoulder-top', 'shoulder-right', closed=False)
