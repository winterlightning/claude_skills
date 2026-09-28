"""A broad rounded puppy head with long drooping ears and an empty face. HRECT_L keeps the source broad proportions. Crown radius20 and mirrored ears share x24 axis; jaw endpoints also own the ear junctions. Lucide dog supplies flowing cheek and ear contours; source supplies drooping orientation. No facial features added.
Source editorial brief is preserved in the gallery; source supplies identity and arrangement.
"""
from ._base import Solo48
from ...keyshapes import Keyshape

SOURCE_ICON_ID = '259dcaae-ccb8-4299-b303-c63950fdc6e2'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_06/bichon frise_259dcaae-ccb8-4299-b303-c63950fdc6e2.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'bichon-frise-puppy-head'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ['Bichon Frise Puppy Head']
    keywords = ['puppy', 'dog', 'head', 'ears', 'bichon frise', 'pet', 'face']

    def build(self):
        self.add_arc("crown-left",(4,28),(24,8),radius_x=20)
        self.add_arc("crown-right",(24,8),(44,28),radius_x=20)
        self.add_bezier("ear-right",(44,28),((44,40),(34,40),(34,32)))
        self.add_bezier("jaw",(34,32),((32,37),(28,40),(24,40)),((20,40),(16,37),(14,32)))
        self.add_bezier("ear-left",(14,32),((14,40),(4,40),(4,28)))
        self.add_contour("silhouette","crown-left","crown-right","ear-right","jaw","ear-left",closed=True)
        for x in (14,34):
            self.add_line(f"inner-ear-{x}",(x,22),(x,32))
            self.relate("connect",f"inner-ear-{x}","silhouette")
