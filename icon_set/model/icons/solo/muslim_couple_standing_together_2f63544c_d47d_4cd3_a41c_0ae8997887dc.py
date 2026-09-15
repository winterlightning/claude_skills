"""Muslim Couple Standing Together.

Symbol plan: Two front-facing people, one pointed headscarf and one round cap, above simple garments. Drop tiny sleeve lines and layered cloth edges. Detached head/body gap is exactly 4 ink units.
HRECT_L centerline extremes (4,8)-(44,40); exact envelope selected for the subject's proportions.
Construction reference: human_ref/user.svg and full_body_ref.png: circular jaws, simple clothing silhouettes and exact detached gap. A two-person scene, not a single centered avatar.
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
        def path(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)
        def circle(n,x,y,r):
            pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
            for j in range(4): arc(n+str(j),pts[j],pts[j+1],r)
            join(n,*(n+str(j) for j in range(4)),closed=True)
        def box(n,x,y,w,h,r=2):
            pts=[(x+r,y),(x+w//2,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+w//2,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
            curves={2,4,7,9}
            for j in range(10):
                a,b=pts[j],pts[(j+1)%10]
                if a==b: continue
                if j in curves: arc(n+str(j),a,b,r)
                else: line(n+str(j),a,b)
            join(n,*(n+str(j) for j in range(10) if pts[j]!=pts[(j+1)%10]),closed=True)

        # Heads bottom at24; garment tops at32: centerline gap8, ink gap4.
        path('hood-top',(4,16),(12,8),(20,16))
        arc('woman-jaw',(20,16),(4,16),8)
        join('woman-head','hood-top-1','hood-top-2','woman-jaw',closed=True)
        self.contours=[c for c in self.contours if c.contour_id!='hood-top']
        arc('man-crown',(28,16),(44,16),8)
        arc('man-jaw',(44,16),(28,16),8)
        join('man-head','man-crown','man-jaw',closed=True)
        line('cap-brim',(28,16),(44,16));connect('cap-brim','man-head')
        path('woman-robe',(4,40),(12,32),(20,40),(4,40),closed=True)
        path('man-robe',(28,40),(28,32),(44,32),(44,40))
