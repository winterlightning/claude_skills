"""house ventilator: fresh SOLO48 repair.
Plan: Four identical rotated curved blades sharing a central node.
Keyshape: SQUARE. Square house holds a centered four-blade rotor.
Omissions: Separate hub ring removed; its center is represented by the blade junction.
Construction reference: house and fan: enclosing roof and quarter-turn blade repetition.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'adc26099-d55f-405e-935e-9a654dc938e4'
SOURCE_PATH = 'pictographic-primitives/other/house ventilator_adc26099-d55f-405e-935e-9a654dc938e4.svg'
AUTHOR = 'gpt-6'
PARENT_SOURCE = 'icon_set/model/icons/solo/house_ventilator_adc26099_d55f_405e_935e_9a654dc938e4.py'

class Drawing(Solo48):
    icon_id = 'house-ventilator'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ()
    keywords = ('house', 'ventilator')

    def house(self):
        self.add_line('roof-1', (6, 14), (24, 6))
        self.add_line('roof-2', (24, 6), (42, 14))
        self.add_line('wall-right', (42, 14), (42, 40))
        self.add_arc('corner-right', (42, 40), (40, 42), radius_x=2)
        self.add_line('floor', (40, 42), (8, 42))
        self.add_arc('corner-left', (8, 42), (6, 40), radius_x=2)
        self.add_line('wall-left', (6, 40), (6, 14))
        self.add_contour('house', 'roof-1', 'roof-2', 'wall-right', 'corner-right', 'floor', 'corner-left', 'wall-left', closed=True)

    def build(self):
        self.house()
        cx, cy = (24, 25)
        for i in range(4):

            def rot(x, y):
                for _ in range(i):
                    x, y = (-y, x)
                return (cx + x, cy + y)
            self.add_bezier('blade-' + str(i), rot(0, 0), (rot(0, -6), rot(9, -8), rot(8, 0)))
        self.relate('connect', *[f'blade-{i}' for i in range(4)])
