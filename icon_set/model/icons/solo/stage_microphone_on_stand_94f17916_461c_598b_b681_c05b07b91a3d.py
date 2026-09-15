"""Stage Microphone on Stand.

Symbol plan: Diagonal handheld stage microphone head and tapered grip with a pedestal stand. Omit the short cable to keep the handle/stand opening clear. Retain directional asymmetry.
VRECT_L centerline extremes (8,4)-(40,44); envelope follows the subject's proportions.
Construction reference: Lucide mic: simple capsule vocabulary; diagonal handle preserves the supplied stage microphone.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '94f17916-461c-598b-b681-c05b07b91a3d'
SOURCE_PATH = 'pictographic-primitives/audio/microphone stage_94f17916-461c-598b-b681-c05b07b91a3d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'stage-microphone-on-stand'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('stage', 'microphone', 'on', 'stand')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def path(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)

        # Cardinal and Pythagorean nodes belong to the same radius-10 head.
        arc('head-a',(20,14),(30,4),10)
        arc('head-b',(30,4),(40,14),10)
        arc('head-c',(40,14),(30,24),10)
        arc('head-d',(30,24),(22,20),10)
        arc('head-e',(22,20),(20,14),10)
        join('head','head-a','head-b','head-c','head-d','head-e',closed=True)
        path('grip',(22,20),(8,28),(12,31),(16,34),(30,24))
        connect('head','grip')
        line('stand',(30,24),(30,44))
        path('foot',(20,44),(30,44),(40,44))
        connect('head','stand');connect('grip','stand');connect('stand','foot')
