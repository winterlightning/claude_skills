"""Restore upright hooked pruning blade and open counterblade with two separated rounded handles.
Construction: Lucide scissors: smooth handle turns and coherent blade/handle runs.
Omissions: Tiny pivot hole omitted.
Keyshape SQUARE: authored to exact SOLO48 extremes."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '90d90e0e-aba7-45e7-989c-2016fb704666'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__open-curved-pruning-shears/20260924T111035Z-thuan-mac/reference/prune_90d90e0e-aba7-45e7-989c-2016fb704666.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'open-curved-pruning-shears'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/reference'
    aliases = ()
    keywords = ('open', 'curved', 'pruning', 'shears')
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

        path('blade',(22,26),[('C',(24,14),(17,21),(23,17)),('L',(30,6)),('C',(30,22),(33,13),(34,18)),('C',(22,26),(28,26),(24,27))],True)
        path('counter',(30,22),[('L',(42,17)),('C',(27,32),(41,27),(36,31)),('L',(30,38)),('C',(24,42),(32,42),(26,42)),('L',(20,31)),('L',(22,26))])
        path('handle',(22,26),[('L',(11,39)),('C',(6,34),(8,42),(6,38)),('L',(17,23)),('L',(22,26))],True)
        join('blade','counter');join('blade','handle');join('counter','handle')
