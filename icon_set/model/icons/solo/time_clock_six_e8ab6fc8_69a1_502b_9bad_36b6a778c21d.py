"""Replaced faceted half-clock rim with an exact semicircle. Kept the left middle and three right ticks; omitted two crowded diagonal left ticks. Lucide clock informed the circular construction."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e8ab6fc8-69a1-502b-9bad-36b6a778c21d'
SOURCE_PATH = 'pictographic-primitives/interface-essential/time clock six_e8ab6fc8-69a1-502b-9bad-36b6a778c21d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'time-clock-six'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('time', 'clock', 'six')

    def build(self):
        # Plan: Exact semicircle with one attached left tick and three detached right ticks.
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
        path('half',(24,6),[('A',(6,24),18,18,False),('A',(24,42),18,18,False),('L',(24,6))],True)
        line('left-mid',(6,24),(10,24));join('left-mid','half')
        for n,a,b in [('right-top',(35,14),(38,11)),('right-mid',(39,24),(42,24)),('right-bottom',(35,34),(38,37))]:line(n,a,b)
