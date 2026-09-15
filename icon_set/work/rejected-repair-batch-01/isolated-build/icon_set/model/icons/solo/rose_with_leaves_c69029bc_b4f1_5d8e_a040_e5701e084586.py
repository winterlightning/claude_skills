"""A cupped rose with a folded petal, straight stem, and paired leaves. VRECT extremes (8,4)-(40,44).
Reduction: Reduced layered inner petals to one folded diagonal; retained paired closed leaves.
Lucide: flower-2, leaf
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c69029bc-b4f1-5d8e-a040-e5701e084586'
SOURCE_PATH = 'pictographic-primitives/nature/rose_c69029bc-b4f1-5d8e-a040-e5701e084586.svg'
AUTHOR = 'gpt-6'

class RoseWithLeaves(Solo48):
    icon_id = 'rose-with-leaves'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/batch-03"
    aliases = ()
    keywords = ('rose', 'flower', 'bloom', 'stem', 'leaves', 'romance', 'love', 'garden')

    def build(self) -> None:
        a=24
        self.add_arc('top',(14,10),(34,10),radius_x=10,radius_y=6)
        self.add_line('right',(34,10),(34,16))
        self.add_arc('bowl-right',(34,16),(24,26),radius_x=10)
        self.add_arc('bowl-left',(24,26),(14,16),radius_x=10)
        self.add_line('left',(14,16),(14,10))
        self.add_contour('rose','top','right','bowl-right','bowl-left','left',closed=True)
        self.add_arc('fold',(14,10),(34,16),radius_x=20,radius_y=10)
        for p in ('top','left'): self.relate('connect','fold',p)
        for p in ('right','bowl-right'): self.relate('connect','fold',p)

        self.add_line('stem',(24,26),(24,44))
        for p in ('bowl-right','bowl-left'):self.relate('connect','stem',p)
        for side in (-1,1):
         tip=(24+side*16,32);joint=(24,44)
         self.add_arc(f'leaf-top-{side}',tip,joint,radius_x=16,radius_y=12,sweep=side<0)
         self.add_arc(f'leaf-bottom-{side}',joint,tip,radius_x=16,radius_y=12,sweep=side<0)
         self.add_contour(f'leaf-{side}',f'leaf-top-{side}',f'leaf-bottom-{side}',closed=True)
         for part in ('top','bottom'):self.relate('connect','stem',f'leaf-{part}-{side}')
