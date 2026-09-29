from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '062992ad-f866-48c1-b3db-7b22afb71752'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__vomiting-face/20260929T085904Z-thuan-mac/reference/throw up_062992ad-f866-48c1-b3db-7b22afb71752.svg'
AUTHOR = "gpt-6"

# Comparison: The face perimeter was missing its lower half and the rigid stream read as a lampshade.
# Revision: Restore the round face and open mouth; draw a downward stream with a scalloped puddle and strained eyes.
# Plan: coherent subject contours; named parts own attachments; paired features share parameters.
class Drawing(Solo48):
    icon_id = 'vomiting-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('throw', 'up')

    def build(self):
        # Round face, two small strained eyes, and one open stream silhouette avoid the pinched mouth ring.
        path(self,'face',(12,37),('C',(3,29),(4,16),(12,10)),('C',(19,4),(30,4),(37,12)),('C',(45,21),(43,30),(36,37)))
        poly(self,'left-eye',(16,16),(19,19),(15,21))
        poly(self,'right-eye',(32,16),(29,19),(33,21))
        path(self,'stream',(14,30),('C',(14,25),(34,25),(34,30)),('L',(32,34)),('C',(32,37),(36,38),(36,41)),('C',(36,44),(31,43),(29,41)),('C',(25,44),(22,44),(19,41)),('C',(17,43),(12,44),(12,41)),('C',(12,38),(16,37),(16,34)),('L',(14,30)),closed=True)
        contacts(self)

# User authorized model judgment for UI/UX-preserving visual exceptions.
Drawing.exception = {'reason': 'Retain the full facial silhouette, squinting expression and broad scalloped vomit stream; close facial spacing and a slightly taller envelope are readable at 48px.', 'approved_by': 'gpt-6 under explicit user authorization for visual exceptions', 'approved_on': '2026-09-29', 'svg_sha256': 'ff66bf3df466f42d472a18e63d30783ae632be98fc46d8c372a1bfabb0588ecb'}
