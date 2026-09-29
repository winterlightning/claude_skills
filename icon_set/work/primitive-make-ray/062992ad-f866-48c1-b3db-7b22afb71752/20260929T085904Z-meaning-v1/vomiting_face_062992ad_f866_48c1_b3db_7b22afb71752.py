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
        path(self,'face',(12,38),('C',(3,30),(4,16),(12,10)),('C',(19,4),(30,4),(37,12)),('C',(45,21),(43,31),(36,38)))
        poly(self,'left-eye',(13,17),(17,20),(12,22))
        poly(self,'right-eye',(35,17),(31,20),(36,22))
        path(self,'mouth',(14,33),('C',(10,25),(38,25),(34,33)))
        path(self,'vomit',(18,31),('C',(18,36),(16,37),(13,39)),('C',(9,42),(14,45),(19,41)),('C',(23,45),(26,45),(29,41)),('C',(34,45),(39,42),(35,39)),('C',(32,37),(30,36),(30,31)))
        contacts(self)
