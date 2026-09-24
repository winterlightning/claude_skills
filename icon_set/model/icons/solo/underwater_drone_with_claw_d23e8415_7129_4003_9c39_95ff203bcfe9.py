"""Submersible with smooth wave crests, rounded hull, coherent sloping tail fins, bent manipulator and open circular pincer. Source submersible preserved; local Lucide satellite-dish supplies related open arc construction. Small dorsal fin omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd23e8415-7129-4003-9c39-95ff203bcfe9'
SOURCE_PATH = 'pictographic-primitives/war/underwater drone 1_d23e8415-7129-4003-9c39-95ff203bcfe9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'underwater-drone-with-claw'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('underwater', 'drone', 'with', 'claw')

    def build(self):
        # Plan: Submersible with smooth wave crests, rounded hull, coherent sloping tail fins, bent manipulator and open circular pincer. Source submersible preserved; local Lucide satellite-dish supplies related open arc construction. Small dorsal fin omitted.
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
        path('water',(6,9),[('C',(18,9),(9,5),(15,5)),('C',(30,9),(21,13),(27,13)),('C',(42,9),(33,5),(39,5))])
        path('hull',(14,22),[('L',(28,22)),('A',(34,26),6,4,True),('A',(28,30),6,4,True),('L',(22,30)),('L',(14,30)),('L',(14,26)),('L',(14,22))],True)
        poly('tail',(6,18),(14,26),(6,34));join('tail','hull')
        path('arm',(22,30),[('L',(22,36)),('A',(24,38),2,2,False),('L',(36,38))]);join('arm','hull')
        path('claw',(42,34),[('A',(36,38),6,4,False),('A',(42,42),6,4,False)]);join('claw','arm')
