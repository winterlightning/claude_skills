'Upload: centred upward arrow and tangent tray corners, with a five-unit ink gap above the tray.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ce7bfa1f-3141-47ae-9f87-a6e785f26d0a'
SOURCE_PATH = 'pictographic-primitives/arrows/upload bottom_ce7bfa1f-3141-47ae-9f87-a6e785f26d0a.svg'
AUTHOR = 'gpt-6'

class UploadBottom(Solo48):
    icon_id = 'upload-bottom'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('upload', 'bottom', 'arrows')

    def build(self) -> None:
        self.add_line('shaft',(24,8),(24,31))
        self.add_polyline('head',(14,18),(24,8),(34,18))
        self.relate('connect','head','shaft')
        self.add_line('tray-left',(4,30),(4,36))
        self.add_arc('tray-bl',(4,36),(8,40),radius_x=4,sweep=False)
        self.add_line('tray-bottom',(8,40),(40,40))
        self.add_arc('tray-br',(40,40),(44,36),radius_x=4,sweep=False)
        self.add_line('tray-right',(44,36),(44,30))
        self.add_contour('tray','tray-left','tray-bl','tray-bottom','tray-br','tray-right')
