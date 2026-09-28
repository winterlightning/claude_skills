"""Ear with Sound Waves on Left.

Symbol plan: Large ear with a smooth outer rim, lobe and inner fold; a single broad wave preserves the listening cue. Drop the smaller second wave.
HRECT_L centerline extremes (4,8)-(44,40); exact envelope selected for the subject's proportions.
Construction reference: Lucide ear: broad rim, rounded lobe and a reduced inner fold.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a556ee5b-117d-4512-906c-2cde16ba32e8'
SOURCE_PATH = 'pictographic-primitives/audio/music ear_a556ee5b-117d-4512-906c-2cde16ba32e8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'ear-with-sound-waves-on-left'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    categories = ('audio', 'primitives')
    aliases = ()
    keywords = ('ear', 'hearing', 'sound', 'listening', 'audio', 'wave', 'acoustic', 'anatomy')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)

        arc('wave',(10,8),(10,40),6,16,s=False)
        arc('ear-top',(24,18),(44,18),10)
        arc('ear-right',(44,18),(36,30),8,12)
        line('ear-neck',(36,30),(36,34))
        arc('ear-lobe',(36,34),(24,34),6)
        join('ear','ear-top','ear-right','ear-neck','ear-lobe')
        line('fold',(33,18),(31,22))
