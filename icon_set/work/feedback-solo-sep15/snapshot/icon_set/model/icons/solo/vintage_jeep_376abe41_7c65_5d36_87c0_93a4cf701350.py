"""A boxy right-facing off-road car with two tall windows and round wheels. Broad envelope retains its short bonnet. Lucide car informed joined geometry; outer fenders merge into wheel arches and hubs are omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '376abe41-7c65-5d36-87c0-93a4cf701350'
SOURCE_PATH = 'pictographic-primitives/transportation/car_376abe41-7c65-5d36-87c0-93a4cf701350.svg'
SOURCE_REFERENCES = (('376abe41-7c65-5d36-87c0-93a4cf701350', 'pictographic-primitives/transportation/car_376abe41-7c65-5d36-87c0-93a4cf701350.svg'),)
AUTHOR = 'gpt-6'

class VintageJeep(Solo48):
    icon_id = 'vintage-jeep'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('jeep', 'vintage', 'off-road', '4x4', 'car', 'classic', 'vehicle', 'side view')

    def build(self) -> None:
        self.add_line('back',(4,33),(4,20))
        self.add_line('top-0',(4,20),(16,20))
        self.add_line('top-1',(16,20),(28,20))
        self.add_line('top-2',(28,20),(34,20))
        self.add_arc('nose',(34,20),(44,30),radius_x=10)
        self.add_line('front',(44,30),(44,33))
        self.add_contour('body','back','top-0','top-1','top-2','nose','front')

        for name,x in [('rear',11),('front',37)]:
            self.add_arc(name+'-a',(x-7,33),(x+7,33),radius_x=7)
            self.add_arc(name+'-b',(x+7,33),(x-7,33),radius_x=7)
            self.add_contour(name+'-wheel',name+'-a',name+'-b',closed=True)
        self.add_line('chassis',(18,33),(30,33))
        for name in ['rear-wheel','front-wheel']:
            self.relate('connect','body',name)
            self.relate('connect','chassis',name)

        self.add_polyline('cabin',(4,20),(4,8),(16,8),(28,8),(28,20))
        self.add_line('pillar',(16,8),(16,20))
        for a,b in [('cabin','body'),('pillar','cabin'),('pillar','body')]:self.relate('connect',a,b)
