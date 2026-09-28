"""Fresh SOLO48 revision of house-with-smoking-chimney from its claimed original reference.

The original and rejected drawing were compared before this construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'ab402af4-7fa5-59c6-8861-78bb8c0e3f7e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__house-with-smoking-chimney/20260927T061852Z-thuan-mac-1/reference/house chimney smoke_ab402af4-7fa5-59c6-8861-78bb8c0e3f7e.svg'
AUTHOR = "gpt-6"

class BatchSolo(Solo48):
    icon_id = 'house-with-smoking-chimney'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'building'
    categories = ('building', 'primitives')
    aliases = ()
    keywords = ('house', 'with', 'smoking', 'chimney')

    def build(self) -> None:

        # Pitched roof, arched door, chimney and wavy smoke.
        poly(self,'house',(6,42),(6,29),(20,18),(34,29),(34,42),closed=True)
        path(self,'door',(16,42),('L',(16,36)),('A',4,4,True,(24,36)),('L',(24,42)))
        poly(self,'chimney',(32,27),(32,16),(38,16),(38,22))
        self.add_bezier('smoke',(35,12),((31,9),(39,9),(39,6)))
        contacts(self)
