from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'f112a16f-0b5c-4192-abdc-173f55e6a032'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__wavy-dollar-bill/20260929T085904Z-thuan-mac/reference/money bill wave_f112a16f-0b5c-4192-abdc-173f55e6a032.svg'
AUTHOR = "gpt-6"

# Comparison: The dollar sign looked like an S because the vertical stroke had been reduced to tiny end knobs.
# Revision: Restore an unmistakable vertical dollar bar crossing a smooth S, centered inside the waving banknote.
# Plan: coherent subject contours; named parts own attachments; paired features share parameters.
class Drawing(Solo48):
    icon_id = 'wavy-dollar-bill'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('money', 'bill', 'wave')

    def build(self):
        path(self,'bill',(4,11),('C',(17,2),(31,16),(44,9)),('L',(44,37)),('C',(31,44),(17,30),(4,39)),('L',(4,11)),closed=True)
        path(self,'dollar',(29,19),('C',(21,13),(15,23),(24,24)),('C',(34,25),(27,35),(19,29)))
        line(self,'dollar-bar',(24,14),(24,34))
        contacts(self)
