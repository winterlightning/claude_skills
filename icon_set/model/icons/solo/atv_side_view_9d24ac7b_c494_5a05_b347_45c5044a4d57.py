"""A quad bike with a dipped saddle, rising handlebar and two large wheels. Broad envelope retains the open riding position. Lucide car informed the wheel joins; hubs omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9d24ac7b-c494-5a05-b347-45c5044a4d57'
SOURCE_PATH = 'pictographic-primitives/transportation/car_9d24ac7b-c494-5a05-b347-45c5044a4d57.svg'
SOURCE_REFERENCES = (('9d24ac7b-c494-5a05-b347-45c5044a4d57', 'pictographic-primitives/transportation/car_9d24ac7b-c494-5a05-b347-45c5044a4d57.svg'),)
AUTHOR = 'gpt-6'

class AtvSideView(Solo48):
    icon_id = 'atv-side-view'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('atv', 'quad', 'quad bike', 'off-road', 'vehicle', 'four wheeler', 'offroad', 'side view')

    def build(self) -> None:
        self.add_line('back',(4,33),(4,20))
        self.add_line('seat-a',(4,20),(12,20))
        self.add_line('seat-b',(12,20),(16,24))
        self.add_line('seat-c',(16,24),(24,24))
        self.add_line('seat-d',(24,24),(28,20))
        self.add_line('hood',(28,20),(38,20))
        self.add_arc('nose',(38,20),(44,26),radius_x=6)
        self.add_line('front',(44,26),(44,33))
        self.add_contour('body','back','seat-a','seat-b','seat-c','seat-d','hood','nose','front')
        self.add_line('handlebar',(28,20),(24,8))
        self.relate('connect','handlebar','body')

        for name,x in [('rear',11),('front',37)]:
            self.add_arc(name+'-a',(x-7,33),(x+7,33),radius_x=7)
            self.add_arc(name+'-b',(x+7,33),(x-7,33),radius_x=7)
            self.add_contour(name+'-wheel',name+'-a',name+'-b',closed=True)
        self.add_line('chassis',(18,33),(30,33))
        for name in ['rear-wheel','front-wheel']:
            self.relate('connect','body',name)
            self.relate('connect','chassis',name)
