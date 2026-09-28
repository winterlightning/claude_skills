"""Three recycling arrows with consistent broad arrowheads and rounded turning corners. Lucide recycle informs the triangular circulation; folded ribbon edges omitted to preserve space at 48px."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5e1048c9-9d25-56a8-b734-5d83dac9ce83'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/ecology/recycling sign_5e1048c9-9d25-56a8-b734-5d83dac9ce83.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-folded-arrows-forming-recycling-loop'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'ecology'
    categories = ('primitives', 'ecology')
    aliases = ()
    keywords = ('three', 'folded', 'arrows', 'forming', 'recycling', 'loop')

    def build(self):
        # Plan: Three recycling arrows with consistent broad arrowheads and rounded turning corners. Lucide recycle informs the triangular circulation; folded ribbon edges omitted to preserve space at 48px.
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
        path('top',(18,12),[('L',(21,8)),('A',(27,8),3,2,True),('L',(36,22))])
        poly('top-head',(27,20),(36,22),(39,13));join('top','top-head')
        path('right',(42,29),[('L',(38,37)),('A',(33,42),5,5,True),('L',(20,42))])
        poly('right-head',(27,35),(20,42),(29,42));join('right','right-head')
        path('left',(12,42),[('L',(7,32)),('C',(7,27),(6,30),(6,29)),('L',(12,19))])
        poly('left-head',(6,21),(12,19),(15,27));join('left','left-head')
