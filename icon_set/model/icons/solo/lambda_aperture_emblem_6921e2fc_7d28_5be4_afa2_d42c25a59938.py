"""Six rotating aperture blades around a regularized hexagonal opening. Circle center (24,24), radius20. Shared ring and hexagon nodes preserve attachment topology. Lucide aperture supplies the continuous rim and repeated blade construction."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='6921e2fc-7d28-5be4-afa2-d42c25a59938'
SOURCE_PATH='pictographic-primitives/money/virtual coin crypto lambda_6921e2fc-7d28-5be4-afa2-d42c25a59938.svg'
AUTHOR='gpt-6'

class LambdaApertureEmblem(Solo48):
    icon_id='lambda-aperture-emblem'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "money"
    aliases=()
    keywords=('lambda', 'aperture', 'emblem', 'crypto', 'blade', 'circle')

    def build(self):
        rim=((24,4),(36,8),(44,24),(36,40),(24,44),(12,40),(4,24),(12,8))
        for n,a in enumerate(rim):self.add_arc(f'rim-{n}',a,rim[(n+1)%len(rim)],radius_x=20)
        self.add_contour('rim',*[f'rim-{n}' for n in range(len(rim))],closed=True)
        hexagon=((24,14),(33,19),(33,29),(24,34),(15,29),(15,19))
        outer=((36,8),(44,24),(36,40),(12,40),(4,24),(12,8))
        for n,a in enumerate(hexagon):
            self.add_line(f'hex-{n}',a,hexagon[(n+1)%6])
        self.add_contour('opening',*[f'hex-{n}' for n in range(6)],closed=True)
        for n,(a,b) in enumerate(zip(hexagon,outer)):
            self.add_line(f'blade-{n}',a,b)
            self.relate('connect',f'blade-{n}','rim')
            self.relate('connect',f'blade-{n}','opening')
