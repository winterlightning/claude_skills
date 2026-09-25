from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd1281a76-8860-5291-a80f-5f2f45ccae89'
SOURCE_PATH = 'pictographic-primitives/transportation/railway station_d1281a76-8860-5291-a80f-5f2f45ccae89.svg'
AUTHOR = 'gpt-6'

class StationCanopyTrack(Solo48):
    icon_id = 'station-canopy-track'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('railway station', 'station', 'platform', 'canopy', 'track', 'train station', 'tunnel', 'rail')

    def build(self):
        self.add_polyline('roof',(4,8),(12,8),(36,8),(44,8))
        self.add_line('left-post',(12,8),(12,30))
        self.add_line('right-post',(36,8),(36,30))
        self.add_polyline('platform',(4,30),(12,30),(20,30),(28,30),(36,30),(44,30))
        self.add_line('door-left',(20,30),(20,22))
        self.add_arc('door-arch',(20,22),(28,22),radius_x=4,sweep=True)
        self.add_line('door-right',(28,22),(28,30))
        self.add_contour('entrance','door-left','door-arch','door-right')
        for p in ('left-post','right-post'):
            self.relate('connect',p,'roof')
            self.relate('connect',p,'platform')
        self.relate('connect','entrance','platform')
        self.add_polyline('track',(4,40),(12,40),(36,40),(44,40))
