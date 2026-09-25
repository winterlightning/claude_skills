'Dashed download: retain two visible shaft dashes and a complete balanced arrowhead above the bottom rule; remove tiny fragmented head dashes.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '529b28f3-98de-499d-84f3-c2ecf8e8d169'
SOURCE_PATH = 'pictographic-primitives/arrows/download dash arrow_529b28f3-98de-499d-84f3-c2ecf8e8d169.svg'
AUTHOR = 'gpt-6'

class DownloadDashArrow(Solo48):
    icon_id = 'download-dash-arrow'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('download', 'dash', 'arrow', 'arrows')

    def build(self) -> None:
        self.add_line('dash-a',(24,4),(24,9))
        self.add_line('dash-b',(24,17),(24,20))
        self.add_line('shaft',(24,28),(24,35))
        self.add_polyline('head',(13,24),(24,35),(35,24))
        self.relate('connect','head','shaft')
        self.add_line('bottom',(8,44),(40,44))
