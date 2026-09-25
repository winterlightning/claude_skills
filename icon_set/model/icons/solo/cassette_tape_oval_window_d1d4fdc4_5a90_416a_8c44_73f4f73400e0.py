"""Wide rounded cassette body enclosing an oval window and the two angled corners of its lower guide. Omit inner reel marks and the upper guide edge to preserve clear space. Extremes (4,8)-(44,40). Lucide cassette-tape construction."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='d1d4fdc4-5a90-416a-8c44-73f4f73400e0'
SOURCE_PATH='pictographic-primitives/music/walkman cassette_d1d4fdc4-5a90-416a-8c44-73f4f73400e0.svg'
AUTHOR='gpt-6'

class CassetteTapeOvalWindow(Solo48):
    icon_id='cassette-tape-oval-window'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "music"
    categories = ("primitives", "music")
    aliases=()
    keywords=('cassette', 'tape', 'mixtape', 'audio', 'retro', 'walkman', 'music')

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
        self.add_line('window-top',(19,17),(29,17))
        self.add_arc('window-right',(29,17),(29,25),radius_x=4)
        self.add_line('window-bottom',(29,25),(19,25))
        self.add_arc('window-left',(19,25),(19,17),radius_x=4)
        self.add_contour('window','window-top','window-right','window-bottom','window-left',closed=True)
        for name,start,end in (('left',(12,40),(16,34)),('right',(36,40),(32,34))):
            self.add_line(f'guide-{name}',start,end)
            self.relate('connect','case',f'guide-{name}')
