"""Wide cassette with two equal round reels connected by one tape bar and a lower trapezoid. Omit the doubled tape band. Extremes (4,8)-(44,40). Lucide cassette-tape loop and guide construction."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='ffecaf0c-db12-435d-80a9-a4632f25a635'
SOURCE_PATH='pictographic-primitives/music/walkman cassette_ffecaf0c-db12-435d-80a9-a4632f25a635.svg'
AUTHOR='gpt-6'

class CassetteTapeRoundReels(Solo48):
    icon_id='cassette-tape-round-reels'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "music"
    categories = ("primitives", "music")
    aliases=()
    keywords=('cassette', 'tape', 'reels', 'audio', 'retro', 'walkman', 'music')

    def build(self):
        top=[(8, 8), (40, 8)]
        bottom=[(40, 40), (36, 40), (12, 40), (8, 40)]
        parts=[]
        for n,(a,b) in enumerate(zip(top,top[1:])):
            self.add_line(f'case-top-{n}',a,b);parts.append(f'case-top-{n}')
        self.add_arc('case-tr',(40,8),(44,12),radius_x=4)
        self.add_line('case-right',(44,12),(44,36))
        self.add_arc('case-br',(44,36),(40,40),radius_x=4)
        parts+=['case-tr','case-right','case-br']
        for n,(a,b) in enumerate(zip(bottom,bottom[1:])):
            self.add_line(f'case-bottom-{n}',a,b);parts.append(f'case-bottom-{n}')
        self.add_arc('case-bl',(8,40),(4,36),radius_x=4)
        self.add_line('case-left',(4,36),(4,12))
        self.add_arc('case-tl',(4,12),(8,8),radius_x=4)
        parts+=['case-bl','case-left','case-tl']
        self.add_contour('case',*parts,closed=True)
        for name,cx in (('left',16),('right',32)):
            cy,r=20,3
            points=((cx-r,cy),(cx,cy-r),(cx+r,cy),(cx,cy+r))
            for n in range(4):self.add_arc(f'{name}-{n}',points[n],points[(n+1)%4],radius_x=r)
            self.add_contour(name,*[f'{name}-{n}' for n in range(4)],closed=True)
        self.add_line('tape',(19,20),(29,20))
        self.relate('connect','tape','left')
        self.relate('connect','tape','right')
        self.add_polyline('guide',(12,40),(16,32),(32,32),(36,40))
        self.relate('connect','case','guide')
