"""A domed hard hat sits on a centered display stand. Lucide hard-hat informs dome and brim. Omit double brim and paired ridge walls; retain a single ridge."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2c1fa7b6-a8c3-4407-9935-862250d036d1'
SOURCE_PATH = 'pictographic-primitives/protection/helmet_2c1fa7b6-a8c3-4407-9935-862250d036d1.svg'
AUTHOR = 'gpt-6'


class ProtectionIcon(Solo48):
    icon_id = 'hard-hat-on-stand-2c1fa7b6'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "protection"
    categories = ("protection", "primitives")
    aliases = ()
    keywords = ('hard hat', 'helmet', 'stand', 'safety', 'construction', 'display', 'protection', 'equipment')

    def build(self):
        # HRECT_L centerline extremes: (4,8)-(44,40).

        # Hat owns dome and brim; stand joins the brim and centered foot.
        self.add_arc('dome-left', (8,24), (24,8), radius_x=16)
        self.add_arc('dome-right', (24,8), (40,24), radius_x=16)
        self.add_contour('dome','dome-left','dome-right')
        self.add_polyline('brim',(4,24),(8,24),(24,24),(40,24),(44,24))
        self.relate('connect','dome','brim')
        self.add_line('ridge',(24,8),(24,15))
        self.relate('connect','ridge','dome')
        self.add_line('post',(24,24),(24,40))
        self.add_polyline('foot',(14,40),(24,40),(34,40))
        self.relate('connect','post','brim')
        self.relate('connect','post','foot')
