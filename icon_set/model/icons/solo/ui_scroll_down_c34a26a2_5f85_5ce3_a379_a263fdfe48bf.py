'Scroll down: connected equal arrowhead arms and a clear five-unit ink gap above the bottom rule.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c34a26a2-5f85-5ce3-a379-a263fdfe48bf'
SOURCE_PATH = 'icons-json/websites/ui scroll down_c34a26a2-5f85-5ce3-a379-a263fdfe48bf.json'
AUTHOR = 'gpt-6'

class UiScrollDown(Solo48):
    icon_id = 'ui-scroll-down'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'websites'
    aliases = ()
    keywords = ('ui', 'scroll', 'down', 'websites')

    def build(self) -> None:
        self.add_line('shaft',(24,4),(24,35))
        self.add_polyline('head',(13,24),(24,35),(35,24))
        self.relate('connect','shaft','head')
        self.add_line('bottom',(8,44),(40,44))
