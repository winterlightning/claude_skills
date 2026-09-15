'Download arrow: clean, centered construction and equal rounded tray corners with clear space below the arrow.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '420aaab1-7942-44fa-a853-3e16edd896fd'
SOURCE_PATH = 'pictographic-primitives/internet/download bottom_420aaab1-7942-44fa-a853-3e16edd896fd.svg'
AUTHOR = 'gpt-6'

class DownloadBottom(Solo48):
    icon_id = 'download-bottom'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'internet'
    aliases = ()
    keywords = ('download', 'bottom', 'internet')

    def build(self) -> None:
        # Square envelope; shared tray corners and centered downward arrow.
        self.add_line('tray-left',(6,33),(6,38))
        self.add_arc('tray-bl',(6,38),(10,42),radius_x=4,sweep=False)
        self.add_line('tray-bottom',(10,42),(38,42))
        self.add_arc('tray-br',(38,42),(42,38),radius_x=4,sweep=False)
        self.add_line('tray-right',(42,38),(42,33))
        self.add_contour('tray','tray-left','tray-bl','tray-bottom','tray-br','tray-right')
        self.add_polyline('head',(14,23),(24,33),(34,23))
        self.add_line('shaft',(24,6),(24,33))
        self.relate('connect','shaft','head')
