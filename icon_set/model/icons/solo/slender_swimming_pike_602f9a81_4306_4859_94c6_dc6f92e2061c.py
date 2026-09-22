'Left-facing slender pike with forked tail and upper/lower fins. Lucide fish informs fin/body construction; preserve source direction and long body.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape HRECT_M uses exact SOLO48 contract bounds. Lucide fish original and atoms informed the continuous body contour; omit the crowded gill stroke.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '602f9a81-4306-4859-94c6-dc6f92e2061c'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_30/pike_602f9a81-4306-4859-94c6-dc6f92e2061c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'slender-swimming-pike'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ["pike", "long swimming pike fish"]
    keywords = ["fish", "swimming", "fins", "tail", "aquatic"]
    def build(self):


        def bez(name,start,*segments): self.add_bezier(name,start,*segments)

        bez('snout',(4,24),((8,18),(14,16),(20,16)))
        upper=[(20,16),(24,10),(32,10),(30,18),(34,20),(44,12),(40,24)]
        points=upper+[(x,48-y) for x,y in upper[-2::-1]]
        for i,(a,b) in enumerate(zip(points,points[1:]),1): self.add_line(f'dorsal-{i}',a,b)
        bez('belly',(20,32),((14,32),(8,30),(4,24)))
        self.add_contour('fish','snout',*[f'dorsal-{i}' for i in range(1,13)],'belly',closed=True)
