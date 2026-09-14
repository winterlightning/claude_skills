"""Virtual coin cyrpto currency (design), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '573e6276-1546-4e04-a069-78d9e36ee390'
SOURCE_PATH = 'icons-json/design/virtual coin cyrpto currency_573e6276-1546-4e04-a069-78d9e36ee390.json'
AUTHOR = 'json_to_solo'

class VirtualCoinCyrptoCurrencyDesign(Solo48):
    icon_id = 'virtual-coin-cyrpto-currency-design'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('virtual', 'coin', 'cyrpto', 'currency', 'design')

    def build(self):
        self.add_line('e0', (41, 25), (25, 34))
        self.add_line('e1', (23, 34), (7, 25))
        self.add_line('e2', (7, 33), (23, 42))
        self.add_line('e3', (25, 42), (41, 33))
        self.add_line('e4', (7, 17), (23, 25))
        self.add_line('e5', (25, 25), (41, 17))
        self.add_line('e6', (41, 15), (25, 6))
        self.add_line('e7', (23, 6), (7, 15))
        self.add_bezier('e8', (40, 22), ((40.344, 22.229), (41.223, 22.805), (41.485, 23.133)), ((41.615, 23.28), (41.583, 23.509), (41.665, 23.689)), ((41.771, 23.918), (41.885, 24.139), (42, 24.368)), ((41.73, 24.515), (41.27, 24.853), (41, 25)))
        self.add_bezier('e9', (25, 34), ((24.615, 34.213), (23.385, 34.213), (23, 34)))
        self.add_bezier('e10', (7, 25), ((6.702, 24.839), (6, 24.081), (6, 23.699)), ((6, 23.693), (6, 23.687), (6, 23.681)), ((6, 23.035), (7.509, 22.237), (8, 22)))
        self.add_bezier('e11', (8, 31), ((7.583, 31.278), (6, 31.527), (6, 32.051)), ((6, 32.37), (6.787, 32.787), (7, 33)))
        self.add_bezier('e12', (23, 42), ((23.196, 42), (23.566, 42), (23.763, 42)), ((23.926, 42), (24.098, 42), (24.27, 42)), ((24.45, 42), (24.82, 42), (25, 42)))
        self.add_bezier('e13', (41, 33), ((41.286, 32.845), (41.992, 32.345), (41.992, 31.985)), ((41.992, 31.953), (42, 31.921), (42, 31.889)), ((42, 31.888), (42, 31.888), (42, 31.887)), ((42, 31.184), (40.499, 31.245), (40, 31)))
        self.add_bezier('e14', (23, 25), ((23.524, 25.074), (24.485, 25.262), (25, 25)))
        self.add_bezier('e15', (41, 17), ((41.196, 16.828), (42, 16.055), (42, 15.802)), ((42, 15.581), (41.172, 15.155), (41, 15)))
        self.add_bezier('e16', (25, 6), ((24.779, 6), (24.385, 6), (24.164, 6)), ((24.025, 6), (23.877, 6), (23.73, 6)), ((23.697, 6), (23.656, 6), (23.624, 6)), ((23.476, 6), (23.147, 6), (23, 6)))
        self.add_bezier('e17', (7, 15), ((6.91, 15.074), (6, 15.614), (6, 15.655)), ((6, 15.99), (6.787, 16.779), (7, 17)))
        self.add_contour('c0', 'e8', 'e0', 'e9', 'e1', 'e10')
        self.add_contour('c1', 'e11', 'e2', 'e12', 'e3', 'e13')
        self.add_contour('c2', 'e4', 'e14', 'e5', 'e15', 'e6', 'e16', 'e7', 'e17', closed=True)
