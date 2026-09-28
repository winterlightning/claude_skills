'Toy duck: preserve the raised tail and round head; lower the eye and lift the curved wing for clearance.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f8800cf8-9b17-539e-8a6c-4faf51c6c5c2'
SOURCE_PATH = 'pictographic-primitives/animals/duck_f8800cf8-9b17-539e-8a6c-4faf51c6c5c2.svg'
AUTHOR = 'gpt-6'


class ToyDuck(Solo48):
    icon_id = 'toy-duck'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    categories = ("animals", "primitives")
    aliases = ()
    keywords = ('duck', 'rubber duck', 'toy', 'bath', 'bird', 'debug', 'yellow', 'play')

    def build(self) -> None:
        self.add_polyline('beak',(13,23),(6,20),(6,17),(12,14))
        self.add_bezier('head',(12,14),((13,9),(17,6),(22,6)),((28,6),(31,11),(31,15)))
        self.add_line('neck',(31,15),(28,26))
        self.add_bezier('tail',(28,26),((34,27),(39,25),(42,22)))
        self.add_bezier('back',(42,22),((42,32),(38,42),(32,42)))
        self.add_line('base',(32,42),(16,42))
        self.add_bezier('belly',(16,42),((7,42),(6,33),(13,23)))
        self.relate('connect','beak','head');self.relate('connect','head','neck');self.relate('connect','neck','tail');self.relate('connect','tail','back');self.relate('connect','back','base');self.relate('connect','base','belly');self.relate('connect','belly','beak')
        self.add_dot('eye',(22,16))
        self.add_bezier('wing',(18,32),((20,34),(22,34),(24,33)))
