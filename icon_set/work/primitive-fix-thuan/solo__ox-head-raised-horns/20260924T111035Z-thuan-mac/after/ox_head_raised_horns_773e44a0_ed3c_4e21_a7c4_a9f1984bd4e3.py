"""Separate broad muzzle from tapered face at shared nodes and redraw symmetric horns with clean tips.
Construction: No useful exact Lucide match; supplied reference controls the silhouette.
Omissions: Small side ears omitted; raised horns and wide muzzle retained.
Keyshape SQUARE: authored to exact SOLO48 extremes."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '773e44a0-ed3c-4e21-a7c4-a9f1984bd4e3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__ox-head-raised-horns/20260924T111035Z-thuan-mac/reference/ox_773e44a0-ed3c-4e21-a7c4-a9f1984bd4e3.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'ox-head-raised-horns'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/reference'
    aliases = ()
    keywords = ('ox', 'head', 'raised', 'horns')
    def build(self):

        def path(name,start,commands,closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                here=end;members.append(ident)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(name,a,b):self.add_line(name,a,b)
        def poly(name,*pts,closed=False):self.add_polyline(name,*pts,closed=closed)
        def join(a,b):self.relate('connect',a,b)

        path('face',(18,34),[('C',(16,25),(17,32),(16,29)),('L',(16,17)),('L',(32,17)),('L',(32,25)),('C',(30,34),(32,29),(31,32))])
        path('muzzle',(18,34),[('L',(30,34)),('A',(30,42),4,4,True),('L',(18,42)),('A',(18,34),4,4,True)],True)
        join('face','muzzle')
        for s in (-1,1):
         def p(x,y):return (24+s*x,y)
         n='horn-left' if s==-1 else 'horn-right'
         path(n,p(8,17),[('C',p(18,6),p(15,17),p(18,13)),('C',p(8,25),p(18,22),p(15,25))])
         join(n,'face')
