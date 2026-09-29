"""Centered player under a symmetric headphone arch. Round speaker reduced to a filled control dot; earcups reduced to thick end strokes. Omit top and bottom bands. Extremes (6,6)-(42,42). Lucide headphones and smartphone."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='32ab4ed8-b548-4a61-956b-a99332d1684d'
SOURCE_PATH='pictographic-primitives/music/walkman headphones_32ab4ed8-b548-4a61-956b-a99332d1684d.svg'
AUTHOR='gpt-6'

class HeadphonesWithPortablePlayer(Solo48):
    icon_id='headphones-with-portable-player'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "music"
    categories = ("primitives", "music")
    aliases=()
    keywords=('walkman', 'headphones', 'portable', 'player', 'audio', 'listening', 'music')

    def build(self):
        axis=24
        self.add_arc('headband',(6,24),(42,24),radius_x=18)
        for name,x in (('left',6),('right',42)):
            self.add_line(f'{name}-earcup',(x,24),(x,34))
            self.relate('connect',f'{name}-earcup','headband')
        top=[(18, 18), (30, 18)]
        bottom=[(30, 42), (18, 42)]
        parts=[]
        for n,(a,b) in enumerate(zip(top,top[1:])):
            self.add_line(f'case-top-{n}',a,b);parts.append(f'case-top-{n}')
        self.add_arc('case-tr',(30,18),(33,21),radius_x=3)
        self.add_line('case-right',(33,21),(33,39))
        self.add_arc('case-br',(33,39),(30,42),radius_x=3)
        parts+=['case-tr','case-right','case-br']
        for n,(a,b) in enumerate(zip(bottom,bottom[1:])):
            self.add_line(f'case-bottom-{n}',a,b);parts.append(f'case-bottom-{n}')
        self.add_arc('case-bl',(18,42),(15,39),radius_x=3)
        self.add_line('case-left',(15,39),(15,21))
        self.add_arc('case-tl',(15,21),(18,18),radius_x=3)
        parts+=['case-bl','case-left','case-tl']
        self.add_contour('case',*parts,closed=True)
        self.add_dot('speaker',(24,30))
