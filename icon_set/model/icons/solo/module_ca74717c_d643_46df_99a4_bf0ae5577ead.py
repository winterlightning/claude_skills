'module: independent smooth-curve repair.\n\nConstruction: Open cube defined by a shared top diamond and two equal side panels; geometric edges retain purposeful corners.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/box.svg and atomic-debug/box.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'ca74717c-d643-46df-99a4-bf0ae5577ead'
SOURCE_PATH = 'pictographic-primitives/design/module_ca74717c-d643-46df-99a4-bf0ae5577ead.svg'
AUTHOR = 'gpt-6'


class Module(Solo48):
    icon_id = 'module'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('module', 'design')
    keyshape = Keyshape.HRECT_L

    def build(self):
        poly(self,'top',(24,8),(44,16),(24,24),(4,16),closed=True)
        poly(self,'walls',(4,16),(4,32),(24,40),(44,32),(44,16))
        line(self,'center',(24,24),(24,40))
        contacts(self)
