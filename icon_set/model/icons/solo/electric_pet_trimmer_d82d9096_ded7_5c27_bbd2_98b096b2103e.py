"""Electric Pet Trimmer.

Plan: Tapered upright trimmer with rounded base, five evenly spaced comb teeth and one front button stroke.
Centerline extremes: (8,4)-(40,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd82d9096-ded7-5c27-bbd2-98b096b2103e'
SOURCE_PATH = 'pictographic-primitives/pets/grooming electric trimmer_d82d9096-ded7-5c27-bbd2-98b096b2103e.svg'
AUTHOR = 'gpt-6'

class ElectricPetTrimmer(Solo48):
    icon_id = 'electric-pet-trimmer'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    categories = ("pets", "primitives")
    aliases = ()
    keywords = ('trimmer', 'clipper', 'grooming', 'electric', 'shaver', 'pet', 'fur')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        self.add_polyline('top',(8,12),(16,12),(24,12),(32,12),(40,12))
        line('right-side',(40,12),(36,36))
        arc('base',(36,36),(12,36),12,8)
        line('left-side',(12,36),(8,12))
        contour('body','right-side','base','left-side')
        self.relate('connect','top','body')
        for i,x in enumerate(range(8,41,8)):
         line(f'tooth-{i}',(x,4),(x,12));self.relate('connect','top',f'tooth-{i}')
         if i in (0,4):self.relate('connect','body',f'tooth-{i}')
        line('button',(24,24),(24,30))
