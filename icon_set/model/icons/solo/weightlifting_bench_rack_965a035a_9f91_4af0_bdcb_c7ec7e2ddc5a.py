'A weightlifting bench sits beneath a racked barbell.\nConstruction: Horizontal centerlines (6,8)-(42,40). Two rack uprights, weighted bar and central padded seat; omit stacked weight plates.\nLucide: dumbbell: strong transverse bar and paired weights.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '965a035a-9f91-4af0-bdcb-c7ec7e2ddc5a'
SOURCE_PATH = 'pictographic-primitives/sports/weighlifting bench_965a035a-9f91-4af0-bdcb-c7ec7e2ddc5a.svg'
AUTHOR = 'gpt-6'

class WeightliftingBenchRack(Solo48):
    icon_id = 'weightlifting-bench-rack'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('weightlifting', 'bench', 'rack', 'sport')

    def build(self):
        self.add_polyline('bar', (4, 8), (4, 20), (14, 20), (34, 20), (44, 20), (44, 8), closed=False)
        self.add_line('left-weight', (4, 20), (4, 28))
        self.add_line('right-weight', (44, 20), (44, 28))
        self.relate("connect", 'bar', 'left-weight')
        self.relate("connect", 'bar', 'right-weight')
        self.add_line('rack-left', (14, 20), (14, 40))
        self.add_line('rack-right', (34, 20), (34, 40))
        self.relate("connect", 'bar', 'rack-left')
        self.relate("connect", 'bar', 'rack-right')
        self.add_polyline('bench', (22, 31), (24, 31), (26, 31), closed=False)
        self.add_line('bench-leg', (24, 31), (24, 40))
        self.relate("connect", 'bench', 'bench-leg')
