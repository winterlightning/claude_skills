"""An open-bottom cloud with three round network terminals and vertical stems rising into its lower opening. Preserve the cloud and connected network motif as one complete IoT subject.

Plan: Open cloud silhouette above three identical outlined terminal circles with vertical stems. Bounds (4,8)-(44,40).
Construction reference: Lucide cloud: unequal cloud lobes and open lower region; source supplies network terminals."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd32e133b-6689-4cde-8526-21a32ea3b111'
SOURCE_PATH = 'pictographic-primitives/programing/internet of thing core_d32e133b-6689-4cde-8526-21a32ea3b111.svg'
SOURCE_ICON_IDS = ('d32e133b-6689-4cde-8526-21a32ea3b111',)
AUTHOR = 'gpt-6'

class CloudWithNetworkStems(Solo48):
    icon_id = 'cloud-with-network-stems'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('cloud', 'with', 'network', 'stems')

    def build(self) -> None:
        self.add_bezier('cloud',(4,24),((4,22),(4,20),(4,18)),((4,12),(9,8),(15,8)),((22,8),(26,12),(28,16)),((36,12),(44,16),(44,22)),((44,23),(44,24),(44,24)))
        for i,(x,y) in enumerate(((10,34),(24,28),(38,34))):
            self.add_arc(f'terminal-{i}-a',(x,y-3),(x,y+3),radius_x=3)
            self.add_arc(f'terminal-{i}-b',(x,y+3),(x,y-3),radius_x=3)
            self.add_contour(f'terminal-{i}',f'terminal-{i}-a',f'terminal-{i}-b',closed=True)
            self.add_line(f'stem-{i}',(x,y+3),(x,40))
            self.relate('connect',f'terminal-{i}',f'stem-{i}')
