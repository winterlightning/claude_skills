'Elephant profile: coherent round crown, hanging ear and upturned trunk; preserve the curve character while opening the eye area.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '52c22bc9-c487-5768-a911-7e5b0e2ce1e4'
SOURCE_PATH = 'pictographic-primitives/animals/elephant head_52c22bc9-c487-5768-a911-7e5b0e2ce1e4.svg'
AUTHOR = 'gpt-6'


class MinimalElephantHead(Solo48):
    icon_id = 'minimal-elephant-head'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/animals"
    aliases = ()
    keywords = ('minimal', 'elephant', 'head')

    def build(self) -> None:
        self.add_bezier('crown',(4,16),((6,10),(12,8),(18,8)),((27,8),(34,9),(36,16)))
        self.add_polyline('trunk-top',(36,16),(36,31),(44,31),(44,36))
        self.add_bezier('trunk-tip',(44,36),((44,39),(40,40),(36,40)),((31,40),(28,38),(28,34)))
        self.add_line('throat',(28,34),(28,30))
        self.add_bezier('body',(28,30),((22,30),(17,32),(12,32)),((7,32),(4,23),(4,16)))
        for a,b in (('crown','trunk-top'),('trunk-top','trunk-tip'),('trunk-tip','throat'),('throat','body'),('body','crown')):self.relate('connect',a,b)
        self.add_line('ear-stem',(18,8),(18,16))
        self.add_bezier('ear',(18,16),((18,20),(16,21),(13,21)))
        self.relate('connect','ear-stem','crown');self.relate('connect','ear-stem','ear')
        self.add_dot('eye',(27,19))
