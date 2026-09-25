"""Sun behind a cloud with two rays and three diagonal rain strokes. SQUARE fits cloud-left, ray-top/right and rain-bottom. Source supplies scene and arrangement; Lucide cloud-sun-rain supplies lobe construction and detached rainfall. Sun radius8, shared attachment nodes (24,24) and (32,32); repeated rain step10. Two rays retained; other rays omitted to preserve gaps."""
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
    category = 'primitives-generate'
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
        path('cloud',(14,32),[('A',(6,24),8,8,True),('A',(14,16),8,8,True),('C',(24,24),(14,8),(24,8)),('C',(32,32),(28,24),(32,28)),('L',(14,32))],True)
        path('sun',(24,24),[('A',(32,16),8,8,True),('A',(40,24),8,8,True),('A',(32,32),8,8,True)])
        self.relate('connect','sun','cloud')
        self.add_line('ray-top',(32,6),(32,8))
        self.add_line('ray-diagonal',(42,10),(42,11))
        for x in (14,24,34): self.add_line(f'rain-{x}',(x,40),(x-2,42))
