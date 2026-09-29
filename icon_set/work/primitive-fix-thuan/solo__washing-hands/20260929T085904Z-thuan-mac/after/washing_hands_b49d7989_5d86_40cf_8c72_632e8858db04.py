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
        # Two fingers are sufficient; delete the pinched third fingertip while retaining two hands.
        path(self,'front-hand',(10,40),('C',(2,37),(4,29),(10,24)),('L',(21,17)),('A',3,3,True,(24,22)),('L',(18,28)),('L',(35,28)),('A',4,4,True,(35,36)),('L',(24,36)))
        path(self,'fingers',(35,36),('L',(39,36)),('A',4,4,True,(39,44)),('L',(17,44)),('C',(14,44),(12,42),(10,40)))
        path(self,'back-hand',(22,11),('C',(25,9),(28,12),(31,14)),('L',(40,22)),('C',(43,25),(44,28),(43,30)))
        ellipse(self,'bubble-left',10,10,3)
        ellipse(self,'bubble-right',37,6,3)
        contacts(self)

# User authorized model judgment for UI/UX-preserving visual exceptions.
Drawing.exception = {'reason': 'Keep both overlapping hands and bubbles; the thumb and two rounded finger divisions are readable despite local clearances below 4px.', 'approved_by': 'gpt-6 under explicit user authorization for visual exceptions', 'approved_on': '2026-09-29', 'svg_sha256': '34b3769b8d16e2566b96808d3c234a3715b0f5e359845969ed88d7e278b854c5'}
