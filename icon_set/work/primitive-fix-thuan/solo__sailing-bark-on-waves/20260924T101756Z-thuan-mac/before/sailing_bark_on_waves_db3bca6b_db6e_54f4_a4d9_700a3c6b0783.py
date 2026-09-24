"""A bark with a bellied square sail, open hull and water wave. SQUARE ink (6,6)-(42,42). Lucide sailboat informs the mast attachment; open hull replaces the crowded double edge."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'db3bca6b-db6e-54f4-a4d9-700a3c6b0783'
SOURCE_PATH = 'pictographic-primitives/transportation/bark_db3bca6b-db6e-54f4-a4d9-700a3c6b0783.svg'
AUTHOR = 'gpt-6'

class SailingBarkOnWaves(Solo48):
    icon_id = 'sailing-bark-on-waves'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('ship', 'bark', 'sail', 'sailing', 'boat', 'nautical', 'waves', 'sea')

    def build(self) -> None:
        self.add_arc('sail-left',(16,6),(16,22),radius_x=18,sweep=True)
        self.add_line('sail-bottom',(16,22),(23,22))
        self.add_line('sail-bottom-right',(23,22),(30,22))
        self.add_arc('sail-belly',(30,22),(30,6),radius_x=8,sweep=False)
        self.add_line('sail-top',(30,6),(16,6))
        self.add_contour('sail','sail-left','sail-bottom','sail-bottom-right','sail-belly','sail-top',closed=True)
        self.add_line('mast',(23,22),(23,31))
        self.add_polyline('hull',(6,28),(12,31),(23,31),(36,31),(42,28))
        self.relate('connect','mast','sail')
        self.relate('connect','mast','hull')
        self.add_arc('wave-left',(6,41),(24,41),radius_x=15,radius_y=5)
        self.add_arc('wave-right',(24,41),(42,41),radius_x=15,radius_y=5,sweep=False)
        self.add_contour('wave','wave-left','wave-right')
