"""Sprouting Potted Plant.
Plan: One high left leaf and one lower right leaf on a stem above a tapered pot. Extrema (8,4)-(40,44).
Reference: Lucide sprout: two simple leaf contours with shared stem junctions.
Reduction: Double pot rim and leaf veins omitted; staggered attachment heights retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1bbd9cd8-2ed7-5e55-b8ae-ee312ee5b289'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/farming/gardening pot_1bbd9cd8-2ed7-5e55-b8ae-ee312ee5b289.svg'
AUTHOR = 'gpt-6'

class Batch29Icon(Solo48):
    icon_id = 'potted-plant-staggered-leaves'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/agriculture"
    aliases = ()
    keywords = ('sprouting', 'potted', 'plant')

    def build(self):

        self.add_bezier('left-a',(8,4),((20,4),(24,7),(24,16)))
        self.add_bezier('left-b',(24,16),((12,16),(8,13),(8,4)))
        self.add_contour('left','left-a','left-b',closed=True)

        self.add_bezier('right-a',(40,12),((28,12),(24,15),(24,24)))
        self.add_bezier('right-b',(24,24),((36,24),(40,21),(40,12)))
        self.add_contour('right','right-a','right-b',closed=True)

        self.add_polyline('stem',(24,16),(24,24),(24,32))
        for n in ('left','right'):self.relate('connect','stem',n)
        self.add_polyline('pot',(10,32),(24,32),(38,32),(32,44),(16,44),(10,32));self.relate('connect','stem','pot')
