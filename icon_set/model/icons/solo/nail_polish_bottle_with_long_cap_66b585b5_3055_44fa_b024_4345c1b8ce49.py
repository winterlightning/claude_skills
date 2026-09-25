"""Nail Polish Bottle with Long Cap.

Symbol plan: Rounded bottle body and tall narrow cap share one seam. Drop the small nested label to preserve clear bottle volume.
VRECT_L centerline extremes (8,4)-(40,44); exact envelope selected for the subject's proportions.
Construction reference: No useful exact Lucide subject match; reconstruct the supplied silhouette with coherent lines and arcs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '66b585b5-3055-44fa-b024-4345c1b8ce49'
SOURCE_PATH = 'pictographic-primitives/beauty/nail polisher_66b585b5-3055-44fa-b024-4345c1b8ce49.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'nail-polish-bottle-with-long-cap'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'beauty'
    categories = ('primitives', 'beauty')
    aliases = ()
    keywords = ('nail polish', 'bottle', 'cosmetic', 'manicure', 'beauty', 'cap', 'nail', 'personal care')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def path(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)

        line('cap-l',(18,24),(18,8));arc('cap-tl',(18,8),(22,4),4)
        line('cap-top',(22,4),(26,4));arc('cap-tr',(26,4),(30,8),4);line('cap-r',(30,8),(30,24))
        join('cap','cap-l','cap-tl','cap-top','cap-tr','cap-r')
        path('seam',(14,24),(18,24),(30,24),(34,24))
        arc('body-tr',(34,24),(40,30),6);line('body-r',(40,30),(40,38));arc('body-br',(40,38),(34,44),6)
        line('bottom',(34,44),(14,44));arc('body-bl',(14,44),(8,38),6);line('body-l',(8,38),(8,30));arc('body-tl',(8,30),(14,24),6)
        join('body','body-tr','body-r','body-br','bottom','body-bl','body-l','body-tl')
        connect('body','seam');connect('cap','seam')
