"""Front-facing baboon with small ears and a long central nose/muzzle.

SQUARE (6,6)-(42,42) accommodates the ears and elongated lower face.
Axis24 owns paired contours/eyes. Lucide dog contributes contour economy and
small eye marks; the source supplies the long central muzzle and rounded chin.
Omit the nested muzzle outline, preserving its long nose and curved mouth.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '43a539c3-82f4-4fbd-b778-c77d1e22af44'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_05/baboon_43a539c3-82f4-4fbd-b778-c77d1e22af44.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'long-muzzled-baboon-face'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ('Baboon Animal Face',)
    keywords = ('baboon','face','muzzle','primate','ears','animal','monkey')

    def build(self):
        self.add_bezier('outline',(24,6),
            ((30,6),(32,8),(36,10)),
            ((40,10),(42,12),(42,18)),
            ((42,22),(40,24),(38,26)),
            ((38,36),(32,42),(24,42)),
            ((16,42),(10,36),(10,26)),
            ((8,24),(6,22),(6,18)),
            ((6,12),(8,10),(12,10)),
            ((16,8),(18,6),(24,6)))
        self.add_contour('head','outline',closed=True)
        for x in (15,33):
            self.add_dot(f'eye-{x}',(x,18))
        self.add_line('nose',(24,22),(24,33))
        self.add_bezier('mouth-left',(20,30),((20,32),(22,33),(24,33)))
        self.add_bezier('mouth-right',(24,33),((26,33),(28,32),(28,30)))
        self.add_contour('mouth','mouth-left','mouth-right')
        self.relate('connect','nose','mouth')
