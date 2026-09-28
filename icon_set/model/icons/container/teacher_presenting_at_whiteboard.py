'Teacher presenting at whiteboard: independent spacing revision.\n\nRemove narrow leg split and arm seams; open the two legs and add a clear presenting arm.\nNative container family, SQUARE keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Container64
AUTHOR = 'gpt-6'
SOURCE_ICON_ID = None
SOURCE_PATH = None

class TeacherPresentingAtWhiteboard(Container64):
    icon_id = 'teacher-presenting-at-whiteboard'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('teacher', 'presenting', 'at', 'whiteboard')

    def build(self):
        # Stick-line torso and limbs follow the human reference; head-to-torso ink gap is exactly four.

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
        path('board',(28,2),[('L',(56,2)),('A',(62,8),6,6,True),('L',(62,48)),('A',(56,54),6,6,True),('L',(38,54))])
        ellipse('head',15,11,9,9)
        line('torso',(15,28),(15,46))
        poly('legs',(2,62),(15,46),(28,62));join('legs','torso')
        poly('arms',(2,40),(15,28),(28,40),(38,30));join('arms','torso')
        self.mark_human_figure('teacher',head='head',torso='torso',torso_junction='start')
