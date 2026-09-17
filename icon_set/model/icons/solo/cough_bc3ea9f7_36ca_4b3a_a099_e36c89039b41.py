'cough: Keep the left-facing anatomical head and add two expelled breath strokes at the mouth. Repaired original in place.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc3ea9f7-36ca-4b3a-a099-e36c89039b41'
SOURCE_PATH = 'pictographic-primitives/health/cough_bc3ea9f7-36ca-4b3a-a099-e36c89039b41.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-repaired'

class Cough(Solo48):
    icon_id = 'cough'
    keyshape = Keyshape.FREE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('cough', 'health')

    def build(self):
        # Symbol plan: Keep the left-facing anatomical head and add two expelled breath strokes at the mouth.

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
        path('head',(40,44),[('L',(40,32)),('C',(44,18),(40,27),(44,25)),('A',(20,18),12,14,False),('L',(16,26)),('L',(20,26)),('L',(20,34)),('A',(24,38),4,4,False),('L',(28,38)),('L',(28,44))])
        line('cough-upper',(4,24),(8,26));line('cough-lower',(4,40),(8,38))
