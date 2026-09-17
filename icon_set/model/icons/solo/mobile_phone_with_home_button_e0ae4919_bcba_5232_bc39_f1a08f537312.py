'mobile-phone-with-home-button: Restore a tall narrow handset with a top speaker and round home button; remove the false screen divider. Repaired original in place.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e0ae4919-bcba-5232-bc39-f1a08f537312'
SOURCE_PATH = 'pictographic-primitives/mobile/mobile phone_e0ae4919-bcba-5232-bc39-f1a08f537312.svg'
AUTHOR = 'gpt-6'

class MobileIcon(Solo48):
    icon_id = 'mobile-phone-with-home-button'
    keyshape = Keyshape.FREE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/mobile'
    aliases = ()
    keywords = ('phone', 'mobile', 'screen', 'home-button', 'bezel', 'device', 'smartphone')

    def build(self):
        # Symbol plan: Restore a tall narrow handset with a top speaker and round home button; remove the false screen divider.

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
        rounded('phone',12,4,36,44,4)
        line('speaker',(21,13),(27,13));circle('home',24,33,2)
