from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '145df94c-38fe-4a63-b878-f9b0d6c352db'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__potty-with-steam/20260927T170540Z-thuan-mac-1/reference/poo poop station waste_145df94c-38fe-4a63-b878-f9b0d6c352db.svg'
AUTHOR = 'gpt-6'

class PottyWithSteam(Solo48):
    icon_id = 'potty-with-steam'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "babies"
    categories = ("babies", "primitives")
    aliases = ()
    keywords = ('potty', 'toilet', 'poop', 'steam', 'smell', 'training', 'baby', 'bathroom')

    # Designed to centerline extremes (6, 6)–(42, 42).
    def build(self):
        # Rounded seat over a concave base with two rising steam curls.
        self.add_line('left',(6,24),(6,42))
        self.add_bezier('base',(6,42),((14,40),(34,40),(42,42)))
        self.add_line('right',(42,42),(42,24))
        self.add_contour('potty','left','base','right')
        self.add_arc('seat',(6,24),(42,24),radius_x=18,radius_y=8,sweep=False)
        self.relate('connect','potty','seat')
        for x in (14,34):
            self.add_arc(f'steam-top-{x}',(x,6),(x,12),radius_x=4,radius_y=3)
            self.add_arc(f'steam-low-{x}',(x,12),(x,18),radius_x=4,radius_y=3,sweep=False)
            self.add_contour(f'steam-{x}',f'steam-top-{x}',f'steam-low-{x}')
