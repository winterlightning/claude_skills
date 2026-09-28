"""Chinese ghost mask with a curved hat band, brow and nose, and pointed beard; mirrored face retains the source chin.
Keyshape VRECT_L: exact SOLO48 contract envelope.
Construction references: Lucide drama: coherent mask outline and minimal face.
Omissions: Cheek flourishes omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0592309c-696b-46e7-b80b-faf3ea17d049'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/hungry ghost festival_0592309c-696b-46e7-b80b-faf3ea17d049.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'chinese-ghost-mask'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'holidays'
    categories = ('primitives', 'holidays')
    aliases = ()
    keywords = ('hungry', 'ghost', 'festival')
    def build(self):

        def path(n, start, steps, closed=False):
            ids=[]; p=start
            for i,step in enumerate(steps):
                k=f'{n}-{i}';kind=step[0];q=step[1]
                if kind=='L': self.add_line(k,p,q)
                elif kind=='A': self.add_arc(k,p,q,radius_x=step[2],radius_y=step[3],sweep=step[4])
                elif kind=='B': self.add_bezier(k,p,(step[2],step[3],q))
                ids.append(k);p=q
            self.add_contour(n,*ids,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        path('hat',(8,8),[('A',(40,8),16,4,True),('L',(36,16)),('A',(12,16),12,4,False),('L',(8,8))],True)
        path('face',(12,16),[('L',(12,27)),('B',(24,44),(12,34),(18,39)),('B',(36,27),(30,39),(36,34)),('L',(36,16))])
        join('hat','face')
        poly('brow',(21,24),(24,24),(27,24));line('nose',(24,24),(24,32));join('brow','nose')
