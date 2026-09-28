'Hydroelectric dam: independent spacing revision.\n\nEight-unit piers and one clear spillway stream touching the lower water.\nNative solo family, HRECT_XL keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6411cee5-9e14-533a-9adf-d5bcd2213734'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hydroelectric-dam/20260927T070849Z-thuan-mac-1/reference/water dam_6411cee5-9e14-533a-9adf-d5bcd2213734.svg'
AUTHOR = "gpt-6"

class HydroelectricDam(Solo48):
    icon_id = 'hydroelectric-dam'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'landmarks'
    categories = ('landmarks', 'primitives')
    aliases = ()
    keywords = ('dam', 'hydroelectric', 'water', 'reservoir', 'spillway', 'power', 'energy', 'infrastructure')

    def build(self):
        # Three curved water strokes form one continuous lower wave; one diagonal spillway mark restores the stream.

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
        poly('left-pier',(4,37),(4,8),(12,8),(12,16),(12,37),closed=True)
        poly('right-pier',(36,37),(36,16),(36,8),(44,8),(44,37),closed=True)
        line('crest',(12,16),(36,16));join('crest','left-pier');join('crest','right-pier')
        path('water',(4,37),[('A',(18,37),7,3,False),('A',(30,37),6,3,False),('A',(44,37),7,3,False)])
        line('spill',(24,24),(22,29))
        join('water','left-pier');join('water','right-pier')
