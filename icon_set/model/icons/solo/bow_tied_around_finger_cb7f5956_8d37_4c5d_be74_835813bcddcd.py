"""A bow tied above a downward pointing finger and curled palm; oblique hand retained, bow has two round loops.
Keyshape SQUARE: exact SOLO48 contract envelope.
Construction references: Lucide hand rounded fingertip and coherent palm; human_ref/user.svg and full_body_ref.png
Omissions: Neighboring curled finger crease lines omitted to retain open palm.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cb7f5956-8d37-4c5d-be74-835813bcddcd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/raksha bandhan_cb7f5956-8d37-4c5d-be74-835813bcddcd.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'bow-tied-around-finger'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/holidays'
    aliases = ()
    keywords = ('raksha', 'bandhan')
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

        path('bow',(30,16),[('B',(22,16),(27,16),(25,16)),('B',(16,10),(16,16),(16,14)),('B',(22,6),(16,6),(19,6)),('B',(30,16),(26,6),(28,12)),('B',(38,6),(33,9),(35,6)),('B',(42,12),(42,6),(42,9)),('B',(30,16),(42,16),(35,16))],True)
        path('hand',(22,16),[('L',(8,30)),('B',(6,35),(6,32),(6,33)),('B',(13,42),(6,39),(9,42)),('B',(18,40),(15,42),(16,42)),('L',(24,34)),('L',(29,29))])
        path('palm',(30,16),[('B',(38,26),(36,17),(38,20)),('B',(24,34),(38,35),(30,40))])
        join('bow','hand');join('bow','palm');join('hand','palm')
