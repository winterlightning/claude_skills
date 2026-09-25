"""A steering wheel with round rim, central hub and four spokes. Lucide ship-wheel informed concentric rings and radial spokes. Circular keyshape preserves the rim; lower spokes diverge symmetrically."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f5cd3524-152e-5c6f-aaa6-f2bc2d392400'
SOURCE_PATH = 'pictographic-primitives/transportation/car tool steering wheel_f5cd3524-152e-5c6f-aaa6-f2bc2d392400.svg'
SOURCE_REFERENCES = (('f5cd3524-152e-5c6f-aaa6-f2bc2d392400', 'pictographic-primitives/transportation/car tool steering wheel_f5cd3524-152e-5c6f-aaa6-f2bc2d392400.svg'),)
AUTHOR = 'gpt-6'

class SteeringWheel(Solo48):
    icon_id = 'steering-wheel'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('steering wheel', 'driving', 'car', 'wheel', 'steer', 'control', 'vehicle', 'driver')

    def build(self) -> None:
        for name,r,pts in [('rim',20,[(4,24),(44,24),(36,40),(12,40),(4,24)]),('hub',10,[(14,24),(34,24),(30,32),(18,32),(14,24)])]:
            for i,(a,b) in enumerate(zip(pts,pts[1:])):
                self.add_arc(f'{name}-{i}',a,b,radius_x=r)
            self.add_contour(name,*[f'{name}-{i}' for i in range(4)],closed=True)
        for i,(a,b) in enumerate([((4,24),(14,24)),((34,24),(44,24)),((18,32),(12,40)),((30,32),(36,40))]):
            self.add_line(f'spoke-{i}',a,b)
            self.relate('connect',f'spoke-{i}','rim')
            self.relate('connect',f'spoke-{i}','hub')
