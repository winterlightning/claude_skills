"""Muslim Couple Standing Together.

Symbol plan: Two front-facing people in continuous draped clothing, one headscarf and one round cap. Drop tiny sleeve lines and layered cloth edges.
HRECT_L centerline extremes (4,8)-(44,40); exact envelope selected for the subject's proportions.
Construction reference: human_ref/user.svg and full_body_ref.png: circular jaws and simple clothing silhouettes. Continuous clothed figures, not detached stick figures or one centered avatar.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2f63544c-d47d-4cd3-a41c-0ae8997887dc'
SOURCE_PATH = 'pictographic-primitives/avatars/muslim couple_2f63544c-d47d-4cd3-a41c-0ae8997887dc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'muslim-couple-standing-together'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('muslim', 'person', 'headscarf', 'clothing', 'portrait', 'islam', 'community', 'people')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)

        # The headscarf and long garment form one continuous clothed outline.
        for n,cx in [('woman',12),('man',36)]:
            arc(n+'-crown',(cx-8,16),(cx+8,16),8)
            line(n+'-right',(cx+8,16),(cx+8,38))
            arc(n+'-hem-r',(cx+8,38),(cx+6,40),2)
            line(n+'-hem',(cx+6,40),(cx-6,40))
            arc(n+'-hem-l',(cx-6,40),(cx-8,38),2)
            line(n+'-left',(cx-8,38),(cx-8,16))
            join(n+'-outline',n+'-crown',n+'-right',n+'-hem-r',n+'-hem',n+'-hem-l',n+'-left',closed=True)
            arc(n+'-jaw',(cx+8,16),(cx-8,16),8)
            connect(n+'-jaw',n+'-outline')
        line('cap-brim',(28,16),(44,16));connect('cap-brim','man-outline');connect('cap-brim','man-jaw')
