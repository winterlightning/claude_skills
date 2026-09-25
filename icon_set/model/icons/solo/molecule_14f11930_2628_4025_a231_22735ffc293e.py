'molecule-science: Use a central atom, three satellites and exposed bonds instead of a heavy triangular network. Repaired original in place.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '14f11930-2628-4025-a231-22735ffc293e'
SOURCE_PATH = 'pictographic-primitives/science/molecule_14f11930-2628-4025-a231-22735ffc293e.svg'
AUTHOR = 'gpt-6'

class MoleculeScience(Solo48):
    icon_id = 'molecule-science'
    keyshape = Keyshape.FREE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    categories = ('science', 'primitives')
    aliases = ()
    keywords = ('molecule', 'science')

    def build(self):
        # Symbol plan: Use a central atom, three satellites and exposed bonds instead of a heavy triangular network.

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
        circle('center',24,32,6);circle('left',6,32,4);circle('right',42,32,4);circle('top',24,14,4)
        for n,a,b,atom in [('bond-left',(10,32),(18,32),'left'),('bond-right',(30,32),(38,32),'right'),('bond-top',(24,18),(24,26),'top')]:
         line(n,a,b);join(n,'center');join(n,atom)
