"""Thermometer with a true rounded tube, symmetric bulb and two aligned scale marks. Lucide thermometer informed the bulb-to-tube transition; interior mercury retained at a readable size."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9c8949d3-833c-43ae-a29e-7b03ccb3f36b'
SOURCE_PATH = 'pictographic-primitives/other/thermometer_9c8949d3-833c-43ae-a29e-7b03ccb3f36b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'vertical-temperature-measurement-thermometer-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    aliases = ()
    keywords = ('vertical', 'temperature', 'measurement', 'thermometer', 'solo')

    def build(self):
        # Plan: Thermometer with a true rounded tube, symmetric bulb and two aligned scale marks. Lucide thermometer informed the bulb-to-tube transition; interior mercury retained at a readable size.
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
        path('outline',(10,28),[('L',(10,13)),('A',(28,13),9,9,True),('L',(28,28)),('C',(30,36),(30,30),(30,33)),('C',(19,44),(30,42),(25,44)),('C',(8,36),(13,44),(8,42)),('C',(10,28),(8,33),(8,30))],True)
        line('mercury',(19,24),(19,35))
        for i,y in enumerate((14,24)):line(f'scale-{i}',(38,y),(40,y))
