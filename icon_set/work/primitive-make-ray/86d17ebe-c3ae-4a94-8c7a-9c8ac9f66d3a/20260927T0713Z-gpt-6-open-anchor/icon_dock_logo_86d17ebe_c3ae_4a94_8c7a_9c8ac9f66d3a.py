"""Open arrowhead anchor rebuilt from the claimed Icon Dock logo reference.

The rejected drawing made the side flukes into bulky enclosed hooks; the source uses a
long centerline, a lower V, and separated open arrowhead arms.
Lucide anchor informed the ring and shaft relationship; the source determines the V.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import ellipse, line, poly, contacts

SOURCE_ICON_ID = '86d17ebe-c3ae-4a94-8c7a-9c8ac9f66d3a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__icon-dock-logo/20260927T070901Z-thuan-mac-1/reference/icon dock logo_86d17ebe-c3ae-4a94-8c7a-9c8ac9f66d3a.svg'
AUTHOR = "gpt-6"

class IconDockLogo(Solo48):
    icon_id = 'icon-dock-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('icon-dock','anchor','logo','brand')

    def build(self) -> None:
        ellipse(self,'ring',24,12,6)
        line(self,'shaft',(24,18),(24,42))
        poly(self,'flukes',(13,28),(24,42),(35,28))
        poly(self,'arrow-left',(7,32),(6,24),(13,28))
        poly(self,'arrow-right',(35,28),(42,24),(41,32))
        contacts(self)
