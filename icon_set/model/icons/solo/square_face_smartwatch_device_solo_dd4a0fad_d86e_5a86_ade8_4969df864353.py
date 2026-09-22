"""Square Face Smartwatch Device: standalone SOLO48 reconstruction.
Source render supplies essential parts and arrangement. Lucide construction
reference and ownership plan are recorded in build. Original artwork preserved.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
from ._symmetry_curves import path, ellipse, box, contacts
SOURCE_ICON_ID = 'dd4a0fad-d86e-5a86-ade8-4969df864353'
SOURCE_PATH = 'pictographic-primitives/devices/wearable smart watch square_dd4a0fad-d86e-5a86-ade8-4969df864353.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'square-face-smartwatch-device-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'devices'
    aliases = ('Square Face Smartwatch Device',)
    keywords = ('square', 'face', 'smartwatch', 'device')
    def build(self):
        # Front face owns four strap joins; a rear band bends to the right.
        # SQUARE accommodates perspective width; Lucide watch informs attachment flow.
        box(self,'face',6,15,28,33,4,xs=(10,24))
        path(self,'upper-band',(10,15),('C',(13,9),(18,6),(22,6)),
             ('L',(30,6)),('C',(36,6),(42,15),(42,20)),
             ('C',(42,23),(39,24),(36,24)))
        path(self,'upper-inner',(30,6),('C',(27,8),(25,11),(24,15)))
        path(self,'lower-band',(10,33),('C',(13,39),(18,42),(22,42)),
             ('L',(30,42)),('C',(37,42),(40,38),(42,32)))
        path(self,'lower-inner',(30,42),('C',(27,40),(25,37),(24,33)))
        contacts(self)
