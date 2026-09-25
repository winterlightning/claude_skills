"""Treble clef with round upper loop, full central bowl and curved bottom hook; staff fragments remain at regular 8-unit pitch. Lucide music provides coherent symbol strokes; no exact clef match."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='57a950ed-c372-483c-a381-f0de14acc5e9'
SOURCE_PATH='pictographic-primitives/music/music clef sheet_57a950ed-c372-483c-a381-f0de14acc5e9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'treble-clef-on-staff'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'music'
    aliases = ()
    keywords = ('treble', 'clef', 'on', 'staff')

    def build(self):
        # Plan: Treble clef with round upper loop, full central bowl and curved bottom hook; staff fragments remain at regular 8-unit pitch. Lucide music provides coherent symbol strokes; no exact clef match.
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
        path('stem',(24,12),[('L',(24,20)),('L',(24,30)),('L',(24,35)),('A',(19,40),5,5,True)])
        path('upper',(24,12),[('A',(28,8),4,4,True),('A',(32,12),4,4,True),('C',(24,20),(32,15),(28,18))]);join('upper','stem')
        path('bowl',(24,20),[('C',(16,29),(19,23),(16,25)),('C',(24,32),(16,32),(20,32)),('C',(30,27),(29,32),(32,30)),('C',(24,24),(29,24),(26,24))]);join('bowl','stem');join('bowl','upper')
        for i,y in enumerate((12,20,28,36)):
            line(f'staff-left-{i}',(4,y),(7,y));line(f'staff-right-{i}',(41,y),(44,y))
