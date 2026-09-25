'Blood bag: consistent rounded shoulders and broad integral outlet; centered medical cross with explicit intersection.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9abd9c20-5510-40da-8f74-a3309483ed6a'
SOURCE_PATH = 'pictographic-primitives/health/blood bag cross_9abd9c20-5510-40da-8f74-a3309483ed6a.svg'
AUTHOR = 'gpt-6'

class BloodBagCross(Solo48):
    icon_id = 'blood-bag-cross'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    categories = ('health', 'primitives')
    aliases = ()
    keywords = ('blood', 'bag', 'cross', 'health')

    def build(self) -> None:
        # VRECT_L: rounded bag, broad bottom neck and centered medical cross.
        self.add_line('top',(14,4),(34,4))
        self.add_arc('tr',(34,4),(40,10),radius_x=6)
        self.add_line('right',(40,10),(40,26))
        self.add_arc('br',(40,26),(34,32),radius_x=6)
        neck_points = ((34,32),(30,32),(30,40),(24,40),(18,40),(18,32),(14,32))
        for i,(a,b) in enumerate(zip(neck_points,neck_points[1:])): self.add_line('neck-'+str(i),a,b)
        self.add_arc('bl',(14,32),(8,26),radius_x=6)
        self.add_line('left',(8,26),(8,10))
        self.add_arc('tl',(8,10),(14,4),radius_x=6)
        self.add_contour('bag','top','tr','right','br',*('neck-'+str(i) for i in range(6)),'bl','left','tl',closed=True)
        self.add_line('tube',(24,40),(24,44))
        self.relate('connect','tube','bag')
        self.add_polyline('cross-h',(19,18),(24,18),(29,18))
        self.add_polyline('cross-v',(24,13),(24,18),(24,23))
        self.relate('connect','cross-h','cross-v')
