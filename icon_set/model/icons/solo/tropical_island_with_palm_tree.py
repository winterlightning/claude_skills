'Tropical island with palm tree.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The VRECT_L visible envelope is (6, 2, 42, 46).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/model/icons/solo/tropical_island_with_palm_tree.py'
AUTHOR = 'gpt-6'

class TropicalIslandWithPalmTree(Solo48):
    icon_id = 'tropical-island-with-palm-tree'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature'
    aliases = ('tropical-island', 'palm-tree-island', 'island-palm')
    keywords = ('island', 'palm', 'tree', 'beach', 'tropical', 'vacation', 'holiday', 'sea', 'sand', 'water')

    def build(self):
        # Reduced to one island, a curved trunk and three fronds; removed the decorative waves.

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
        path('island',(8,40),[('A',(24,32),16,8,True),('A',(40,40),16,8,True),('A',(24,44),16,4,True),('A',(8,40),16,4,True)],True)
        path('trunk',(24,12),[('C',(24,32),(28,18),(28,26))]);join('trunk','island')
        path('left-frond',(24,12),[('C',(8,18),(18,8),(10,10))])
        path('right-frond',(24,12),[('C',(40,18),(30,8),(38,10))])
        path('top-frond',(24,12),[('C',(34,4),(24,6),(30,4))])
        for a in ['left-frond','right-frond','top-frond']:
         join(a,'trunk')
        for a,b in [('left-frond','right-frond'),('left-frond','top-frond'),('right-frond','top-frond')]:join(a,b)
