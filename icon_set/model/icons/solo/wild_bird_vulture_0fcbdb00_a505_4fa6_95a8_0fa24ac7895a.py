"""vulture: source silhouette re-authored on SOLO48.

Lucide bird informs coherent body arcs and sparse detail.
Keyshape VRECT_L; extremes obtained from the SOLO48 contract.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0fcbdb00-a505-4fa6-95a8-0fa24ac7895a'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird vulture_0fcbdb00-a505-4fa6-95a8-0fa24ac7895a.svg'
AUTHOR = 'gpt-6'


class Vulture(Solo48):
    icon_id = 'vulture'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/birds"
    aliases = ()
    keywords = ('vulture', 'scavenger', 'bird', 'neck', 'beak', 'standing', 'carrion', 'wildlife')

    def build(self) -> None:
        self.add_arc('head', (26, 9), (40, 9), radius_x=7, radius_y=7, sweep=True)
        self.add_line('beak', (40, 9), (40, 15))
        self.add_line('chin', (40, 15), (32, 15))
        self.add_line('neck', (32, 15), (32, 21))
        self.add_arc('throat', (32, 21), (25, 28), radius_x=7, radius_y=7, sweep=True)
        self.add_arc('shoulder', (25, 28), (18, 16), radius_x=10, radius_y=10, sweep=False)
        self.add_arc('wing-back', (18, 16), (8, 40), radius_x=40, radius_y=40, sweep=False)
        self.add_line('wing-tip', (8, 40), (23, 34))
        self.add_arc('wing-front', (23, 34), (25, 28), radius_x=10, radius_y=10, sweep=False)
        self.add_contour('wing', 'shoulder', 'wing-back', 'wing-tip', 'wing-front', closed=True)
        self.add_line('nape', (26, 9), (26, 17))
        self.add_contour('neck-head', 'nape', closed=False)
        self.add_contour('head-neck', 'head', 'beak', 'chin', 'neck', 'throat', closed=False)
        self.relate("connect", 'head-neck', 'wing')
        self.add_line('foot-leg', (23, 34), (26, 46))
        self.add_line('foot', (26, 46), (34, 46))
        self.add_contour('leg', 'foot-leg', 'foot', closed=False)
        self.relate("connect", 'wing', 'leg')
