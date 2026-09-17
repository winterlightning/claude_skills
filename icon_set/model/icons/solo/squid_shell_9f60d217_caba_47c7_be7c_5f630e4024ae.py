'nautilus-shell: Use a round coiled shell with an expanding outer chamber and flared aperture. Repaired original in place.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9f60d217-caba-47c7-be7c-5f630e4024ae'
SOURCE_PATH = 'pictographic-primitives/animals/squid shell_9f60d217-caba-47c7-be7c-5f630e4024ae.svg'
AUTHOR = 'gpt-6'


class NautilusShell(Solo48):
    icon_id = 'nautilus-shell'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('nautilus', 'shell', 'spiral', 'sea', 'marine', 'cephalopod', 'coil', 'ocean')

    def build(self):
        # Symbol plan: Use a round coiled shell with an expanding outer chamber and flared aperture.

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
        path('shell',(24,24),[('A',(32,24),4,4,True),('A',(16,24),8,8,True),('C',(24,40),(16,34),(18,40)),('C',(42,24),(36,44),(42,36)),('A',(6,24),18,18,False),('L',(6,42)),('C',(24,40),(12,42),(18,42))])
