"""An open circular speed dial with three ticks and an upper-right needle. Lucide gauge informed the open rim; minor ticks omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '527246fa-c534-5d3c-a36c-8140f069ee20'
SOURCE_PATH = 'pictographic-primitives/transportation/car dashboard speed_527246fa-c534-5d3c-a36c-8140f069ee20.svg'
SOURCE_REFERENCES = (('527246fa-c534-5d3c-a36c-8140f069ee20', 'pictographic-primitives/transportation/car dashboard speed_527246fa-c534-5d3c-a36c-8140f069ee20.svg'),)
AUTHOR = 'gpt-6'

class Speedometer(Solo48):
    icon_id = 'speedometer'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('speedometer', 'speed', 'gauge', 'dashboard', 'dial', 'car', 'meter', 'performance')

    def build(self) -> None:
        points=[(12,40),(4,24),(12,8),(24,4),(44,24),(36,40)]
        for i,(a,b) in enumerate(zip(points,points[1:])):
            self.add_arc(f'rim-{i}',a,b,radius_x=20)
        self.add_contour('rim',*[f'rim-{i}' for i in range(5)])
        for i,(a,b) in enumerate([((4,24),(10,24)),((12,8),(16,13)),((24,4),(24,10))]):
            self.add_line(f'tick-{i}',a,b)
            self.relate('connect',f'tick-{i}','rim')
        self.add_arc('hub-a',(26,25),(22,25),radius_x=2)
        self.add_arc('hub-b',(22,25),(26,25),radius_x=2)
        self.add_contour('hub','hub-a','hub-b',closed=True)
        self.add_line('needle',(26,25),(32,17))
        self.relate('connect','needle','hub')
