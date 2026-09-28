'mixed-reality-headset: Widen and flatten the visor, preserve the nose recess and show the side strap. Repaired original in place.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'dfd86ad0-9936-5051-a60d-200aa0c585ad'
SOURCE_PATH = 'pictographic-primitives/technology/apple vision pro_dfd86ad0-9936-5051-a60d-200aa0c585ad.svg'
AUTHOR = 'gpt-6'

class MixedRealityHeadset(Solo48):
    icon_id = 'mixed-reality-headset'
    keyshape = Keyshape.FREE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    categories = ('primitives', 'technology')
    aliases = ()
    keywords = ('headset', 'mixed-reality', 'vision-pro', 'visor', 'spatial', 'vr', 'ar', 'goggles')

    def build(self):
        # Symbol plan: Widen and flatten the visor, preserve the nose recess and show the side strap.

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
        path('visor',(14,12),[('L',(30,12)),('A',(40,22),10,10,True),('L',(40,26)),('A',(30,36),10,10,True),('C',(22,31),(26,36),(25,31)),('C',(14,36),(19,31),(18,36)),('A',(4,26),10,10,True),('L',(4,22)),('A',(14,12),10,10,True)],True)
        line('strap',(40,24),(44,24))
        join('visor','strap')
