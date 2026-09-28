"""Hanging Ball Cat Toy.

Plan: Hanging ball with straight string and an attached curled feather tail; bead removed. Circular ball owns exact top and bottom attachments.
Centerline extremes: (8,4)-(40,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7a06c938-aa06-5aee-b5c4-6a27a848e3b5'
SOURCE_PATH = 'pictographic-primitives/pets/cat toy_7a06c938-aa06-5aee-b5c4-6a27a848e3b5.svg'
AUTHOR = 'gpt-6'

class HangingBallCatToy(Solo48):
    icon_id = 'hanging-ball-cat-toy'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    categories = ("pets", "primitives")
    aliases = ()
    keywords = ('cat-toy', 'ball', 'string', 'hanging', 'feather', 'play', 'pet')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis = 24
        def mirror(p): return (2 * axis - p[0], p[1])
        line('string',(20,4),(20,14))
        arc('ball-right',(20,14),(20,38),12)
        arc('ball-left',(20,38),(20,14),12)
        contour('ball','ball-right','ball-left',closed=True)
        self.relate('connect','string','ball')
        line('feather-root',(20,38),(20,40))
        arc('feather-curl',(20,40),(24,44),4,sweep=False)
        arc('feather-tip',(24,44),(40,40),16,4,False)
        contour('feather','feather-root','feather-curl','feather-tip')
        self.relate('connect','feather','ball')
