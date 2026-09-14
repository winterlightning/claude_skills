# Complete geometry repair; parent preserved.
'Hammer bar widened to 8 units; broad curved body and swept tail have room between opposing edges. Nonessential gill removed. Exact SQUARE bounds; Lucide fish informs a reduced continuous silhouette.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bdd1577c-6f14-5bee-a41f-fac2b80017a7'
SOURCE_PATH = 'pictographic-primitives/animals/shark hammer_bdd1577c-6f14-5bee-a41f-fac2b80017a7.svg'
AUTHOR = 'gpt-6'

class HammerheadSharkVariant5(Solo48):
    icon_id = 'hammerhead-shark-v5'
    variant_of = 'hammerhead-shark'
    variant_label = 'Exact keyshape bounds'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals/marine'
    aliases = ()
    keywords = ('hammerhead', 'shark', 'head', 'fins', 'sea', 'ocean', 'fish', 'predator')

    def build(self):
        # Broad 8-unit hammer bar, 12-unit body, one swept tail.
        # Lucide fish informs the reduced continuous silhouette. Gill mark omitted
        # to preserve body clearance; swept profile and fin points are intentional.
        points = [(6,6),(34,6),(34,14),(26,14),(26,18),(34,24),(26,26)]
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'head-{i}',a,b)
        self.add_arc('inner-body',(26,26),(34,32),radius_x=8,radius_y=6,sweep=False)
        self.add_line('tail-upper',(34,32),(40,22))
        self.add_arc('tail-end',(40,22),(40,42),radius_x=26)
        self.add_line('tail-bottom',(40,42),(30,42))
        self.add_arc('outer-body',(30,42),(14,26),radius_x=16,sweep=True)
        points = [(14,26),(6,26),(14,18),(14,14),(6,14),(6,6)]
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'left-{i}',a,b)
        self.add_contour('body',*[f'head-{i}' for i in range(1,7)],'inner-body','tail-upper','tail-end','tail-bottom','outer-body',*[f'left-{i}' for i in range(1,6)],closed=True)
