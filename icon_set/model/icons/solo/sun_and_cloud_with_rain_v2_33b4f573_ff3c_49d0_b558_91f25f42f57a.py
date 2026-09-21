"""Sun behind a rounded cloud with three repeated diagonal raindrops. Lucide cloud-sun-rain supplies overlapping lobes and detached rain. Candidate retains sun disk, omits rays while testing space."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '33b4f573-ff3c-49d0-b558-91f25f42f57a'
SOURCE_PATH = 'work/drawn-unpublished-2026-09-21/batch-04/02-sun-behind-rainy-cloud/reference.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sun-and-cloud-with-rain-v2'
    variant_of = 'sun-and-cloud-with-rain'
    variant_label = 'Distilled reconstruction'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('sun', 'and', 'cloud', 'with', 'rain', 'v2')

    def build(self):
        def circle(name, x, y, r):
            self.add_arc(name+'-a',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(name+'-b',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(name,name+'-a',name+'-b',closed=True)
        def path(name, start, commands, closed=False):
            here=start; members=[]
            for i,(kind,end,*args) in enumerate(commands):
                part=f'{name}-{i}'
                if kind=='L': self.add_line(part,here,end)
                elif kind=='A': self.add_arc(part,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                else: self.add_bezier(part,here,(args[0],args[1],end))
                here=end; members.append(part)
            self.add_contour(name,*members,closed=closed)
        path('cloud',(14,32),[('A',(6,24),8,8,True),('A',(14,16),8,8,True),('C',(24,16),(14,5),(24,5)),('C',(32,24),(28,16),(32,20)),('A',(32,32),4,4,True),('L',(14,32))],True)
        path('sun',(24,16),[('A',(33,6),9,10,True),('A',(42,16),9,10,True),('A',(32,24),10,8,True)])
        self.relate('connect','sun','cloud')
        for x in (14,24,34): self.add_line(f'rain-{x}',(x,40),(x-2,42))
