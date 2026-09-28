"""Center the result window within the diagonal body, preserving its shared diagonal angle. Applied to the original icon identity."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b241bd89-0db8-5044-8d9f-dbdc77fb5d9f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__pregnancy-test/20260927T170540Z-thuan-mac-1/reference/pregnancy test_b241bd89-0db8-5044-8d9f-dbdc77fb5d9f.svg'
AUTHOR = 'gpt-6'

class PregnancyTest(Solo48):
    icon_id = 'pregnancy-test'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'babies'
    categories = ('babies', 'primitives')
    aliases = ('pregnancy-test-stick',)
    keywords = ('pregnancy', 'test', 'stick', 'result', 'fertility', 'maternity', 'medical', 'expecting')

    def build(self) -> None:
        """Symbol plan: Center the result window within the diagonal body, preserving its shared diagonal angle. Reference: inspected current parent; no useful exact Lucide match selected."""
        self.add_bezier('body', (34, 6), ((39, 6), (42, 10), (42, 16)), ((42, 20), (40, 22), (35, 27)), ((27, 35), (22, 42), (16, 42)), ((10, 42), (6, 38), (6, 32)), ((6, 28), (8, 25), (13, 20)), ((21, 12), (29, 6), (34, 6)))
        self.add_contour('outline', 'body', closed=True)
        self.add_line('window', (20,28), (27,21))
