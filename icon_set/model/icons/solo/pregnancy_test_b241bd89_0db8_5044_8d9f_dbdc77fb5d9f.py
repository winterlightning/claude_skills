"""Diagonal test stick. SQUARE extremes (2,2)-(46,46). Lucide pipette informs diagonal shaft and rounded handle. Capsule window retains one result bar."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b241bd89-0db8-5044-8d9f-dbdc77fb5d9f'
SOURCE_PATH = 'pictographic-primitives/babies/pregnancy test_b241bd89-0db8-5044-8d9f-dbdc77fb5d9f.svg'
AUTHOR = 'gpt-6'

class PregnancyTest(Solo48):
    icon_id = 'pregnancy-test'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/maternity'
    aliases = ('pregnancy-test-stick',)
    keywords = ('pregnancy', 'test', 'stick', 'result', 'fertility', 'maternity', 'medical', 'expecting')

    def build(self) -> None:
        self.add_arc('handle-top', (30,4), (46,12), radius_x=10)
        self.add_arc('handle-right', (46,12), (42,20), radius_x=10)
        self.add_line('shoulder-right-1', (42,20), (38,26))
        self.add_line('shoulder-right-2', (38,26), (37,30))
        self.add_line('shoulder-right-3', (37,30), (29,40))
        self.add_arc('body-bottom', (29,40), (17,46), radius_x=15)
        self.add_arc('body-left', (17,46), (2,31), radius_x=15)
        self.add_arc('body-upper', (2,31), (8,19), radius_x=15)
        self.add_line('shoulder-left-1', (8,19), (20,10))
        self.add_line('shoulder-left-2', (20,10), (25,9))
        self.add_line('shoulder-left-3', (25,9), (30,4))
        self.add_contour('outline', 'handle-top', 'handle-right', 'shoulder-right-1', 'shoulder-right-2', 'shoulder-right-3', 'body-bottom', 'body-left', 'body-upper', 'shoulder-left-1', 'shoulder-left-2', 'shoulder-left-3', closed=True)
        self.add_arc('window-top', (19,19), (27,25), radius_x=5)
        self.add_line('window-right-a', (27,25), (23,30))
        self.add_line('window-right-b', (23,30), (19,35))
        self.add_arc('window-bottom', (19,35), (11,29), radius_x=5)
        self.add_line('window-left-a', (11,29), (15,24))
        self.add_line('window-left-b', (15,24), (19,19))
        self.add_contour('window', 'window-top', 'window-right-a', 'window-right-b', 'window-bottom', 'window-left-a', 'window-left-b', closed=True)
        self.add_line('result', (15,24), (23,30))
        self.relate('connect', 'result', 'window')
