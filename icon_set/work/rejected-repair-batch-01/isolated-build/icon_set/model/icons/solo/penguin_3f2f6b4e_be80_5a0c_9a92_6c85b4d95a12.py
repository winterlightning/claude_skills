'Standing penguin: rounded upright head, relaxed belly and clear folded flipper; preserve beak and tail.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3f2f6b4e-be80-5a0c-9a92-6c85b4d95a12'
SOURCE_PATH = 'pictographic-primitives/animals/penguin_3f2f6b4e-be80-5a0c-9a92-6c85b4d95a12.svg'
AUTHOR = 'gpt-6'


class StandingPenguin(Solo48):
    icon_id = 'standing-penguin'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('penguin', 'standing', 'bird', 'antarctic', 'flipper', 'beak', 'ice', 'simple')

    def build(self) -> None:
        self.add_bezier('crown',(12,16),((15,9),(19,4),(24,4)),((31,4),(36,10),(36,17)))
        self.add_line('back',(36,17),(36,38))
        self.add_bezier('tail',(36,38),((36,41),(38,44),(40,44)))
        self.add_line('base',(40,44),(22,44))
        self.add_bezier('belly',(22,44),((12,41),(13,26),(18,20)))
        self.add_line('beak-1',(18,20),(8,20))
        self.add_line('beak-2',(8,20),(12,16))
        self.add_contour('outline','crown','back','tail','base','belly','beak-1','beak-2',closed=True)
        self.add_dot('eye',(24,14))
        self.add_bezier('flipper',(25,26),((24,30),(25,33),(27,35)))
