"""Right-facing gorilla with domed skull, heavy back and broad knuckle-supported forelimb; crest scallops and ear omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '655f543d-189f-5aa3-982a-b4ed7b3481e7'
SOURCE_PATH = 'pictographic-primitives/animals/gorilla_655f543d-189f-5aa3-982a-b4ed7b3481e7.svg'
AUTHOR = 'gpt-6'


class Gorilla(Solo48):
    icon_id = 'gorilla'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('gorilla', 'ape', 'primate', 'knuckle', 'monkey', 'animal', 'wildlife', 'strength')

    def build(self) -> None:
        # Keyshape ink extremes: (0, 3, 48, 45); centerlines inset by stroke radius 2.
        self.add_arc('silhouette-1', (6, 33), (12, 19), radius_x=10, radius_y=14, sweep=True)
        self.add_line('silhouette-2', (12, 19), (19, 19))
        self.add_arc('silhouette-3', (19, 19), (27, 12), radius_x=8, radius_y=8, sweep=False)
        self.add_arc('silhouette-4', (27, 12), (35, 6), radius_x=8, radius_y=7, sweep=True)
        self.add_arc('silhouette-5', (35, 6), (42, 12), radius_x=7, radius_y=7, sweep=True)
        self.add_line('silhouette-6', (42, 12), (42, 18))
        self.add_line('silhouette-7', (42, 18), (42, 24))
        self.add_arc('silhouette-8', (42, 24), (40, 28), radius_x=6, radius_y=6, sweep=True)
        self.add_line('silhouette-9', (40, 28), (42, 38))
        self.add_line('silhouette-10', (42, 38), (42, 42))
        self.add_line('silhouette-11', (42, 42), (33, 42))
        self.add_line('silhouette-12', (33, 42), (31, 34))
        self.add_line('silhouette-13', (31, 34), (24, 34))
        self.add_line('silhouette-14', (24, 34), (15, 35))
        self.add_line('silhouette-15', (15, 35), (14, 42))
        self.add_line('silhouette-16', (14, 42), (6, 42))
        self.add_arc('silhouette-17', (6, 42), (6, 41), radius_x=2, radius_y=2, sweep=True)
        self.add_line('silhouette-18', (6, 41), (6, 33))
        self.add_contour('silhouette', 'silhouette-1', 'silhouette-2', 'silhouette-3', 'silhouette-4', 'silhouette-5', 'silhouette-6', 'silhouette-7', 'silhouette-8', 'silhouette-9', 'silhouette-10', 'silhouette-11', 'silhouette-12', 'silhouette-13', 'silhouette-14', 'silhouette-15', 'silhouette-16', 'silhouette-17', 'silhouette-18', closed=True)
        self.add_line('arm', (27, 23), (31, 34))
        self.relate("connect", 'arm', 'silhouette')
