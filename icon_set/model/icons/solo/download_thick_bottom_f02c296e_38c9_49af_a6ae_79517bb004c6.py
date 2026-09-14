'Download arrow: clean, centered construction and equal rounded tray corners with clear space below the arrow.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f02c296e-38c9-49af-a6ae-79517bb004c6'
SOURCE_PATH = 'icons-json/arrows/download thick bottom_f02c296e-38c9-49af-a6ae-79517bb004c6.json'
AUTHOR = 'gpt-6'

class DownloadThickBottom(Solo48):
    icon_id = 'download-thick-bottom'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('download', 'thick', 'bottom', 'arrows')

    def build(self) -> None:
        # Square envelope; shared tray corners and centered downward arrow.
        self.add_line('tray-left',(6,33),(6,38))
        self.add_arc('tray-bl',(6,38),(10,42),radius_x=4,sweep=False)
        self.add_line('tray-bottom',(10,42),(38,42))
        self.add_arc('tray-br',(38,42),(42,38),radius_x=4,sweep=False)
        self.add_line('tray-right',(42,38),(42,33))
        self.add_contour('tray','tray-left','tray-bl','tray-bottom','tray-br','tray-right')
        self.add_polyline('arrow',(19,6),(29,6),(29,22),(34,22),(24,32),(14,22),(19,22),closed=True)
