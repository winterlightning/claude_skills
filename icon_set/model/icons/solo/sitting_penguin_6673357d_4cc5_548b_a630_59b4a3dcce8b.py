'Sitting penguin.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The VRECT_L visible envelope is (6, 2, 42, 46).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6673357d-4cc5-548b-a630-59b4a3dcce8b'
SOURCE_PATH = 'pictographic-primitives/animals/tux_6673357d-4cc5-548b-a630-59b4a3dcce8b.svg'
AUTHOR = 'gpt-6'

class SittingPenguin(Solo48):
    icon_id = 'sitting-penguin'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('penguin', 'sitting', 'tux', 'linux', 'mascot', 'bird', 'flippers', 'antarctic')

    def build(self):
        # An oval body replaces the pinched waist; paired eyes and a beak preserve the penguin face.

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
        ellipse('body',24,24,16,20)
        dot('eye-left',(20,17));dot('eye-right',(28,17));dot('beak',(24,26))
        poly('feet',(8,44),(24,44),(40,44));join('body','feet')
