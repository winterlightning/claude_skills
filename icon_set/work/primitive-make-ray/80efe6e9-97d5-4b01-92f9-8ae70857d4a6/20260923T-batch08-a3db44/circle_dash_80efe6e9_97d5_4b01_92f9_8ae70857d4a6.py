"""circle dash. Standalone reconstruction of supplied reference.
Plan: preserve the whole composition; CIRCLE bounds (2, 2, 46, 46).
Construction reference: Lucide circle-dashed, round joins and coherent symbol contours.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '80efe6e9-97d5-4b01-92f9-8ae70857d4a6'
SOURCE_PATH = 'icon_set/work/todo-references/circle dash_80efe6e9-97d5-4b01-92f9-8ae70857d4a6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circle-dash'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('circle', 'dash')

    def build(self):

        # Eight repeated dashes, using cardinal bars and diagonal circular arcs.
        # The outermost radial ink is 22 about (24,24).
        for i in range(4):
            def rotate(p):
                x,y=p
                for _ in range(i): x,y=48-y,x
                return x,y
            self.add_arc(f'cardinal-{i}',rotate((22,5)),rotate((26,5)),radius_x=20)
            self.add_arc(f'diagonal-{i}',rotate((36,8)),rotate((40,12)),radius_x=20)

