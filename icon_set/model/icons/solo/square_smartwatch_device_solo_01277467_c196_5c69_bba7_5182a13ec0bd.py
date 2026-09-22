"""Square Smartwatch Device: standalone SOLO48 reconstruction.
Source render supplies essential parts and arrangement. Lucide construction
reference and ownership plan are recorded in build. Original artwork preserved.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
from ._symmetry_curves import path, ellipse, box, contacts
SOURCE_ICON_ID = '01277467-c196-5c69-bba7-5182a13ec0bd'
SOURCE_PATH = 'pictographic-primitives/devices/smart watch square_01277467-c196-5c69-bba7-5182a13ec0bd.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'square-smartwatch-device-solo'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'devices'
    aliases = ('Square Smartwatch Device',)
    keywords = ('square', 'smartwatch', 'device')
    def build(self):
        # Shared x axis and mirrored straps; face owns exact strap attachment nodes.
        # Lucide watch teaches the strap/face join; rounded face replaces its circle.
        box(self,'face',10,12,38,36,4,xs=(16,32))
        for name,edge,extreme,corner in [('top',12,4,7),('bottom',36,44,41)]:
            sign=1 if name=='top' else -1
            path(self,name,(16,edge),('L',(17,corner)),
                 ('C',(17,extreme+sign),(18,extreme),(20,extreme)),
                 ('L',(28,extreme)),
                 ('C',(30,extreme),(31,extreme+sign),(31,corner)),
                 ('L',(32,edge)))
            self.relate('connect','face',name)
