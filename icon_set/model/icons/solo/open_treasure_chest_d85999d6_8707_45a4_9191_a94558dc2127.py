"""Open treasure chest with a domed treasure mound and central latch. HRECT_L extremes (4,8)-(44,40) favor its broad front. Drop radiating glints for breathing room. Rounded case construction follows Lucide box; mound remains naturally attached."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='d85999d6-8707-45a4-9191-a94558dc2127'
SOURCE_PATH='pictographic-primitives/money/treasure chest open_d85999d6-8707-45a4-9191-a94558dc2127.svg'
AUTHOR='gpt-6'

class OpenTreasureChest(Solo48):
    icon_id='open-treasure-chest'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "money"
    categories = ("primitives", "money")
    aliases=()
    keywords=('treasure', 'chest', 'open', 'latch', 'wealth', 'container')

    def build(self):
        top=[(8, 22), (10, 22), (24, 22), (38, 22), (40, 22)]
        bottom=[(40, 40), (8, 40)]
        parts=[]
        for n,(a,b) in enumerate(zip(top,top[1:])):
            self.add_line(f'case-top-{n}',a,b);parts.append(f'case-top-{n}')
        self.add_arc('case-tr',(40,22),(44,26),radius_x=4)
        self.add_line('case-right',(44,26),(44,36))
        self.add_arc('case-br',(44,36),(40,40),radius_x=4)
        parts+=['case-tr','case-right','case-br']
        for n,(a,b) in enumerate(zip(bottom,bottom[1:])):
            self.add_line(f'case-bottom-{n}',a,b);parts.append(f'case-bottom-{n}')
        self.add_arc('case-bl',(8,40),(4,36),radius_x=4)
        self.add_line('case-left',(4,36),(4,26))
        self.add_arc('case-tl',(4,26),(8,22),radius_x=4)
        parts+=['case-bl','case-left','case-tl']
        self.add_contour('case',*parts,closed=True)
        self.add_arc('treasure',(10,22),(38,22),radius_x=14)
        self.relate('connect','case','treasure')
        self.add_line('latch',(24,22),(24,30))
        self.relate('connect','case','latch')
