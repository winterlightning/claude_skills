from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'b49d7989-5d86-40cf-8c72-632e8858db04'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__washing-hands/20260929T085904Z-thuan-mac/reference/washing hand_b49d7989-5d86-40cf-8c72-632e8858db04.svg'
AUTHOR = "gpt-6"

# Comparison: The fingers became an angular zigzag and the second hand became a detached diagonal bar.
# Revision: Reconstruct two overlapping rounded hands with visible finger divisions and soap bubbles.
# Plan: coherent subject contours; named parts own attachments; paired features share parameters.
class Drawing(Solo48):
    icon_id = 'washing-hands'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('washing', 'hand')

    def build(self):
        path(self,'front-hand',(10,41),('C',(2,38),(4,30),(10,25)),('L',(22,17)),('A',3,3,True,(25,22)),('L',(18,28)),('L',(36,28)),('A',3,3,True,(36,34)),('L',(24,34)))
        path(self,'fingers',(34,34),('L',(39,34)),('A',3,3,True,(39,40)),('L',(32,40)),('L',(24,40)))
        path(self,'palm',(32,40),('A',3,3,True,(29,44)),('L',(17,44)),('C',(14,44),(12,43),(10,41)))
        path(self,'back-hand',(22,12),('C',(25,9),(28,12),(31,14)),('L',(40,22)),('C',(43,25),(44,28),(43,31)))
        ellipse(self,'bubble-left',10,12,3)
        ellipse(self,'bubble-right',37,6,3)
        contacts(self)
