"""Ui columns (apps), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '87c9b933-0954-4c85-b549-2051219db557'
SOURCE_PATH = 'icons-json/apps/ui columns_87c9b933-0954-4c85-b549-2051219db557.json'
AUTHOR = 'json_to_solo'

class UiColumnsApps(Solo48):
    icon_id = 'ui-columns-apps'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'apps'
    aliases = ()
    keywords = ('ui', 'columns', 'apps')

    def build(self):
        self.add_line('e0', (28, 23), (44, 23))
        self.add_line('e1', (28, 23), (28, 40))
        self.add_line('e2', (28, 40), (44, 40))
        self.add_line('e3', (44, 40), (44, 23))
        self.add_line('e4', (28, 23), (28, 8))
        self.add_line('e5', (28, 8), (44, 8))
        self.add_line('e6', (44, 8), (44, 23))
        self.add_line('e7', (5, 8), (19, 8))
        self.add_line('e8', (20, 9), (20, 39))
        self.add_line('e9', (19, 40), (5, 40))
        self.add_line('e10', (4, 39), (4, 9))
        self.add_bezier('e11', (4, 9), ((4.264, 8.646), (4.336, 8), (5, 8)))
        self.add_bezier('e12', (19, 8), ((19.127, 8.034), (19.718, 8.067), (19.845, 8.109)), ((20.182, 8.303), (19.809, 8.731), (20, 9)))
        self.add_bezier('e13', (20, 39), ((19.845, 39.211), (20.227, 39.621), (19.982, 39.815)), ((19.818, 39.941), (19.145, 39.907), (19, 40)))
        self.add_bezier('e14', (5, 40), ((4.8, 39.916), (4, 39.731), (4, 39.629)), ((4, 39.469), (4, 39.16), (4, 39)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3')
        self.add_contour('c2', 'e4', 'e5', 'e6')
        self.add_contour('c3', 'e11', 'e7', 'e12', 'e8', 'e13', 'e9', 'e14', 'e10', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
