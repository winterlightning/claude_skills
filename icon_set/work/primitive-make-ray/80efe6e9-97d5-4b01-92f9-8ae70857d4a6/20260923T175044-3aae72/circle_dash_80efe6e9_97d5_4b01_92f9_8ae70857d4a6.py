"""A dashed circular outline.
Construction: Reduced dash count to eight for required separation; straight short tangent strokes follow the circular arrangement.
Lucide construction reference: circle-dashed; coherent arcs and independent enclosed content.
Keyshape CIRCLE: radial ink radius 22, centre (24,24).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '80efe6e9-97d5-4b01-92f9-8ae70857d4a6'
SOURCE_PATH = 'icon_set/work/todo-references/circle dash_80efe6e9-97d5-4b01-92f9-8ae70857d4a6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circle-dash'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('circle', 'dash')

    def build(self):
        # Eight short tangent dashes use shared cardinal and diagonal definitions, rotated by quarter-turns.
        # Dash count reduced to maintain the required clearance between independent arcs.
        for i in range(4):
            def turn(x,y):
                for _ in range(i): x,y=-y,x
                return (24+x,24+y)
            self.add_line(f'cardinal-{i}',turn(-3,-19),turn(3,-19))
            self.add_line(f'diagonal-{i}',turn(12,-16),turn(16,-12))

