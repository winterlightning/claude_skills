'Two winding riverbanks run from upper left toward lower right with two detached stones on the near bank. SQUARE extremes (6,6)-(42,42) spread the landscape. No useful local Lucide river or wave match was found. The banks are separate coherent cubic runs; asymmetry follows the river. Two stones share a circular definition. The third stone and irregular stone outlines were omitted to retain four units of ink clearance.'
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = 'b49c8cb8-5668-460b-a654-dc45fa10b497'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_33/riverbed_b49c8cb8-5668-460b-a654-dc45fa10b497.svg'
AUTHOR = 'gpt-6-astra'
class Drawing(Solo48):
    icon_id = 'winding-riverbed-with-stones'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'Uncategorized'
    aliases = ['Winding River with Stones']
    keywords = ['winding', 'riverbed', 'with', 'stones']
    def build(self):
        self.add_bezier('far-bank',(6,6),((18,6),(30,6),(30,12)),((30,16),(26,16),(26,20)),((26,24),(34,20),(42,24)))
        self.add_bezier('near-bank',(6,16),((12,16),(16,15),(16,20)),((16,24),(10,24),(12,28)),((15,33),(25,27),(28,42)))
        for n,(x,y,r) in enumerate([(10,40,2),(40,36,2)]):
            self.add_arc(f'stone-{n}-a',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(f'stone-{n}-b',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(f'stone-{n}',f'stone-{n}-a',f'stone-{n}-b',closed=True)
