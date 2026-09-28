"""Person Using Open Laptop.

Symbol plan: Round-headed user behind an open angled laptop; retain a bent arm meeting the keyboard and a smooth outer shoulder.
HRECT_L centerline extremes (4,8)-(44,40); exact envelope selected for the subject's proportions.
Construction reference: Shared human_ref/full_body_ref.png: head aligned with upper torso and exact 8-unit centerline gap; Lucide laptop: sloped screen and base.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '98d57c01-7c97-4dd1-92f9-16dbd0cae67f'
SOURCE_PATH = 'pictographic-primitives/business/piracy content criminal_98d57c01-7c97-4dd1-92f9-16dbd0cae67f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'person-using-open-laptop'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('person', 'laptop', 'computer', 'work', 'technology', 'typing', 'office', 'device')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def path(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)
        def circle(n,x,y,r):
            pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
            for j in range(4): arc(n+str(j),pts[j],pts[j+1],r)
            join(n,*(n+str(j) for j in range(4)),closed=True)

        circle('head',30,14,6)
        path('laptop',(4,22),(18,22),(22,40),(8,40),(4,22),closed=True)
        path('keyboard',(22,40),(30,40),(44,40));connect('keyboard','laptop')
        line('torso',(30,28),(30,40));connect('torso','keyboard')
        arc('shoulder',(30,28),(44,40),14,12);connect('shoulder','torso');connect('shoulder','keyboard')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
