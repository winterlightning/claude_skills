"""Dreidel with square body, pointed base and handle. VRECT_M x10..38 y4..44, mirrored about x24. Source supplies central unlabelled upright mark (not an identified letter); no useful Lucide dreidel match. Single-stroke handle removes tiny enclosed handle opening."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = 'cfd87fe1-8357-410b-b9c6-f70bd7c344c2'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_15/dreidel_cfd87fe1-8357-410b-b9c6-f70bd7c344c2.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'plain-dreidel-with-central-stroke'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ['Plain Dreidel with Central Stroke']
    keywords = ['dreidel', 'top', 'spinning', 'toy', 'handle', 'hanukkah', 'game']
    def build(self):
        self.add_polyline('body',(10,12),(24,12),(38,12),(38,32),(24,44),(10,32),(10,12),closed=True)
        self.add_line('handle',(24,4),(24,12))
        self.add_line('seam',(10,32),(38,32))
        self.relate('connect','body','handle')
        self.relate('connect','body','seam')
        self.add_line('front-mark',(24,20),(24,24))
