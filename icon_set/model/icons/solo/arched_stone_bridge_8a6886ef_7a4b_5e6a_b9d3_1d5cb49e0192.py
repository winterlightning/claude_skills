'Stone bridge: two equal tiers of arches share real vertical piers above a smooth water line; omit the cramped middle deck rule.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8a6886ef-7a4b-5e6a-b9d3-1d5cb49e0192'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-06/bridge_8a6886ef-7a4b-5e6a-b9d3-1d5cb49e0192.svg'
AUTHOR = 'gpt-6'


class ArchedStoneBridge(Solo48):
    icon_id = 'arched-stone-bridge'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('bridge', 'arch', 'viaduct', 'river', 'water', 'crossing', 'stone', 'landmark', 'infrastructure')

    def build(self) -> None:
        self.add_polyline('deck',(6,6),(24,6),(42,6))
        for i,x in enumerate((6,24,42)):
            self.add_polyline(f'pier-{i}',(x,6),(x,22),(x,38),(x,42))
            self.relate('connect','deck',f'pier-{i}')
        for row,y in enumerate((22,38)):
            for col,x in enumerate((6,24)):
                name=f'arch-{row}-{col}'
                self.add_arc(name,(x,y),(x+18,y),radius_x=9,radius_y=7)
                self.relate('connect',name,f'pier-{col}');self.relate('connect',name,f'pier-{col+1}')
            self.relate('connect',f'arch-{row}-0',f'arch-{row}-1')
        self.add_bezier('water',(6,42),((12,42),(12,40),(15,40)),((18,40),(18,42),(24,42)),((30,42),(30,40),(33,40)),((36,40),(36,42),(42,42)))
        for i in range(3):self.relate('connect','water',f'pier-{i}')
