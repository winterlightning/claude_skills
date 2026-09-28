"""A top-view airliner points upper right with swept wings and a small tail.

Construction: plane: one continuous wing/fuselage silhouette and rounded nose.
Reduction: Omitted wing seams and widened the fuselage for native-size clarity. Diagonal orientation is intentional.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f7df912f-c801-53cc-a0b8-6bfbd3f5fdf8'
SOURCE_PATH = 'pictographic-primitives/travel/crafts model plane_f7df912f-c801-53cc-a0b8-6bfbd3f5fdf8.svg'
AUTHOR = 'gpt-6'


class SlenderAirlinerDiagonal(Solo48):
    icon_id = 'slender-airliner-diagonal'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/travel"
    aliases = ()
    keywords = ('airplane', 'plane', 'airliner', 'aircraft', 'flight', 'aviation', 'model', 'travel')

    def build(self) -> None:
        runs = {}
        def run(name, *points):
         ids = []
         for n,(a,b) in enumerate(zip(points,points[1:])):
          part = f'{name}-{n}'
          self.add_line(part,a,b)
          ids.append(part)
         runs[name] = ids
        # SQUARE extremes (6,6)-(42,42); nose is a radius5 semicircle on a 3:4 diagonal.
        run('tail-and-left-wing',(40,15),(33,22),(42,34),(34,42),(27,28),(20,35),(24,40),(14,42),(12,36),(6,34),(8,24),(13,28),(20,21),(6,14),(14,6),(26,15),(34,7))
        self.add_arc('nose',(34,7),(40,15),radius_x=5)
        self.add_contour('outline',*runs['tail-and-left-wing'],'nose',closed=True)
