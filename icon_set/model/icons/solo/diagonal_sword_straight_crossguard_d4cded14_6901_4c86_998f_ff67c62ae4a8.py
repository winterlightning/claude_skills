"""A diagonal sword with pointed blade, straight crossguard and short grip. SQUARE fits the rising diagonal and pommel extremes. Blade is symmetric around y48-x; guard and grip share an exact center node. Source supplies broad blade; Lucide sword informs a single-stroke guard and grip. Inner ridge and thick guard outline omitted to preserve clearance."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = 'd4cded14-6901-4c86-998f-ff67c62ae4a8'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_26/magic sword_d4cded14-6901-4c86-998f-ff67c62ae4a8.svg'
AUTHOR = "gpt-6-astra"

class Drawing(Solo48):
    icon_id = 'diagonal-sword-straight-crossguard'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ('Diagonal Sword with Straight Crossguard',)
    keywords = ('diagonal', 'sword', 'straight', 'crossguard')
    def build(self):
        self.add_polyline('blade',(16,24),(34,6),(42,6),(42,14),(24,32))
        nodes = [(10,18),(16,24),(20,28),(24,32),(30,38)]
        for i in range(4):
            self.add_line('guard-'+str(i),nodes[i],nodes[i+1])
        self.add_contour('guard',*[f'guard-{i}' for i in range(4)])
        self.add_line('grip',(20,28),(8,40))
        self.add_polyline('pommel',(6,38),(8,40),(10,42))
        self.relate('connect','blade','guard')
        self.relate('connect','grip','guard')
        self.relate('connect','grip','pommel')
