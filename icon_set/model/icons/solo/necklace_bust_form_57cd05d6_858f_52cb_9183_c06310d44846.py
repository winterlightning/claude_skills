'Necklace bust form.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The VRECT_L visible envelope is (6, 2, 42, 46).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '57cd05d6-858f-52cb-9183-c06310d44846'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-03/necklace_57cd05d6-858f-52cb-9183-c06310d44846.svg'
AUTHOR = 'gpt-6'

class NecklaceBustForm(Solo48):
    icon_id = 'necklace-bust-form'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('necklace', 'bust', 'form', 'display', 'mannequin', 'jewellery', 'jewelry', 'torso', 'stand')

    def build(self):
        # Widened the bust base and shortened the necklace drop to open the side and bottom gaps.

        def path(n, start, commands, closed=False):
            names=[];here=start
            for j,(kind,end,*args) in enumerate(commands):
                ident=f'{n}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                names.append(ident);here=end
            self.add_contour(n,*names,closed=closed)
        def ellipse(n,x,y,rx,ry):
            path(n,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        line=self.add_line;poly=self.add_polyline;dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)
        path('form',(16,4),[('L',(32,4)),('C',(40,16),(32,12),(36,16)),('L',(36,44)),('L',(12,44)),('L',(8,16)),('C',(16,4),(12,16),(16,12))],True)
        path('necklace',(16,4),[('C',(24,28),(16,20),(18,28)),('C',(32,4),(30,28),(32,20))]);join('form','necklace')
