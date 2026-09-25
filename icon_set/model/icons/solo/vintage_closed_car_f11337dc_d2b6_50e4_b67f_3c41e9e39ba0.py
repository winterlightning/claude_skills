"""A tall vintage car with two rear windows and a long lower bonnet. Square envelope preserves its upright cabin. Lucide car informed body/wheel construction; fenders merge with wheel arches and hubs are omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f11337dc-d2b6-50e4-b67f-3c41e9e39ba0'
SOURCE_PATH = 'pictographic-primitives/transportation/car_f11337dc-d2b6-50e4-b67f-3c41e9e39ba0.svg'
SOURCE_REFERENCES = (('f11337dc-d2b6-50e4-b67f-3c41e9e39ba0', 'pictographic-primitives/transportation/car_f11337dc-d2b6-50e4-b67f-3c41e9e39ba0.svg'),)
AUTHOR = 'gpt-6'

class VintageClosedCar(Solo48):
    icon_id = 'vintage-closed-car'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('vintage car', 'classic', 'antique', 'old car', 'car', 'retro', 'vehicle', 'side view')

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

        self.add_polyline('cabin',(6,22),(6,6),(16,6),(26,6),(26,22))
        self.add_line('pillar',(16,6),(16,22))
        for a,b in [('cabin','body'),('pillar','cabin'),('pillar','body')]:self.relate('connect',a,b)
