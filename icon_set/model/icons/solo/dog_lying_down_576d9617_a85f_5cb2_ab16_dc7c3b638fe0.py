"""Dog Lying Down.

Plan: Low resting dog with raised left tail, long back, rounded head, floppy ear and front paw.
Centerline extremes: (4,8)-(44,40).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '576d9617-a85f-5cb2-ab16-dc7c3b638fe0'
SOURCE_PATH = 'pictographic-primitives/pets/dog lying down_576d9617-a85f-5cb2-ab16-dc7c3b638fe0.svg'
AUTHOR = 'gpt-6'

class DogLyingDown(Solo48):
    icon_id = 'dog-lying-down'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    aliases = ()
    keywords = ('dog', 'lying', 'resting', 'sleep', 'down', 'pet', 'relax')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        arc('tail',(4,8),(8,24),4,16)
        line('back',(8,24),(26,24))
        arc('head',(26,24),(42,24),8)
        line('snout',(42,24),(44,24))
        arc('chin',(44,24),(36,32),8)
        line('paw-top',(36,32),(40,32))
        arc('paw',(40,32),(40,40),4)
        line('base',(40,40),(12,40))
        arc('rump',(12,40),(8,24),4,16)
        contour('body','back','head','snout','chin','paw-top','paw','base','rump',closed=True)
        self.relate('connect','tail','body')
        line('ear',(26,24),(26,31))
        self.relate('connect','ear','body')
