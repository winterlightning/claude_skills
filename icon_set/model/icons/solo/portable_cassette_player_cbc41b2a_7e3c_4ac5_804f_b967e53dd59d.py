"""Wide portable player with a cassette protruding from its upper slot. Retain one control line and a circular reel mark; omit the slanted window outline and second slot lip. Extremes (4,8)-(44,40). Lucide cassette-tape body."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='cbc41b2a-7e3c-4ac5-804f-b967e53dd59d'
SOURCE_PATH='pictographic-primitives/music/walkman_cbc41b2a-7e3c-4ac5-804f-b967e53dd59d.svg'
AUTHOR='gpt-6'

class PortableCassettePlayer(Solo48):
    icon_id='portable-cassette-player'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "music"
    aliases=()
    keywords=('walkman', 'cassette', 'player', 'portable', 'retro', 'tape', 'audio', 'music')

    def build(self):
        top=[(8, 16), (20, 16), (38, 16), (40, 16)]
        bottom=[(40, 40), (8, 40)]
        parts=[]
        for n,(a,b) in enumerate(zip(top,top[1:])):
            self.add_line(f'case-top-{n}',a,b);parts.append(f'case-top-{n}')
        self.add_arc('case-tr',(40,16),(44,20),radius_x=4)
        self.add_line('case-right',(44,20),(44,36))
        self.add_arc('case-br',(44,36),(40,40),radius_x=4)
        parts+=['case-tr','case-right','case-br']
        for n,(a,b) in enumerate(zip(bottom,bottom[1:])):
            self.add_line(f'case-bottom-{n}',a,b);parts.append(f'case-bottom-{n}')
        self.add_arc('case-bl',(8,40),(4,36),radius_x=4)
        self.add_line('case-left',(4,36),(4,20))
        self.add_arc('case-tl',(4,20),(8,16),radius_x=4)
        parts+=['case-bl','case-left','case-tl']
        self.add_contour('case',*parts,closed=True)
        self.add_polyline('inserted-cassette',(20,16),(20,8),(38,8),(38,16))
        self.relate('connect','case','inserted-cassette')
        self.add_line('control',(14,28),(18,28))
        cx,cy,rx,ry=32,28,2,2
        points=((cx-rx,cy),(cx,cy-ry),(cx+rx,cy),(cx,cy+ry))
        for n in range(4):
            self.add_arc(f'reel-{n}',points[n],points[(n+1)%4],radius_x=rx,radius_y=ry)
        self.add_contour('reel',*[f'reel-{n}' for n in range(4)],closed=True)
