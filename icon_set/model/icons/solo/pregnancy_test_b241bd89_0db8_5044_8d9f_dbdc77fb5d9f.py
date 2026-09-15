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
        # One diagonal rounded body; matching tangents replace the faceted shoulders.
        self.add_bezier('body',(30,6),((37,6),(42,11),(42,18)),((42,27),(42,28),(36,34)),((30,40),(27,42),(18,42)),((11,42),(6,37),(6,30)),((6,21),(6,20),(12,14)),((18,8),(21,6),(30,6)))
        self.add_bezier('window-top',(23,21),((25,19),(31,25),(29,27)))
        self.add_line('window-right-a',(29,27),(26,30))
        self.add_line('window-right-b',(26,30),(23,33))
        self.add_bezier('window-bottom',(23,33),((21,35),(15,29),(17,27)))
        self.add_line('window-left-a',(17,27),(20,24))
        self.add_line('window-left-b',(20,24),(23,21))
        self.add_contour('outline','body',closed=True)
        self.add_contour('window','window-top','window-right-a','window-right-b','window-bottom','window-left-a','window-left-b',closed=True)
        self.add_line('result',(20,24),(26,30))
        self.relate('connect','result','window')
