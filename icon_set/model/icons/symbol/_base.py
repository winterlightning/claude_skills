"""The symbol family owns the SYMBOL32 profile."""
from ...keyshapes import Keyshape
from ..family import FamilyIcon
class Symbol32(FamilyIcon):
    family = 'symbol'
    icon_id = ''
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ()
