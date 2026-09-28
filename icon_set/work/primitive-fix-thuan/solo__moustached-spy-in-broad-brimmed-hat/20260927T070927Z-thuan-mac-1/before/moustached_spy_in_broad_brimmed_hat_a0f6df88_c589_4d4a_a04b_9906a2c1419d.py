"""Moustached Spy in Broad-Brimmed Hat.

Symbol plan: Broad brim and a low dipped crown above a circular jaw and a curved moustache; omit the inner hat band to preserve facial space.
VRECT_L centerline extremes (8,4)-(40,44); exact envelope selected for the subject's proportions.
Construction reference: Shared human_ref/user.svg: circular jaw, broad smooth shoulders and zero-ink-gap head/body contact. Supplied reference defines headwear; tiny trim is omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'a0f6df88-c589-4d4a-a04b-9906a2c1419d'
SOURCE_PATH = 'pictographic-primitives/avatars/police man spy_a0f6df88-c589-4d4a-a04b-9906a2c1419d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'moustached-spy-in-broad-brimmed-hat'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('spy', 'hat', 'sunglasses', 'person', 'portrait', 'disguise', 'agent', 'detective')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)

        self.add_bezier('crown',(11,16),((15,14),(13,4),(16,4)),((18,4),(18,6),(24,6)),((30,6),(30,4),(32,4)),((35,4),(33,14),(37,16)))

        arc('face-right',(37,16),(36,21),13)
        arc('face-lower-right',(36,21),(24,29),13)
        arc('face-lower-left',(24,29),(12,21),13)
        arc('face-left',(12,21),(11,16),13)
        join('face','face-right','face-lower-right','face-lower-left','face-left')
        connect('face','crown')
        line('brim-left',(8,16),(11,16));line('brim-right',(37,16),(40,16))
        connect('brim-left','crown');connect('brim-right','crown');connect('brim-left','face');connect('brim-right','face')
        arc('moustache-left',(12,21),(24,21),6,2)
        arc('moustache-right',(24,21),(36,21),6,2)
        join('moustache','moustache-left','moustache-right');connect('moustache','face')
        bottom=29

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

        line('body-wrap',(30,top),(18,44));connect('body-wrap','body-top-right')
