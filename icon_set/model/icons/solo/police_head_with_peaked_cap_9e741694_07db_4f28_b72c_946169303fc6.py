"""Police Head with Peaked Cap.

Symbol plan: Head-only police portrait with a broad pointed cap and curved visor above a circular jaw. Preserve the isolated head.
VRECT_L centerline extremes (8,4)-(40,44); exact envelope selected for the subject's proportions.
Construction reference: Shared human_ref/user.svg informs the circular jaw. Supplied reference establishes a head-only peaked cap with a curved visor.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '9e741694-07db-4f28-b72c-946169303fc6'
SOURCE_PATH = 'pictographic-primitives/avatars/police man_9e741694-07db-4f28-b72c-946169303fc6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'police-head-with-peaked-cap'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('avatars', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('police', 'officer', 'uniform', 'hat', 'person', 'portrait', 'security', 'law enforcement')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def path(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)

        path('cap',(8,12),(24,4),(40,12),(36,20),(12,20),(8,12),closed=True)
        line('band',(8,12),(40,12));connect('band','cap')
        arc('face',(36,32),(12,32),12)
        line('face-left',(12,20),(12,32));line('face-right',(36,32),(36,20))
        connect('face','face-left');connect('face','face-right');connect('face-left','cap');connect('face-right','cap')
        arc('visor',(12,20),(36,20),12,8,s=False);connect('visor','cap');connect('visor','face-left');connect('visor','face-right')
