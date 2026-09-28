"""Bearded Pirate with Crossed Hat Mark.

Symbol plan: Broad rounded pirate hat with a compact crossed emblem above a circular face and long pointed beard; omit fine face detail.
VRECT_L centerline extremes (8,4)-(40,44); exact envelope selected for the subject's proportions.
Construction reference: Shared human_ref/user.svg: circular jaw, broad smooth shoulders and zero-ink-gap head/body contact. Supplied reference defines headwear; tiny trim is omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '871b202b-58cd-4c8b-af66-2a006eddce86'
SOURCE_PATH = 'pictographic-primitives/avatars/pirate_871b202b-58cd-4c8b-af66-2a006eddce86.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bearded-pirate-with-crossed-hat-mark'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('beard', 'pirate', 'eyepatch', 'hat', 'person', 'portrait', 'seafarer', 'costume', 'adventure')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def path(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)

        arc('hat-left',(8,26),(24,4),16,22)
        arc('hat-right',(24,4),(40,26),16,22)
        join('hat','hat-left','hat-right')
        path('brim',(8,26),(18,26),(30,26),(40,26));connect('brim','hat')
        arc('face',(30,26),(18,26),6);connect('face','brim')
        line('beard-left',(18,26),(18,38));line('beard-right',(30,38),(30,26))
        self.add_bezier('beard-tip-left',(18,38),((18,40),(20,42),(24,44)))
        self.add_bezier('beard-tip-right',(24,44),((28,42),(30,40),(30,38)))
        join('beard','beard-left','beard-tip-left','beard-tip-right','beard-right')
        connect('beard','face');connect('beard','brim')
        path('mark-a',(22,13),(24,15),(26,17));path('mark-b',(22,17),(24,15),(26,13));connect('mark-a','mark-b')
