from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '49aa3ae9-4599-4f0a-839e-996103c1a778'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__wireless-mouse-with-signal/20260929T085904Z-thuan-mac/reference/mouse remote_49aa3ae9-4599-4f0a-839e-996103c1a778.svg'
AUTHOR = "gpt-6"

# Comparison: The mouse was too round and the two signal arcs crowded it, so it read as a wireless power button.
# Revision: Give the mouse a long capsule body and scroll wheel with two separated wireless arcs above it.
# Plan: coherent subject contours; named parts own attachments; paired features share parameters.
class Drawing(Solo48):
    icon_id = 'wireless-mouse-with-signal'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('mouse', 'remote')

    def build(self):
        path(self,'mouse',(14,28),('A',10,10,True,(34,28)),('L',(34,34)),('A',10,10,True,(14,34)),('L',(14,28)),closed=True)
        line(self,'scroll-wheel',(24,26),(24,30))
        path(self,'signal-outer',(10,9),('C',(18,2),(30,2),(38,9)))
        path(self,'signal-inner',(18,14),('C',(22,10),(26,10),(30,14)))
        contacts(self)
