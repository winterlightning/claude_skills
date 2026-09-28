"""An upright airplane has broad rounded wings and rounded tail tips.

Construction: plane: shared fuselage contour; luggage: quarter-circle transitions for repeated rounded corners.
Reduction: Broadened wings and tail to preserve open space; mirrored about x=24.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3d6cd0c8-32b5-4b44-85b4-ced44e8263e3'
SOURCE_PATH = 'pictographic-primitives/travel/plane_3d6cd0c8-32b5-4b44-85b4-ced44e8263e3.svg'
AUTHOR = 'gpt-6'


class AirplaneTopViewRoundedWings(Solo48):
    icon_id = 'airplane-top-view-rounded-wings'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "travel"
    categories = ("travel", "state", "other", "primitives-generate")
    aliases = ()
    keywords = ('airplane', 'plane', 'aircraft', 'top-view', 'flight', 'mode', 'aviation', 'travel')

    def build(self) -> None:
        runs = {}
        def run(name, *points):
         ids = []
         for n,(a,b) in enumerate(zip(points,points[1:])):
          part = f'{name}-{n}'
          self.add_line(part,a,b)
          ids.append(part)
         runs[name] = ids
        # SQUARE extremes (6,6)-(42,42); paired rounded wing tips use radius4.
        run('upper-right',(29,11),(29,12),(38,15))
        self.add_arc('right-tip',(38,15),(38,25),radius_x=4,radius_y=5)
        run('lower-right',(38,25),(29,22),(29,31),(34,32))
        self.add_arc('right-tail',(34,32),(34,42),radius_x=4,radius_y=5)
        run('tail-notch',(34,42),(24,38),(14,42))
        self.add_arc('left-tail',(14,42),(14,32),radius_x=4,radius_y=5)
        run('lower-left',(14,32),(19,31),(19,22),(10,25))
        self.add_arc('left-tip',(10,25),(10,15),radius_x=4,radius_y=5)
        run('upper-left',(10,15),(19,12),(19,11))
        self.add_arc('nose',(19,11),(29,11),radius_x=5)
        self.add_contour('airplane',*runs['upper-right'],'right-tip',*runs['lower-right'],'right-tail',*runs['tail-notch'],'left-tail',*runs['lower-left'],'left-tip',*runs['upper-left'],'nose',closed=True)
