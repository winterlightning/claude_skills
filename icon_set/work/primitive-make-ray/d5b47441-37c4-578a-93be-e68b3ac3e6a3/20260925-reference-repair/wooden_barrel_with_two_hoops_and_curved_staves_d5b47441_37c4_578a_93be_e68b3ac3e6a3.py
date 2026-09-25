'Restored a fuller curved barrel on VRECT_L: narrower top and bottom, bowed walls and staves, and hoops moved toward the ends to expose the long central curves. Centerline bounds remain (8,4)–(40,44). All curve joins have aligned tangents. Full QA passes without exceptions.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
AUTHOR='gpt-6'
SOURCE_ICON_ID='d5b47441-37c4-578a-93be-e68b3ac3e6a3'
SOURCE_PATH='pictographic-primitives/drinks/wine barrel_d5b47441-37c4-578a-93be-e68b3ac3e6a3.svg'
class Drawing(Solo48):
    icon_id='wooden-barrel-with-two-hoops-and-curved-staves'
    keyshape=Keyshape.VRECT_L
    category='objects/drink'
    semantic_role='MAIN'
    semantic_kind='noun'
    aliases=()
    keywords=()
    def build(self):
        # Mirrored cubic curves with aligned tangent directions at each joint.
        for side in ('left','right'):
            flip=lambda p: p if side=='left' else (48-p[0],p[1])
            for name in ('wall','stave'):
                pts=([(12,4),(9,12),(8,24),(9,36),(12,44)] if name=='wall' else [(20,4),(18,12),(17,24),(18,36),(20,44)])
                controls=([((11,6),(10,8)),((8,16),(8,20)),((8,28),(8,32)),((10,40),(11,42))] if name=='wall' else [((19,6),(19,8)),((17,16),(17,20)),((17,28),(17,32)),((19,40),(19,42))])
                for i in range(4):
                    c1,c2=controls[i]
                    self.add_bezier(f'{name}-{side}-{i}',flip(pts[i]),(flip(c1),flip(c2),flip(pts[i+1])))
                self.add_contour(name+'-'+side,*(f'{name}-{side}-{i}' for i in range(4)))
        for name,y in [('top',4),('bottom',44)]:
            self.add_polyline(name,(12,y),(20,y),(28,y),(36,y))
            for part in ('wall-left','wall-right','stave-left','stave-right'):self.relate('connect',name,part)
        for y in (12,36):
            self.add_polyline('hoop-'+str(y),(9,y),(18,y),(30,y),(39,y))
            for part in ('wall-left','wall-right','stave-left','stave-right'):self.relate('connect','hoop-'+str(y),part)
