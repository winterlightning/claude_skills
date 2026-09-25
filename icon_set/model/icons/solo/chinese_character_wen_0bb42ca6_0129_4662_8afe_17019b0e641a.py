"""Chinese Language Character. Retains the identifying silhouette and visible features.

SQUARE visible extremes (4, 4, 44, 44); centerlines (6, 6, 42, 42).
Supplied reference; no useful exact Lucide match found.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0bb42ca6-0129-4662-8afe-17019b0e641a'
SOURCE_PATH = 'pictographic-primitives/symbol/chinese language symbol_0bb42ca6-0129-4662-8afe-17019b0e641a.svg'
AUTHOR = 'gpt-6'


class ChineseCharacterWen(Solo48):
    icon_id = 'chinese-character-wen'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    aliases = ()
    keywords = ('chinese', 'language', 'character', 'translate', 'wen', 'script', 'writing', 'text')

    def build(self) -> None:
        self.add_polyline('bar', (6, 14), (14, 14), (24, 14), (34, 14), (42, 14))
        self.add_line('tick', (24, 6), (24, 14))
        self.relate("connect", 'bar', 'tick')
        self.add_arc('down-right-a', (14, 14), (24, 30), radius_x=40, radius_y=40, sweep=False)
        self.add_arc('down-right-b', (24, 30), (42, 42), radius_x=40, radius_y=40, sweep=False)
        self.add_contour('down-right', 'down-right-a', 'down-right-b')
        self.add_arc('down-left-a', (34, 14), (24, 30), radius_x=40, radius_y=40, sweep=True)
        self.add_arc('down-left-b', (24, 30), (6, 42), radius_x=40, radius_y=40, sweep=True)
        self.add_contour('down-left', 'down-left-a', 'down-left-b')
        self.relate("connect", 'down-left', 'down-right')
        self.relate("connect", 'bar', 'down-left')
        self.relate("connect", 'bar', 'down-right')
