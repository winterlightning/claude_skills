"""Right-facing barrel-bodied rhino. Two visible legs and one strong horn replace overlapping distant limbs and the tiny second horn. Centerline (6,8)-(42,40)."""
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
    category = "animals"
    aliases = ()
    keywords = ('rhino', 'rhinoceros', 'horn', 'standing', 'animal', 'safari', 'africa', 'wildlife')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_line('silhouette-1',(4, 40),(4, 22))
        self.add_bezier('silhouette-2',(4, 22),*(((4, 16.66495389), (7.69870466, 11.77263283), (14, 10)),))
        self.add_line('silhouette-3',(14, 10),(29, 10))
        self.add_line('silhouette-4',(29, 10),(33, 8))
        self.add_line('silhouette-5',(33, 8),(35, 16))
        self.add_line('silhouette-6',(35, 16),(40, 20))
        self.add_line('silhouette-7',(40, 20),(44, 12))
        self.add_line('silhouette-8',(44, 12),(44, 26))
        self.add_bezier('silhouette-9',(44, 26),*(((44, 28.21753356), (43.69026141, 30.5422399), (42, 32)),))
        self.add_line('silhouette-10',(42, 32),(32, 28))
        self.add_line('silhouette-11',(32, 28),(30, 40))
        self.add_line('silhouette-12',(30, 40),(22, 40))
        self.add_line('silhouette-13',(22, 40),(22, 32))
        self.add_line('silhouette-14',(22, 32),(14, 32))
        self.add_line('silhouette-15',(14, 32),(12, 40))
        self.add_line('silhouette-16',(12, 40),(4, 40))
        self.add_contour('silhouette',*('silhouette-1', 'silhouette-2', 'silhouette-3', 'silhouette-4', 'silhouette-5', 'silhouette-6', 'silhouette-7', 'silhouette-8', 'silhouette-9', 'silhouette-10', 'silhouette-11', 'silhouette-12', 'silhouette-13', 'silhouette-14', 'silhouette-15', 'silhouette-16'),closed=True)
