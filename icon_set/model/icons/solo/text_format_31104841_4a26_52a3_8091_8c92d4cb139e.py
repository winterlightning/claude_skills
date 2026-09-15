'text-format: independent smooth-curve repair.\n\nConstruction: Capital T with a balanced top bar and base serif.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/type.svg and atomic-debug/type.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '31104841-4a26-52a3-8091-8c92d4cb139e'
SOURCE_PATH = 'pictographic-primitives/interface-essential/text format_31104841-4a26-52a3-8091-8c92d4cb139e.svg'
AUTHOR = 'gpt-6'


class TextFormat(Solo48):
    icon_id = 'text-format'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('text', 'format', 'interface-essential')
    keyshape = Keyshape.VRECT_L

    def build(self):
        line(self,'top',(8,4),(40,4));line(self,'stem',(24,4),(24,44));line(self,'foot',(17,44),(31,44))
        contacts(self)
