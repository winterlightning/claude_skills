'camera-video: independent smooth-curve repair.\n\nConstruction: Camera body with an integrated raised shutter housing and one centered lens dot.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/camera.svg and atomic-debug/camera.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '0313a853-8fee-401d-b021-0624788b6cd1'
SOURCE_PATH = 'pictographic-primitives/video/camera_0313a853-8fee-401d-b021-0624788b6cd1.svg'
AUTHOR = 'gpt-6'


class CameraVideo(Solo48):
    icon_id = 'camera-video'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video'
    aliases = ()
    keywords = ('camera', 'video')
    keyshape = Keyshape.HRECT_L

    def build(self):
        path(self,'body',(8,12),('L',(16,12)),('A',4,4,True,(20,8)),('L',(28,8)),('A',4,4,True,(32,12)),('L',(40,12)),('A',4,4,True,(44,16)),('L',(44,36)),('A',4,4,True,(40,40)),('L',(8,40)),('A',4,4,True,(4,36)),('L',(4,16)),('A',4,4,True,(8,12)),closed=True)
        self.add_dot('lens',(24,26))
        contacts(self)
