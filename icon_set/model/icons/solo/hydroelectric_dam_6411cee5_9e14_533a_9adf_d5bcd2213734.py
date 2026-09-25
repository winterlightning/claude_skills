'Hydroelectric dam: independent spacing revision.\n\nEight-unit piers and one clear spillway stream above lower water.\nNative solo family, HRECT_XL keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6411cee5-9e14-533a-9adf-d5bcd2213734'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-07/water dam_6411cee5-9e14-533a-9adf-d5bcd2213734.svg'
AUTHOR = 'gpt-6'

class HydroelectricDam(Solo48):
    icon_id = 'hydroelectric-dam'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'landmarks'
    aliases = ()
    keywords = ('dam', 'hydroelectric', 'water', 'reservoir', 'spillway', 'power', 'energy', 'infrastructure')

    def build(self):
        # Three curved water strokes form one continuous lower wave; the straight stream is removed.

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
        poly('left-pier',(4,24),(4,8),(12,8),(12,16),(12,24),closed=True)
        poly('right-pier',(36,24),(36,16),(36,8),(44,8),(44,24),closed=True)
        line('crest',(12,16),(36,16));join('crest','left-pier');join('crest','right-pier')
        path('water',(4,37),[('A',(18,37),7,3,False),('A',(30,37),6,3,False),('A',(44,37),7,3,False)])
