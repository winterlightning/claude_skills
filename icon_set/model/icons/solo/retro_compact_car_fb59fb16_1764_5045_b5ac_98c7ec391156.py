"""A compact car with a domed two-window cabin and circular wheels. Lucide bus and car-front informed shared cabin/body joins. Broad keyshape preserves the right-facing silhouette; tiny hubs omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fb59fb16-1764-5045-b5ac-98c7ec391156'
SOURCE_PATH = 'pictographic-primitives/transportation/car retro_fb59fb16-1764-5045-b5ac-98c7ec391156.svg'
SOURCE_REFERENCES = (('fb59fb16-1764-5045-b5ac-98c7ec391156', 'pictographic-primitives/transportation/car retro_fb59fb16-1764-5045-b5ac-98c7ec391156.svg'),)
AUTHOR = 'gpt-6'

class RetroCompactCar(Solo48):
    icon_id = 'retro-compact-car'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('car', 'retro', 'compact', 'beetle', 'vintage', 'vehicle', 'side view', 'automobile')

    def build(self) -> None:
        self.add_line('back',(4,33),(4,24))
        self.add_arc('back-corner',(4,24),(8,20),radius_x=4)
        self.add_line('top-0',(8,20),(10,20))
        self.add_line('top-1',(10,20),(22,20))
        self.add_line('top-2',(22,20),(34,20))
        self.add_arc('nose',(34,20),(44,30),radius_x=10)
        self.add_line('front',(44,30),(44,33))
        self.add_contour('body','back','back-corner','top-0','top-1','top-2','nose','front')

        for side,x in [('rear',11),('front',37)]:
            self.add_arc(side+'-upper',(x-7,33),(x+7,33),radius_x=7)
            self.add_arc(side+'-lower',(x+7,33),(x-7,33),radius_x=7)
            self.add_contour(side+'-wheel',side+'-upper',side+'-lower',closed=True)
        self.add_line('chassis',(18,33),(30,33))
        for wheel in ['rear-wheel','front-wheel']:
            self.relate('connect','body',wheel)
            self.relate('connect','chassis',wheel)

        self.add_arc('cabin-a',(10,20),(22,8),radius_x=12)
        self.add_arc('cabin-b',(22,8),(34,20),radius_x=12)
        self.add_contour('cabin','cabin-a','cabin-b')
        self.add_line('pillar',(22,8),(22,20))
        for a,b in [('cabin','body'),('pillar','cabin'),('pillar','body')]:
            self.relate('connect',a,b)
