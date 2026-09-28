"""Fresh SOLO48 revision of currency-dollar from the claimed reference.

The original and rejected drawing were compared before this construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts
from icon_set.model.icons.solo._payments_batch02 import small_dollar

SOURCE_ICON_ID = '3334fbb0-436e-4762-bc8a-40fa2559c98c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__currency-dollar/20260927T071330Z-thuan-mac-1/reference/currency dollar_3334fbb0-436e-4762-bc8a-40fa2559c98c.svg'
AUTHOR = "gpt-6"

class CurrencyDollar(Solo48):
    icon_id = 'currency-dollar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    categories = ('money', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('currency', 'dollar', 'money')

    def build(self) -> None:

        line(self,'stem-top',(24,4),(24,10))
        path(self,'s',(38,12),('C',(34,10),(28,10),(24,10)),
             ('C',(14,10),(8,13),(8,18)),
             ('C',(8,23),(22,24),(28,25)),
             ('C',(36,26),(40,28),(40,31)),
             ('C',(40,36),(31,38),(24,38)),
             ('C',(18,38),(12,37),(8,36)))
        line(self,'stem-bottom',(24,38),(24,44))
        contacts(self)
