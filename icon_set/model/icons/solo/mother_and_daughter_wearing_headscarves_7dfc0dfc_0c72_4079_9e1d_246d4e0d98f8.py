"""Mother and Daughter Wearing Headscarves.

Symbol plan: Adult and smaller child in rounded headscarves and continuous garments; shared circular-jaw vocabulary. Omit nested face borders and sleeve seams.
HRECT_L centerline extremes (4,8)-(44,40); exact envelope selected for the subject's proportions.
Construction reference: human_ref/user.svg and full_body_ref.png: circular jaws and rounded clothed silhouettes. Heads and garments are continuous; natural adult/child size asymmetry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7dfc0dfc-0c72-4079-9e1d-246d4e0d98f8'
SOURCE_PATH = 'pictographic-primitives/avatars/muslim mom daughter_7dfc0dfc-0c72-4079-9e1d-246d4e0d98f8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'mother-and-daughter-wearing-headscarves'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('mother', 'daughter', 'muslim', 'person', 'headscarf', 'clothing', 'portrait', 'islam', 'community', 'people')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)

        # Unequal covered heads and garments share their true face/cloth side junctions.
        for n,cx,cy,r in [('child',10,24,6),('mother',34,18,10)]:
            arc(n+'-crown',(cx-r,cy),(cx+r,cy),r)
            line(n+'-right',(cx+r,cy),(cx+r,38))
            arc(n+'-hem-r',(cx+r,38),(cx+r-2,40),2)
            line(n+'-hem',(cx+r-2,40),(cx-r+2,40))
            arc(n+'-hem-l',(cx-r+2,40),(cx-r,38),2)
            line(n+'-left',(cx-r,38),(cx-r,cy))
            join(n+'-outline',n+'-crown',n+'-right',n+'-hem-r',n+'-hem',n+'-hem-l',n+'-left',closed=True)
            arc(n+'-jaw',(cx+r,cy),(cx-r,cy),r)
            connect(n+'-jaw',n+'-outline')
