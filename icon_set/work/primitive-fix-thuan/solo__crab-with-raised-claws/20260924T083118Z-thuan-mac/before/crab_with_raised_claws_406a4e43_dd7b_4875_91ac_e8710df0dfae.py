"""Crab with Large Open Pincers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '406a4e43-dd7b-4875-91ac-e8710df0dfae'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/crab_406a4e43-dd7b-4875-91ac-e8710df0dfae.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'crab-with-raised-claws'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('crab', 'seafood', 'claw', 'pincer', 'shellfish', 'legs', 'animal')

    def build(self):
        # Plan: Broad crab body, paired open raised pincers and four legs. Six legs reduced to four. Shared mirror axis and exact shell attachments. No close Lucide match; envelope (6,6)-(42,42).
        self.add_bezier('shell',(12,28),((12,24),(18,24),(24,24)),((30,24),(36,24),(36,28)),((36,31),(35,34),(33,36)),((30,40),(26,42),(24,42)),((22,42),(18,40),(15,36)),((13,34),(12,31),(12,28)))
        self.add_contour('body','shell',closed=True)
        for side in (-1,1):
         def p(x,y):return (24+side*x,y)
         self.add_bezier(f'claw-{side}',p(10,6),(p(18,6),p(18,16),p(12,16)),(p(8,16),p(8,10),p(6,8)))
         self.add_line(f'arm-{side}',p(12,16),p(12,28));self.relate('connect',f'arm-{side}',f'claw-{side}');self.relate('connect',f'arm-{side}','body')
         self.add_line(f'leg-a-{side}',p(12,28),p(18,31));self.relate('connect',f'leg-a-{side}','body');self.relate('connect',f'leg-a-{side}',f'arm-{side}')
         self.add_line(f'leg-b-{side}',p(9,36),p(18,42));self.relate('connect',f'leg-b-{side}','body')
