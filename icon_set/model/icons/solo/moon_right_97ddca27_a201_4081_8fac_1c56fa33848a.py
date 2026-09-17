'moon-right: Make the illuminated crescent slimmer, with rounded outer curvature and long inward-curving horns. Repaired original in place.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '97ddca27-a201-4081-8fac-1c56fa33848a'
SOURCE_PATH = 'pictographic-primitives/symbol/moon right_97ddca27-a201-4081-8fac-1c56fa33848a.svg'
AUTHOR = 'gpt-6'

class MoonRight(Solo48):
    icon_id = 'moon-right'
    keyshape = Keyshape.FREE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('solo-ai-full-set', 'moon-right')

    def build(self):
        # Symbol plan: Make the illuminated crescent slimmer, with rounded outer curvature and long inward-curving horns.

        def path(name,start,commands,closed=False):
            members=[];here=start
            for i,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident);here=end
            self.add_contour(name,*members,closed=closed)
        def ellipse(name,x,y,rx,ry):
            path(name,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def circle(name,x,y,r): ellipse(name,x,y,r,r)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line;poly=self.add_polyline;dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)
        path('crescent',(12,4),[('C',(38,24),(27,4),(38,10)),('C',(12,44),(38,38),(27,44)),('C',(28,24),(23,41),(28,34)),('C',(12,4),(28,14),(23,7))],True)
