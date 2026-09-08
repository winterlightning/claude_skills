from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '62ffc005-105c-5ac9-aefb-e949fc1fa313'
SOURCE_PATH = 'pictographic-primitives/animals/sheep_62ffc005-105c-5ac9-aefb-e949fc1fa313.svg'
AUTHOR = 'gpt-6'


class SheepHead(Solo48):
    icon_id = 'sheep-head'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/farm"
    aliases = ()
    keywords = ('sheep', 'head', 'face', 'ears', 'lamb', 'farm', 'minimal', 'animal')

    def build(self) -> None:
        self.add_arc('crown', (10, 19), (38, 19), radius_x=14, radius_y=14, sweep=True, large_arc=False)
        self.add_arc('chin-right', (38, 19), (24, 43), radius_x=14, radius_y=24, sweep=True, large_arc=False)
        self.add_arc('chin-left', (24, 43), (10, 19), radius_x=14, radius_y=24, sweep=True, large_arc=False)
        self.add_contour('face', 'crown', 'chin-right', 'chin-left', closed=True)
        self.add_line('ear-left-1', (10, 19), (2, 29))
        self.add_line('ear-left-2', (2, 29), (5, 31))
        self.add_contour('ear-left', 'ear-left-1', 'ear-left-2', closed=False)
        self.add_line('ear-right-1', (38, 19), (46, 29))
        self.add_line('ear-right-2', (46, 29), (43, 31))
        self.add_contour('ear-right', 'ear-right-1', 'ear-right-2', closed=False)
        self.relate("connect", 'ear-left', 'face')
        self.relate("connect", 'ear-right', 'face')
        self.add_line('mouth-1', (18, 31), (24, 36))
        self.add_line('mouth-2', (24, 36), (30, 31))
        self.add_contour('mouth', 'mouth-1', 'mouth-2', closed=False)
        self.add_line('chin-mark', (24, 36), (24, 43))
        self.relate("connect", 'chin-mark', 'mouth')
        self.relate("connect", 'chin-mark', 'face')
