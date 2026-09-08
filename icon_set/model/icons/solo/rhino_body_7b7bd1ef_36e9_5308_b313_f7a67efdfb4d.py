"""Right-facing barrel-bodied rhino. Two visible legs and one strong horn replace overlapping distant limbs and the tiny second horn. Centerline (2,8)-(46,40)."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7b7bd1ef-36e9-5308-b313-f7a67efdfb4d'
SOURCE_PATH = 'pictographic-primitives/animals/rhino body_7b7bd1ef-36e9-5308-b313-f7a67efdfb4d.svg'
AUTHOR = 'gpt-6'


class StandingRhino(Solo48):
    icon_id = 'standing-rhino'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('rhino', 'rhinoceros', 'horn', 'standing', 'animal', 'safari', 'africa', 'wildlife')

    def build(self) -> None:
        self.add_line('silhouette-1', (2, 40), (2, 22))
        self.add_arc('silhouette-2', (2, 22), (14, 10), radius_x=12, radius_y=12, sweep=True)
        self.add_line('silhouette-3', (14, 10), (29, 10))
        self.add_line('silhouette-4', (29, 10), (33, 8))
        self.add_line('silhouette-5', (33, 8), (35, 16))
        self.add_line('silhouette-6', (35, 16), (39, 20))
        self.add_line('silhouette-7', (39, 20), (44, 12))
        self.add_line('silhouette-8', (44, 12), (46, 26))
        self.add_arc('silhouette-9', (46, 26), (40, 32), radius_x=6, radius_y=6, sweep=True)
        self.add_line('silhouette-10', (40, 32), (32, 28))
        self.add_line('silhouette-11', (32, 28), (30, 40))
        self.add_line('silhouette-12', (30, 40), (24, 40))
        self.add_line('silhouette-13', (24, 40), (24, 32))
        self.add_line('silhouette-14', (24, 32), (10, 32))
        self.add_line('silhouette-15', (10, 32), (8, 40))
        self.add_line('silhouette-16', (8, 40), (2, 40))
        self.add_contour('silhouette', 'silhouette-1', 'silhouette-2', 'silhouette-3', 'silhouette-4', 'silhouette-5', 'silhouette-6', 'silhouette-7', 'silhouette-8', 'silhouette-9', 'silhouette-10', 'silhouette-11', 'silhouette-12', 'silhouette-13', 'silhouette-14', 'silhouette-15', 'silhouette-16', closed=True)
