'Broken link: preserve two separated curved chain halves with two clear fracture rays; omit the crowded middle ray.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'db03fa02-7797-54ce-b9f4-d8c10fd4b4a5'
SOURCE_PATH = 'icons-json/interface-essential/link broken_db03fa02-7797-54ce-b9f4-d8c10fd4b4a5.json'
AUTHOR = 'gpt-6'

class LinkBroken(Solo48):
    icon_id = 'link-broken'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('link', 'broken', 'interface-essential')

    def build(self) -> None:
        self.add_bezier('upper-link',(24,18),((27,14),(29,8),(33,8)),((37,8),(40,11),(40,15)),((40,19),(35,23),(31,27)))
        self.add_bezier('lower-link',(16,26),((12,30),(8,34),(8,38)),((8,42),(11,44),(15,44)),((19,44),(23,39),(25,36)))
        self.add_line('spark-top',(16,4),(16,10))
        self.add_line('spark-left',(8,17),(12,17))
