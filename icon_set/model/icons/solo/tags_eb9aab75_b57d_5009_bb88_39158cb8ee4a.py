'tags: independent smooth-curve repair.\n\nConstruction: Tag with a gently rounded roof and lower corners; circular hanging hole.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/tag.svg and atomic-debug/tag.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'eb9aab75-b57d-5009-bb88-39158cb8ee4a'
SOURCE_PATH = 'pictographic-primitives/interface-essential/tags_eb9aab75-b57d-5009-bb88-39158cb8ee4a.svg'
AUTHOR = 'gpt-6'


class Tags(Solo48):
    icon_id = 'tags'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('tags', 'interface-essential')
    keyshape = Keyshape.VRECT_L

    def build(self):
        path(self,'tag',(8,40),('L',(8,20)),('C',(8,17),(17,8),(21,5)),('C',(23,3.666666667),(25,3.666666667),(27,5)),('C',(31,8),(40,17),(40,20)),('L',(40,40)),('A',4,4,True,(36,44)),('L',(12,44)),('A',4,4,True,(8,40)),closed=True)
        ellipse(self,'hole',24,19,3)
        contacts(self)
