"""Moustache with Drooping Ends.

Symbol plan: Mirrored upper moustache lobes, broad center and downward curled ends. Use shared radii and tangent arcs; omit hair texture.
HRECT_L centerline extremes (4,8)-(44,40); exact envelope selected for the subject's proportions.
Construction reference: No useful exact Lucide subject match; reconstruct the supplied silhouette with coherent lines and arcs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2d299adf-39d3-4a59-a36e-c1a3f1ba07d3'
SOURCE_PATH = 'pictographic-primitives/beauty/mustache_2d299adf-39d3-4a59-a36e-c1a3f1ba07d3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'moustache-with-drooping-ends'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'beauty'
    aliases = ()
    keywords = ('beard', 'moustache', 'facial hair', 'grooming', 'barber', 'style', 'face', 'hair')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)

        arc('upper-l',(4,20),(24,20),10,12)
        arc('upper-r',(24,20),(44,20),10,12)
        line('outer-r',(44,20),(44,36))
        arc('tip-r',(44,36),(36,36),4)
        line('inner-r',(36,36),(36,34))
        arc('under-r',(36,34),(24,30),12,4,s=False)
        arc('under-l',(24,30),(12,34),12,4,s=False)
        line('inner-l',(12,34),(12,36))
        arc('tip-l',(12,36),(4,36),4)
        line('outer-l',(4,36),(4,20))
        join('moustache','upper-l','upper-r','outer-r','tip-r','inner-r','under-r','under-l','inner-l','tip-l','outer-l',closed=True)
