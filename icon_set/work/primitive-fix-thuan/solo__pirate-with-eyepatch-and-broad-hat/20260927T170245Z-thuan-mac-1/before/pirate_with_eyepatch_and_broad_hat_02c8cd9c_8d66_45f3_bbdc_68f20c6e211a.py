"""Pirate with Eyepatch and Broad Hat.

Symbol plan: Broad rounded pirate hat, circular jaw, diagonal eyepatch and open coat with a wrapping lapel; omit the second narrow coat seam.
VRECT_L centerline extremes (8,4)-(40,44); exact envelope selected for the subject's proportions.
Construction reference: Shared human_ref/user.svg: circular jaw, broad smooth shoulders and zero-ink-gap head/body contact. Supplied reference defines headwear; tiny trim is omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '02c8cd9c-8d66-45f3-bbdc-68f20c6e211a'
SOURCE_PATH = 'pictographic-primitives/avatars/pirate_02c8cd9c-8d66-45f3-bbdc-68f20c6e211a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pirate-with-eyepatch-and-broad-hat'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('pirate', 'eyepatch', 'hat', 'person', 'portrait', 'seafarer', 'costume', 'adventure')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def path(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)

        arc('hat-crown',(8,18),(40,18),16,14)
        path('brim',(8,18),(12,18),(24,18),(36,18),(40,18));connect('brim','hat-crown')
        arc('face',(36,18),(12,18),12);connect('face','brim')
        arc('patch',(24,18),(36,18),6,s=False);connect('patch','brim');connect('patch','face')
        bottom=30

        top = bottom + HEAD_BODY_CENTERLINE_GAP
        line('body-left-side',(8,44),(8,42))
        arc('body-left-shoulder',(8,42),(18,top),10,42-top)
        join('body-left','body-left-side','body-left-shoulder')
        line('body-top',(18,top),(24,top))
        line('body-top-right',(24,top),(30,top))
        arc('body-right-shoulder',(30,top),(40,42),10,42-top)
        line('body-right-side',(40,42),(40,44))
        join('body-right','body-right-shoulder','body-right-side')
        connect('body-left','body-top');connect('body-top','body-top-right');connect('body-top-right','body-right')
        connect('face','body-top');connect('face','body-top-right')
        line('body-coat-left',(18,top),(18,44));connect('body-coat-left','body-top')
        line('body-coat-right',(30,top),(30,44));connect('body-coat-right','body-top-right')
