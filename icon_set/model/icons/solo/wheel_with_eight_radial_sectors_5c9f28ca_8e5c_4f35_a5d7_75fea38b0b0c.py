'An eight-spoked wheel with one hub and a circular rim. CIRCLE radius20 fills the radial keyshape. Source supplies eight sectors; Lucide circle-plus supplies rim and axial structure. Four cardinal quarters are split at genuine integer Pythagorean diagonal contacts (12,16). Horizontal and vertical mirror symmetry; diagonal spoke angles adjusted from45 degrees to53.13 degrees for exact integer circle attachment.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5c9f28ca-8e5c-4f35-a5d7-75fea38b0b0c'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_04/army symbol support_5c9f28ca-8e5c-4f35-a5d7-75fea38b0b0c.svg'
AUTHOR = "gpt-6-astra"
class Drawing(Solo48):
    icon_id = 'wheel-with-eight-radial-sectors'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ['Eight Spoked Support Wheel']
    keywords = ['wheel', 'spokes', 'sectors', 'circle', 'radial', 'support', 'symmetry']
    def build(self):
        points=[(24,4),(36,8),(44,24),(36,40),(24,44),(12,40),(4,24),(12,8)]
        for j,p in enumerate(points):
            self.add_arc(f'rim-{j}',p,points[(j+1)%8],radius_x=20)
            self.add_line(f'spoke-{j}',(24,24),p)
        self.add_contour('rim',*[f'rim-{j}' for j in range(8)],closed=True)
        self.relate('connect',*[f'spoke-{j}' for j in range(8)])
        for j in range(8): self.relate('connect','rim',f'spoke-{j}')
