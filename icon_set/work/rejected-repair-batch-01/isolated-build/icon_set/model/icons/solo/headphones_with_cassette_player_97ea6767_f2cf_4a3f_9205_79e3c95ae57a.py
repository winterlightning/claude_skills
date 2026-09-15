"""Centered rectangular cassette player with raised top tab under a mirrored headband. Omit the narrow clip line; earcups become thick end strokes. Extremes (6,6)-(42,42). Lucide headphones and smartphone."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='97ea6767-f2cf-4a3f-9205-79e3c95ae57a'
SOURCE_PATH='pictographic-primitives/music/walkman heaphones_97ea6767-f2cf-4a3f-9205-79e3c95ae57a.svg'
AUTHOR='gpt-6'

class HeadphonesWithCassettePlayer(Solo48):
    icon_id='headphones-with-cassette-player'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/music"
    aliases=()
    keywords=('walkman', 'headphones', 'cassette', 'portable', 'player', 'retro', 'music')

    def build(self):
        axis=24
        self.add_arc('headband',(6,24),(42,24),radius_x=18)
        for name,x in (('left',6),('right',42)):
            self.add_line(f'{name}-earcup',(x,24),(x,34))
            self.relate('connect',f'{name}-earcup','headband')
        top=[(18, 23), (20, 23), (28, 23), (30, 23)]
        bottom=[(30, 42), (18, 42)]
        parts=[]
        for n,(a,b) in enumerate(zip(top,top[1:])):
            self.add_line(f'case-top-{n}',a,b);parts.append(f'case-top-{n}')
        self.add_arc('case-tr',(30,23),(33,26),radius_x=3)
        self.add_line('case-right',(33,26),(33,39))
        self.add_arc('case-br',(33,39),(30,42),radius_x=3)
        parts+=['case-tr','case-right','case-br']
        for n,(a,b) in enumerate(zip(bottom,bottom[1:])):
            self.add_line(f'case-bottom-{n}',a,b);parts.append(f'case-bottom-{n}')
        self.add_arc('case-bl',(18,42),(15,39),radius_x=3)
        self.add_line('case-left',(15,39),(15,26))
        self.add_arc('case-tl',(15,26),(18,23),radius_x=3)
        parts+=['case-bl','case-left','case-tl']
        self.add_contour('case',*parts,closed=True)
        self.add_polyline('cassette-tab',(20,23),(20,15),(28,15),(28,23))
        self.relate('connect','case','cassette-tab')
