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
    aliases = ()
    keywords = ('ear', 'hearing', 'sound', 'listening', 'audio', 'wave', 'acoustic', 'anatomy')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def path(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)
        def circle(n,x,y,r):
            pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
            for j in range(4): arc(n+str(j),pts[j],pts[j+1],r)
            join(n,*(n+str(j) for j in range(4)),closed=True)
        def box(n,x,y,w,h,r=2):
            pts=[(x+r,y),(x+w//2,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+w//2,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
            curves={2,4,7,9}
            for j in range(10):
                a,b=pts[j],pts[(j+1)%10]
                if a==b: continue
                if j in curves: arc(n+str(j),a,b,r)
                else: line(n+str(j),a,b)
            join(n,*(n+str(j) for j in range(10) if pts[j]!=pts[(j+1)%10]),closed=True)

        arc('wave',(10,8),(10,40),6,16,s=False)
        arc('ear-top',(24,18),(44,18),10)
        arc('ear-right',(44,18),(36,30),8,12)
        line('ear-neck',(36,30),(36,34))
        arc('ear-lobe',(36,34),(24,34),6)
        join('ear','ear-top','ear-right','ear-neck','ear-lobe')
        line('fold-top',(33,18),(33,22))
        arc('fold-turn',(33,22),(29,26),4)
        join('fold','fold-top','fold-turn')
