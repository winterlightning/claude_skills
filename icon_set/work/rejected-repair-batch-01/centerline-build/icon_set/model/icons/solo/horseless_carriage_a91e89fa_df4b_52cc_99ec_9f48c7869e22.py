"""An early motor car with a rear canopy, open seat and upright steering post. Square envelope makes room for the tall canopy. Lucide car informed wheel joins; decorative fenders and hubs omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a91e89fa-df4b-52cc-99ec-9f48c7869e22'
SOURCE_PATH = 'pictographic-primitives/transportation/car_a91e89fa-df4b-52cc-99ec-9f48c7869e22.svg'
SOURCE_REFERENCES = (('a91e89fa-df4b-52cc-99ec-9f48c7869e22', 'pictographic-primitives/transportation/car_a91e89fa-df4b-52cc-99ec-9f48c7869e22.svg'),)
AUTHOR = 'gpt-6'

class HorselessCarriage(Solo48):
    icon_id = 'horseless-carriage'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('vintage car', 'antique', 'horseless carriage', 'classic', 'old car', 'car', 'vehicle', 'history')

    def build(self) -> None:
        self.add_line('back',(6,36),(6,22))
        self.add_line('top-a',(6,22),(16,22))
        self.add_line('top-b',(16,22),(26,22))
        self.add_line('top-c',(26,22),(38,22))
        self.add_arc('nose',(38,22),(42,26),radius_x=4)
        self.add_line('front',(42,26),(42,36))
        self.add_contour('body','back','top-a','top-b','top-c','nose','front')

        for name,x in [('rear',12),('front',36)]:
            self.add_arc(name+'-a',(x-6,36),(x+6,36),radius_x=6)
            self.add_arc(name+'-b',(x+6,36),(x-6,36),radius_x=6)
            self.add_contour(name+'-wheel',name+'-a',name+'-b',closed=True)
        self.add_line('chassis',(18,36),(30,36))
        for name in ['rear-wheel','front-wheel']:
            self.relate('connect','body',name)
            self.relate('connect','chassis',name)

        self.add_polyline('canopy',(6,22),(6,14),(6,6),(26,6))
        self.add_polyline('seat',(6,14),(16,14),(16,22))
        self.add_line('steering-post',(26,22),(26,14))
        for a,b in [('canopy','body'),('seat','canopy'),('seat','body'),('steering-post','body')]:self.relate('connect',a,b)
