'Skunk: independent spacing revision.\n\nRebalanced geometry for eight-unit straight spacing and clear curved openings.\nNative solo family, HRECT_XL keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
# Variant of skunk; parent file remains unchanged.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c747f16a-3172-497d-9495-75b5f73d5aba'
SOURCE_PATH = 'pictographic-primitives/animals/skunk_c747f16a-3172-497d-9495-75b5f73d5aba.svg'
AUTHOR = 'gpt-6'

class Skunk(Solo48):
    icon_id = 'skunk'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('skunk', 'tail', 'bushy', 'stripe', 'animal', 'wildlife', 'spray', 'nocturnal')

    def build(self):
        # Enlarged and curved the torso and rounded the head while retaining the bushy curled tail.

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
        path('outline',(4,18),[('A',(24,18),10,10,True),('A',(20,24),10,10,True),('C',(34,20),(26,24),(28,20)),('L',(36,16)),('C',(44,24),(40,16),(44,20)),('L',(44,32)),('L',(40,32)),('L',(40,40)),('L',(32,40)),('L',(32,32)),('L',(20,32)),('L',(20,40)),('L',(12,40)),('L',(12,24)),('L',(4,18))],True)
