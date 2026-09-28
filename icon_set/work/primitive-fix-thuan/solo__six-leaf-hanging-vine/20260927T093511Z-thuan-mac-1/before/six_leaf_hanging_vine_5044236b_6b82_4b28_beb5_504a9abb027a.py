'Six-leaf vine: six alternating curved leaves with clear counters and a shared stem, preserving the alternating rhythm.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5044236b-6b82-4b28-beb5-504a9abb027a'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-02/hanging plant 4_5044236b-6b82-4b28-beb5-504a9abb027a.svg'
AUTHOR = 'gpt-6'

class SixLeafHangingVine(Solo48):
    icon_id = 'six-leaf-hanging-vine'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "decoration"
    categories = ("primitives", "decoration")
    aliases = ()
    keywords = ('vine', 'hanging', 'leaves', 'stem', 'foliage', 'plant', 'botanical')

    def build(self) -> None:
        self.add_polyline('stem',(24,8),(24,24),(24,40))
        for j,y in enumerate((8,24,40)):
         for side in (-1,1):
          left,right=(8,24) if side==-1 else (24,40)
          name=f'leaf-{j}-{side}'
          self.add_arc(name+'-top',(left,y),(right,y),radius_x=8,radius_y=4)
          self.add_arc(name+'-bottom',(right,y),(left,y),radius_x=8,radius_y=4)
          self.add_contour(name,name+'-top',name+'-bottom',closed=True)
          self.relate('connect',name,'stem')
         self.relate('connect',f'leaf-{j}--1',f'leaf-{j}-1')
