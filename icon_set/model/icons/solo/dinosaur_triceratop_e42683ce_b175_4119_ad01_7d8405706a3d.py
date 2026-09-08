"""Standing left-facing triceratops with heavy body, brow horn and tail. Centerlines (2,8)-(46,40). Two visible legs; omit ground and hidden legs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e42683ce-b175-4119-ad01-7d8405706a3d'
SOURCE_PATH = 'pictographic-primitives/animals/dinosaur triceratop_e42683ce-b175-4119-ad01-7d8405706a3d.svg'
AUTHOR = 'gpt-6'


class StandingTriceratops(Solo48):
    icon_id = 'standing-triceratops'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals/prehistoric'
    aliases = ()
    keywords = ('triceratops', 'dinosaur', 'standing', 'horns', 'prehistoric', 'jurassic', 'reptile', 'extinct')

    def build(self) -> None:
        self.add_polyline('front',(2,29),(2,20),(8,20),(8,8),(16,20))
        self.add_arc('back',(16,20),(28,14),radius_x=15)
        self.add_arc('rump',(28,14),(40,24),radius_x=17)
        self.add_polyline('tail-legs',(40,24),(46,30),(37,32),(37,40),(29,40),(29,31),(20,31),(20,40),(12,40),(12,35))
        self.add_arc('chest',(12,35),(6,29),radius_x=6,sweep=False)
        self.add_line('muzzle',(6,29),(2,29))
        self.add_contour('body-top','back','rump')
        self.add_contour('chest-front','chest','muzzle')
        self.relate('connect','front','body-top')
        self.relate('connect','body-top','tail-legs')
        self.relate('connect','tail-legs','chest-front')
        self.relate('connect','chest-front','front')
