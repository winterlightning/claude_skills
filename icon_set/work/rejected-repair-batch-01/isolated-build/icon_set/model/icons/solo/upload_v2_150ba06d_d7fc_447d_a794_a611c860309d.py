'upload: independent smooth-curve repair.\n\nConstruction: Upright arrow with exactly mirrored arms and a centered shaft; upload variant retains its rounded receiving tray.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/arrow-up.svg and atomic-debug/arrow-up.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '150ba06d-d7fc-447d-a794-a611c860309d'
SOURCE_PATH = 'pictographic-primitives/emails/upload_150ba06d-d7fc-447d-a794-a611c860309d.svg'
AUTHOR = 'gpt-6'


class UploadVariant2(Solo48):
    icon_id = 'upload-v2'
    variant_of = 'upload'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'emails'
    aliases = ()
    keywords = ('upload', 'emails')
    keyshape = Keyshape.VRECT_L

    def build(self):
        poly(self,'head',(14,14),(24,4),(34,14))
        line(self,'shaft',(24,4),(24,30))
        path(self,'tray',(8,34),('L',(8,38)),('A',6,6,False,(14,44)),('L',(34,44)),('A',6,6,False,(40,38)),('L',(40,34)))
        contacts(self)
