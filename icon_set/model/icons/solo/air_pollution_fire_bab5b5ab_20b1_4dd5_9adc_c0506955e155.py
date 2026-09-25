"""Flame: rounded bowl, two rising tongues and a smooth inward lick. Lucide flame informs the continuous silhouette. Incomplete reference is completed from its named concept; no extra smoke.
Keyshape VRECT_L; clean centerlines revision. Shared symbol parameters own paired geometry."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bab5b5ab-20b1-4dd5-9adc-c0506955e155'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_01/air pollution fire_bab5b5ab-20b1-4dd5-9adc-c0506955e155.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='air-pollution-fire'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="Uncategorized"
    aliases=()
    keywords=('air', 'pollution', 'fire')
    def build(self):

        def path(n, start, commands, closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(commands):
                ident=f'{n}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident); here=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(n,l,t,r,b,k=2):
            path(n,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)
        line=self.add_line
        poly=self.add_polyline
        def join(a,b): self.relate('connect',a,b)

        path('flame',(24,4),[
            ('C',(40,28),(24,16),(40,16)),
            ('A',(8,28),16,16,True),
            ('C',(14,16),(8,22),(11,18)),
            ('C',(20,28),(12,23),(16,28)),
            ('C',(24,4),(28,28),(28,12))],True)
