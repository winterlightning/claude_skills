"""Battery: A wide battery body forms a rounded rectangular outline with an empty interior. A smaller rounded terminal projects from the middle of its right edge and joins the body.

Construction: A blank rounded battery body has the original attached outlined right terminal.
Keyshape: HRECT_M; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'd59453b3-a555-48ec-9434-865bcda7a62f'
SOURCE_PATH = 'pictographic-primitives/state/battery 1_d59453b3-a555-48ec-9434-865bcda7a62f.svg'
AUTHOR = 'gpt-6'


class BatterySubState26(Sub32):
    icon_id = 'battery-sub-state-26'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives/shape'
    aliases = ()
    keywords = ('battery', 'wide', 'body', 'forms', 'rounded', 'rectangular', 'outline', 'empty')

    def build(self):
        def rounded(name,x0,y0,x1,y1,r):
            pts=[(x0+r,y0),(x1-r,y0),(x1,y0+r),(x1,y1-r),(x1-r,y1),(x0+r,y1),(x0,y1-r),(x0,y0+r)]
            for i in range(8):
                a,b=pts[i],pts[(i+1)%8]
                if i%2:self.add_arc(name+str(i),a,b,radius_x=r)
                else:self.add_line(name+str(i),a,b)
            self.add_contour(name,*(name+str(i) for i in range(8)),closed=True)
        rounded('body',2,8,22,24,2)
        self.add_line('terminal-top',(22,12),(28,12))
        self.add_arc('terminal-upper',(28,12),(30,14),radius_x=2)
        self.add_line('terminal-right',(30,14),(30,18))
        self.add_arc('terminal-lower',(30,18),(28,20),radius_x=2)
        self.add_line('terminal-bottom',(28,20),(22,20))
        self.add_contour('terminal','terminal-top','terminal-upper','terminal-right','terminal-lower','terminal-bottom')
        self.relate('connect','body','terminal')
