"""Giraffe with long gently leaning neck, rounded muzzle and foot corners, small ear and two visible legs; no exact Lucide giraffe match. Source directional asymmetry retained. Lengthened the legs while retaining the long neck and rounded muzzle."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '91e66038-39e6-4fde-9641-6dc2916522b9'
SOURCE_PATH = 'pictographic-primitives/animals/giraffe body_91e66038-39e6-4fde-9641-6dc2916522b9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'standing-giraffe'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('standing', 'giraffe')

    def build(self):
        # Plan: Giraffe with long gently leaning neck, rounded muzzle and foot corners, small ear and two visible legs; no exact Lucide giraffe match. Source directional asymmetry retained.
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
        path('body',(10,44),[('A',(8,42),2,2,True),('L',(8,30)),('A',(12,26),4,4,True),('L',(18,26)),('A',(24,20),6,6,False),('L',(26,8)),('L',(32,8)),('L',(38,14)),('C',(40,18),(40,16),(40,16)),('A',(36,22),4,4,True),('L',(32,22)),('L',(32,42)),('A',(30,44),2,2,True),('L',(26,44)),('A',(24,42),2,2,True),('L',(24,34)),('L',(16,34)),('L',(16,42)),('A',(14,44),2,2,True),('L',(10,44))],True)
        line('ear',(26,8),(22,4));join('ear','body')
