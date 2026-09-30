"""gymnastics.
Symbol plan: SQUARE extremes (6,6)-(42,42). Symmetric split legs, inverted central torso and bent supporting arms. Head (24,36), r6; torso junction (24,22), exact outline-to-torso gap8 / ink gap4.
Shared human_ref/full_body_ref.png: circular outlined head, coherent round-ended limbs; mirrored inverted pose derived from supplied original. human_ref/user.svg also inspected.
Deliberate anatomical asymmetry preserves the supplied pose."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f9c85943-9f04-45d6-8250-b8130ceafc94'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__gymnast-in-split-leg-handstand/20260929T104744Z-thuan-mac/reference/gymnastics_f9c85943-9f04-45d6-8250-b8130ceafc94.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'gymnast-in-split-leg-handstand'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('gymnast', 'in', 'split', 'leg', 'handstand')
    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def bez(n,a,*segments): self.add_bezier(n,a,*segments)
        def path(n,*points,closed=False): self.add_polyline(n,*points,closed=closed)
        def contour(n,*members,closed=False): self.add_contour(n,*members,closed=closed)
        def connect(a,b): self.relate('connect',a,b)
        def circle(n,x,y,r):
            arc(n+'a',(x-r,y),(x+r,y),r)
            arc(n+'b',(x+r,y),(x-r,y),r)
            contour(n,n+'a',n+'b',closed=True)


        circle('head',24,36,6)
        line('torso',(24,22),(24,15))
        path('legs',(6,6),(24,15),(42,6));connect('legs','torso')
        path('arms',(9,42),(9,31),(24,22),(39,31),(39,42));connect('arms','torso')
        self.mark_human_figure('gymnast',head='head',torso='torso',torso_junction='start')

