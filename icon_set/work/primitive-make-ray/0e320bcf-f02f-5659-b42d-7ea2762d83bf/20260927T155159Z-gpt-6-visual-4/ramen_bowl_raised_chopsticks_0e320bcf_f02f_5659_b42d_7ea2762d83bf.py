"""Fresh revision of ramen-bowl-raised-chopsticks.

Original and rejected SVG compared before drawing. The bowl had a letter-like right angle; replaced it with chopsticks and a descending noodle above the bowl.
"""
"""Ramen Bowl with Chopsticks."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0e320bcf-f02f-5659-b42d-7ea2762d83bf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-fix-thuan/solo__ramen-bowl-raised-chopsticks/20260927T153833Z-thuan-mac-1/reference/asian food noodles_0e320bcf-f02f-5659-b42d-7ea2762d83bf.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'ramen-bowl-raised-chopsticks'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('ramen', 'bowl', 'raised', 'chopsticks')

    def build(self):
        # Original: an open bowl, one hanging noodle, and two raised chopsticks.
        self.add_bezier('bowl-right',(6,26),((6,36),(14,42),(24,42)),((34,42),(42,36),(42,26)))
        self.add_line('rim',(6,26),(42,26))
        self.relate('connect','bowl-right','rim')
        self.add_polyline('upper-stick',(10,10),(18,9),(42,6))
        self.add_line('noodle',(18,9),(18,26))
        self.add_line('lower-stick',(28,16),(42,16))
        self.relate('connect','noodle','upper-stick')
        self.relate('connect','noodle','rim')
