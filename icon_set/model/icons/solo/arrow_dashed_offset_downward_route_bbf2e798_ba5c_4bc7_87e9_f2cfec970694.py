"""A dashed route descends left, crosses right, then points down. Square extremes 6..42 support two elbows. Source supplies step and broken line; Lucide arrow-down supplies joined open tip. Keep three separated route runs, omit tiny dash repeats; shared 8-unit gap budget."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = 'bbf2e798-ba5c-4bc7-87e9-f2cfec970694'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_14/diagram fall fast dash_bbf2e798-ba5c-4bc7-87e9-f2cfec970694.svg'
AUTHOR = 'gpt-6-astra'
class Drawing(Solo48):
    icon_id = 'arrow-dashed-offset-downward-route'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ['Arrow Dashed Offset Downward Route']
    keywords = ['arrow', 'dashed', 'down', 'offset', 'route', 'path', 'bend']
    def build(self):
        self.add_line('start',(6,6),(6,10))
        self.add_bezier('elbow-left',(6,18),((6,22),(8,24),(12,24)))
        self.add_line('middle',(20,24),(24,24))
        self.add_bezier('elbow-right',(32,24),((35,24),(36,27),(36,30)))
        self.add_polyline('head',(30,36),(36,42),(42,36))
        self.add_line('tail',(36,38),(36,42))
        self.relate('connect','tail','head')
