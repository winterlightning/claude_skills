'Rattlesnake: smooth nested turns, an 8-unit body width and regularly separated rattle marks.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd4648896-3720-5e11-b38e-0b0c450735c6'
SOURCE_PATH = 'pictographic-primitives/animals/reptile rattlesnake_d4648896-3720-5e11-b38e-0b0c450735c6.svg'
AUTHOR = 'gpt-6'


class Rattlesnake(Solo48):
    icon_id = 'rattlesnake'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals/reptiles'
    aliases = ()
    keywords = ('rattlesnake', 'snake', 'rattle', 'reptile', 'slither', 'venom', 'desert', 'serpent')

    def build(self):
        # Rattlesnake: tangent nested turns, a broad head and well-separated round rattle marks.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        self.add_dot('rattle-top',(6,6))
        self.add_dot('rattle-bottom',(6,15))
        l('tail',(6,26),(6,32))
        a('tail-turn',(6,32),(22,32),8,sweep=False)
        l('inner-neck',(22,32),(22,20))
        a('inner-top',(22,20),(32,20),5)
        l('inner-right',(32,20),(32,37))
        a('head-tip',(32,37),(42,37),5,sweep=False)
        l('outer-right',(42,37),(42,20))
        a('outer-top',(42,20),(14,20),14,sweep=False)
        l('outer-neck',(14,20),(14,32))
        self.add_contour('snake','tail','tail-turn','inner-neck','inner-top','inner-right','head-tip','outer-right','outer-top','outer-neck')
