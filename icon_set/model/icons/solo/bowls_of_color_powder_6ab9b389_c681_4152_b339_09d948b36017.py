"""Two diagonally staggered bowls with broad powder mounds, front at left; mound and rim share exact endpoints.
Keyshape HRECT_L: exact SOLO48 contract envelope.
Construction references: Lucide soup: shallow bowl profile.
Omissions: No powder texture.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6ab9b389-c681-4152-b339-09d948b36017'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/holi_6ab9b389-c681-4152-b339-09d948b36017.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'bowls-of-color-powder'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'holidays'
    categories = ('primitives', 'holidays')
    aliases = ()
    keywords = ('holi',)
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

        # Shared bowl width, mound height and shallow basin depth.
        for i,x,y in [(0,12,32),(1,36,20)]:
         path(f'mound-{i}',(x-8,y),[('B',(x,y-12),(x-5,y-7),(x-4,y-12)),('B',(x+8,y),(x+4,y-12),(x+5,y-7))])
         path(f'bowl-{i}',(x-8,y),[('L',(x+8,y)),('B',(x+4,y+8),(x+6,y+5),(x+6,y+8)),('L',(x-4,y+8)),('B',(x-8,y),(x-6,y+8),(x-6,y+5))],True)
         join(f'mound-{i}',f'bowl-{i}')
