"""A squat creature with pointed ears, outstretched arms and rounded feet. SQUARE fits the whole silhouette. Bilateral silhouette and dot eyes share axis24. Source supplies ears and limbs; Lucide ghost supplies continuous silhouette with sparse eyes. Tiny mouth and ear seams omitted.
Source editorial brief is preserved in the gallery; source supplies identity and arrangement.
"""
from ._base import Solo48
from ...keyshapes import Keyshape

SOURCE_ICON_ID = 'd0fcb2bb-064f-48db-94e0-3fa45e7e4746'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_06/beastie_d0fcb2bb-064f-48db-94e0-3fa45e7e4746.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'cute-pointy-eared-monster-character'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ['Cute Pointy Eared Monster Character']
    keywords = ['creature', 'monster', 'ears', 'character', 'body', 'cute', 'figure']

    def build(self):
        self.add_bezier("outline",(12,6),
            ((16,7),(18,11),(18,14)),
            ((21,12),(27,12),(30,14)),
            ((30,11),(32,7),(36,6)),
            ((38,10),(38,15),(36,18)),
            ((39,22),(38,24),(36,26)),
            ((40,27),(42,29),(42,32)),
            ((42,35),(37,34),(34,32)),
            ((34,37),(35,42),(30,42)),
            ((27,42),(28,36),(24,36)),
            ((20,36),(21,42),(18,42)),
            ((13,42),(14,37),(14,32)),
            ((11,34),(6,35),(6,32)),
            ((6,29),(8,27),(12,26)),
            ((10,24),(9,22),(12,18)),
            ((10,15),(10,10),(12,6)))
        self.add_contour("body","outline",closed=True)
        for x in (19,29):
            self.add_dot(f"eye-{x}",(x,22))
