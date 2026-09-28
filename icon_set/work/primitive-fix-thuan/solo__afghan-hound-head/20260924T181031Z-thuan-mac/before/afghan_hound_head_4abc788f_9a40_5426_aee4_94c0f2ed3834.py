"""Afghan Hound Head.

Plan: Asymmetric profile under a tall elliptical coat; long muzzle and one eye identify the hound.
Keyshape centerline extremes: (8,4)-(40,44)
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4abc788f-9a40-5426-aee4-94c0f2ed3834'
SOURCE_PATH = 'pictographic-primitives/pets/afghan hound_4abc788f-9a40-5426-aee4-94c0f2ed3834.svg'
AUTHOR = 'gpt-6'

class AfghanHoundHead(Solo48):
    icon_id = 'afghan-hound-head'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/pets"
    aliases = ()
    keywords = ('dog', 'afghan-hound', 'hound', 'head', 'breed', 'long-hair', 'pet')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis=24
        arc('crown',(8,24),(40,24),16,20)
        line('coat-right',(40,24),(40,44))
        line('coat-left',(8,44),(8,24))
        contour('coat','coat-left','crown','coat-right')
        line('face',(21,16),(21,28))
        arc('muzzle',(21,28),(30,37),9,sweep=False)
        arc('chin',(30,37),(18,37),6,7)
        line('hair',(18,37),(18,44))
        contour('profile','face','muzzle','chin','hair')
        self.add_dot('eye',(30,23))
