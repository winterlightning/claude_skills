'massage-bed: independent smooth-curve repair.\n\nConstruction: Massage bench with a rounded bolster top and two evenly spaced legs.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/table.svg and atomic-debug/table.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '6658e426-76a2-54d7-bcab-12976366ac72'
SOURCE_PATH = 'pictographic-primitives/beauty/massage bed_6658e426-76a2-54d7-bcab-12976366ac72.svg'
AUTHOR = 'gpt-6'


class MassageBed(Solo48):
    icon_id = 'massage-bed'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'beauty'
    categories = ('primitives', 'beauty')
    aliases = ()
    keywords = ('massage', 'bed', 'beauty')
    keyshape = Keyshape.HRECT_L

    def build(self):
        box(self,'top',4,8,44,20,4,xs=(10,38))
        line(self,'left-leg',(10,20),(10,40));line(self,'right-leg',(38,20),(38,40))
        line(self,'brace',(10,30),(38,30))
        contacts(self)
