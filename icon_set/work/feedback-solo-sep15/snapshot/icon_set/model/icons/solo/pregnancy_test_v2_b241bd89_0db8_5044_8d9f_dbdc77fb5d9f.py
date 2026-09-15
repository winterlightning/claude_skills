"""Center the result window within the diagonal body, preserving its shared diagonal angle. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b241bd89-0db8-5044-8d9f-dbdc77fb5d9f'
SOURCE_PATH = 'pictographic-primitives/babies/pregnancy test_b241bd89-0db8-5044-8d9f-dbdc77fb5d9f.svg'
AUTHOR = 'gpt-6'

class PregnancyTestVariant2(Solo48):
    icon_id = 'pregnancy-test-v2'
    variant_of = 'pregnancy-test'
    variant_label = 'Center the result window within the diagonal body, preserving its shared diagonal angle.'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/maternity'
    aliases = ('pregnancy-test-stick',)
    keywords = ('pregnancy', 'test', 'stick', 'result', 'fertility', 'maternity', 'medical', 'expecting')

    def build(self) -> None:
        """Symbol plan: Center the result window within the diagonal body, preserving its shared diagonal angle. Reference: inspected current parent; no useful exact Lucide match selected."""
        self.add_bezier('body', (30, 6), ((37, 6), (42, 11), (42, 18)), ((42, 27), (42, 28), (36, 34)), ((30, 40), (27, 42), (18, 42)), ((11, 42), (6, 37), (6, 30)), ((6, 21), (6, 20), (12, 14)), ((18, 8), (21, 6), (30, 6)))
        self.add_bezier('window-top', (24, 18), ((26, 16), (32, 22), (30, 24)))
        self.add_line('window-right-a', (30, 24), (27, 27))
        self.add_line('window-right-b', (27, 27), (24, 30))
        self.add_bezier('window-bottom', (24, 30), ((22, 32), (16, 26), (18, 24)))
        self.add_line('window-left-a', (18, 24), (21, 21))
        self.add_line('window-left-b', (21, 21), (24, 18))
        self.add_contour('outline', 'body', closed=True)
        self.add_contour('window', 'window-top', 'window-right-a', 'window-right-b', 'window-bottom', 'window-left-a', 'window-left-b', closed=True)
        # The result divider is omitted because it closes two undersized apertures.
        
