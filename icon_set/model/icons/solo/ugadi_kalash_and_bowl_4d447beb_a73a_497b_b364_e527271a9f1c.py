"""Restored the three-tip foliage crown and widened the kalash body, with an open rear contour behind the foreground bowl and an angled spoon. Lucide leaf and cooking-pot informed coherent curves; small rim thickness and leaf veins omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4d447beb-a73a-497b-b364-e527271a9f1c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/ugadi 1_4d447beb-a73a-497b-b364-e527271a9f1c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'ugadi-kalash-and-bowl'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'holidays'
    categories = ('primitives', 'holidays')
    aliases = ()
    keywords = ('ugadi', 'kalash', 'and', 'bowl')

    def build(self):
        # Plan: Kalash with a broad rounded pot, pointed coconut/leaf crown, and adjacent bowl with angled spoon. Lucide cooking-pot and leaf informed rounded vessels and smooth foliage; minor side leaves omitted to fit the complete two-vessel composition.
        def path(n, start, steps, closed=False):
            p=start; ids=[]
            for i,s in enumerate(steps):
                name=f'{n}-{i}'; kind,end,*args=s
                if kind=='L': self.add_line(name,p,end)
                elif kind=='A': self.add_arc(name,p,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(name,p,(args[0],args[1],end))
                ids.append(name); p=end
            self.add_contour(n,*ids,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        line=self.add_line; poly=self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        path('pot',(8,24),[('L',(22,24)),('C',(28,33),(24,28),(25,31)),('L',(30,34))])
        path('pot-left',(8,24),[('C',(6,34),(7,28),(6,31)),('A',(14,42),8,8,False),('L',(20,42))]);join('pot','pot-left')
        path('crown',(8,24),[('C',(6,10),(8,19),(6,14)),('C',(13,16),(10,11),(12,14)),('C',(17,6),(13,12),(15,8)),('C',(21,16),(20,9),(21,12)),('C',(28,10),(24,12),(26,11)),('C',(22,24),(26,17),(24,20))]);join('crown','pot');join('crown','pot-left')
        path('bowl',(30,34),[('L',(36,34)),('L',(42,34)),('A',(30,34),6,8,True)],True);join('pot','bowl')
        line('spoon',(36,34),(40,24));join('spoon','bowl')
