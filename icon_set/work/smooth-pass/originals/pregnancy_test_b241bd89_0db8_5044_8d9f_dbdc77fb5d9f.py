"""Diagonal test stick. SQUARE extremes (6,6)-(42,42). Lucide pipette informs diagonal shaft and rounded handle. Capsule window retains one result bar."""
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
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_bezier('handle-top', (30, 6), *(((34.94725664, 6), (40.13410646, 7.21534935), (42, 12)),))
        self.add_bezier('handle-right', (42, 12), *(((42, 14.55050463), (42, 17.44949537), (42, 20)),))
        self.add_line('shoulder-right-1', (42, 20), (38, 26))
        self.add_line('shoulder-right-2', (38, 26), (37, 30))
        self.add_line('shoulder-right-3', (37, 30), (29, 40))
        self.add_bezier('body-bottom', (29, 40), *(((25.46201701, 42), (21.10294156, 42), (17, 42)),))
        self.add_arc('body-left', (17, 42), (6, 31), radius_x=15, radius_y=15, large_arc=False, sweep=True)
        self.add_bezier('body-upper', (6, 31), *(((6, 26.89705844), (6, 22.53798299), (8, 19)),))
        self.add_line('shoulder-left-1', (8, 19), (20, 10))
        self.add_line('shoulder-left-2', (20, 10), (25, 9))
        self.add_line('shoulder-left-3', (25, 9), (30, 6))
        self.add_arc('window-top', (21, 20), (28, 25), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('window-right-a', (28, 25), (25, 30))
        self.add_line('window-right-b', (25, 30), (21, 33))
        self.add_arc('window-bottom', (21, 33), (15, 29), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('window-left-a', (15, 29), (18, 24))
        self.add_line('window-left-b', (18, 24), (21, 20))
        self.add_line('result', (18, 24), (25, 30))
        self.add_contour('outline', *('handle-top', 'handle-right', 'shoulder-right-1', 'shoulder-right-2', 'shoulder-right-3', 'body-bottom', 'body-left', 'body-upper', 'shoulder-left-1', 'shoulder-left-2', 'shoulder-left-3'), closed=True)
        self.add_contour('window', *('window-top', 'window-right-a', 'window-right-b', 'window-bottom', 'window-left-a', 'window-left-b'), closed=True)
        self.relate('connect', *('result', 'window'))
