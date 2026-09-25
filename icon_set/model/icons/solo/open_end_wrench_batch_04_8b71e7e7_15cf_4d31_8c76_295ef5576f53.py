"""Independent diagonal open-end wrench extracted as requested by the component brief. Lucide wrench supplies one closed fork-to-handle contour. No hanging hole; lightning is a separate sub component."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8b71e7e7-15cf-4d31-8c76-295ef5576f53'
SOURCE_PATH = 'work/drawn-unpublished-2026-09-21/batch-04/07-wrench-with-lightning-bolt/reference.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'open-end-wrench-batch-04'
    variant_of = 'wrench-with-lightning-bolt-batch-033'
    variant_label = 'Distilled reconstruction'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('open', 'end', 'wrench', 'batch', '04')

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
        path('wrench',(32,6),[('L',(24,14)),('L',(34,24)),('L',(42,16)),('C',(30,30),(42,27),(37,32)),('L',(18,42)),('C',(6,30),(11,42),(6,37)),('L',(18,18)),('C',(32,6),(16,10),(23,6))],True)
