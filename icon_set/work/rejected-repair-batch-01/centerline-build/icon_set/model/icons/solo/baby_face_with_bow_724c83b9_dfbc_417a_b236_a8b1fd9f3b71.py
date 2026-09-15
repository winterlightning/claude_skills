'Baby face with bow: preserve the rounded cheeks, sleepy smile and paired bow loops; use shared centre and temple junctions with clear internal spacing.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '724c83b9-dfbc-417a-b236-a8b1fd9f3b71'
SOURCE_PATH = 'pictographic-primitives/babies/baby girl_724c83b9-dfbc-417a-b236-a8b1fd9f3b71.svg'
AUTHOR = 'gpt-6'


class BabyFaceWithBow(Solo48):
    icon_id = 'baby-face-with-bow'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/babies"
    aliases = ()
    keywords = ('baby', 'face', 'with', 'bow', 'infant', 'nursery')

    def build(self) -> None:
        # Rounded baby cheeks and ears; paired bow loops share the centre rather than crossing loosely.
        self.add_bezier('temple-left',(10,20),((9,21),(8,23),(8,24)))
        self.add_bezier('ear-left',(8,24),((6,24),(6,25),(6,27)),((6,29),(6,30),(8,30)))
        self.add_bezier('chin',(8,30),((10,38),(16,42),(24,42)),((32,42),(38,38),(40,30)))
        self.add_bezier('ear-right',(40,30),((42,30),(42,29),(42,27)),((42,25),(42,24),(40,24)))
        self.add_bezier('temple-right',(40,24),((40,23),(39,21),(38,20)))
        self.add_contour('face','temple-left','ear-left','chin','ear-right','temple-right')
        self.add_polyline('bow-left',(24,13),(10,6),(10,20),closed=True)
        self.add_polyline('bow-right',(24,13),(38,6),(38,20),closed=True)
        self.relate('connect','bow-left','bow-right');self.relate('connect','bow-left','face');self.relate('connect','bow-right','face')
        self.add_dot('eye-left',(17,26))
        self.add_dot('eye-right',(31,26))
        self.add_arc('smile',(21,33),(27,33),radius_x=4,radius_y=2,sweep=False)
