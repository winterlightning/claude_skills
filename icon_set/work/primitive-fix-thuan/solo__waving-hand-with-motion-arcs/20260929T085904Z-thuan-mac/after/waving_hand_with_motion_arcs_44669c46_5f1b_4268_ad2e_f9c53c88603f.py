from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '44669c46-5f1b-4268-ad2e-f9c53c88603f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__waving-hand-with-motion-arcs/20260929T085904Z-thuan-mac/reference/photo motion sensor_44669c46-5f1b-4268-ad2e-f9c53c88603f.svg'
AUTHOR = "gpt-6"

# Comparison: The waving hand had too few fingers and only one motion stroke, making the gesture generic.
# Revision: Restore four splayed fingertips, the raised thumb and two motion cues around a rounded palm.
# Plan: coherent subject contours; named parts own attachments; paired features share parameters.
class Drawing(Solo48):
    icon_id = 'waving-hand-with-motion-arcs'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('photo', 'motion', 'sensor')

    def build(self):
        path(self,'hand',(12,25),('L',(13,17)),('C',(13,12),(8,12),(8,17)),('L',(6,29)),('C',(5,38),(12,44),(21,43)),('C',(26,42),(29,38),(32,35)),('L',(42,25)),('A',3,3,False,(38,21)),('L',(31,28)),('L',(43,16)),('A',3,3,False,(39,12)),('L',(28,23)),('L',(39,12)),('A',3,3,False,(35,8)),('L',(24,19)),('L',(32,11)),('A',3,3,False,(28,7)),('L',(12,25)),closed=True)
        path(self,'motion-left',(3,17),('C',(3,10),(6,6),(11,4)))
        path(self,'motion-right',(35,43),('C',(40,41),(43,37),(44,32)))
        contacts(self)

# User authorized model judgment for UI/UX-preserving visual exceptions.
Drawing.exception = {'reason': 'Four splayed fingers, thumb and both motion cues are essential to the reference. Finger channels remain distinguishable at native size despite reduced spacing.', 'approved_by': 'gpt-6 under explicit user authorization for visual exceptions', 'approved_on': '2026-09-29', 'svg_sha256': 'b9e20208ccfe7da0c4f09b976fae0d729a87e4fbb8fce4ddc00f892be3b059fb'}
