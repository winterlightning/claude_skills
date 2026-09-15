'Retouch triangle: lower the triangle apex to separate it from three balanced sparkle rays.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6b3bf2aa-46fa-429d-abfa-cd12abb51ff2'
SOURCE_PATH = 'pictographic-primitives/photography/retouch triangle_6b3bf2aa-46fa-429d-abfa-cd12abb51ff2.svg'
AUTHOR = 'gpt-6'

class RetouchTriangle(Solo48):
    icon_id = 'retouch-triangle'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    aliases = ()
    keywords = ('retouch', 'triangle', 'photography')

    def build(self) -> None:
        self.add_polyline('triangle',(24,21),(40,44),(8,44),closed=True)
        self.add_line('spark',(24,4),(24,12))
        self.add_line('spark-left',(12,9),(15,12))
        self.add_line('spark-right',(33,12),(36,9))
