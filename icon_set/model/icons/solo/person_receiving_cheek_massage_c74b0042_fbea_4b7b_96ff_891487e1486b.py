'person-receiving-cheek-massage: Show a relaxed face with two closed eyes and a curved hand pressing the cheek, with a visible wrist. Repaired original in place.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c74b0042-fbea-4b7b-96ff-891487e1486b'
SOURCE_PATH = 'pictographic-primitives/beauty/facial cleansing massage_c74b0042-fbea-4b7b-96ff-891487e1486b.svg'
AUTHOR = 'gpt-6'

class PersonReceivingCheekMassage(Solo48):
    icon_id = 'person-receiving-cheek-massage'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'beauty'
    aliases = ()
    keywords = ('massage', 'therapy', 'person', 'wellness', 'relaxation', 'treatment', 'body', 'spa')

    def build(self):
        # Symbol plan: Show a relaxed face with two closed eyes and a curved hand pressing the cheek, with a visible wrist.

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
        path('face',(24,42),[('C',(6,24),(12,42),(6,33)),('A',(24,6),18,18,True),('A',(42,24),18,18,True),('L',(42,28))])
        path('hand',(34,42),[('L',(34,34)),('C',(30,30),(34,32),(28,32)),('C',(34,28),(28,28),(31,28)),('L',(42,28)),('L',(42,42)),('L',(34,42))],True)
        join('hand','face')
        line('closed-eye-l',(17,19),(20,19));line('closed-eye-r',(28,19),(31,19))
