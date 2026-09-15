'bookmark-interface-essential: independent smooth-curve repair.\n\nConstruction: Bookmark with equal rounded top corners and a centered V notch.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/bookmark.svg and atomic-debug/bookmark.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'fc3ca28d-5459-5622-8b36-d8ebe44e32ab'
SOURCE_PATH = 'pictographic-primitives/interface-essential/bookmark_fc3ca28d-5459-5622-8b36-d8ebe44e32ab.svg'
AUTHOR = 'gpt-6'


class BookmarkInterfaceEssential(Solo48):
    icon_id = 'bookmark-interface-essential'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('bookmark', 'interface-essential')
    keyshape = Keyshape.VRECT_L

    def build(self):
        path(self,'bookmark',(8,44),('L',(8,8)),('A',4,4,True,(12,4)),('L',(36,4)),('A',4,4,True,(40,8)),('L',(40,44)),('L',(24,33)),('L',(8,44)),closed=True)
        contacts(self)
