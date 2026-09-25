'Pair of teardrop earrings.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ef2a4929-2eb7-4242-b6c1-b1b1a7b79511'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-06/earrings oriental_ef2a4929-2eb7-4242-b6c1-b1b1a7b79511.svg'
AUTHOR = 'gpt-6'

class PairOfTeardropEarrings(Solo48):
    icon_id = 'pair-of-teardrop-earrings'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('pair', 'of', 'teardrop', 'earrings')

    def build(self):
        # Enlarged both matching top rings and kept balanced teardrops.

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
        for side,x in [('left',13),('right',35)]:
         ellipse(side+'-stud',x,10,4,4)
         line(side+'-link',(x,14),(x,22))
         path(side+'-drop',(x,22),[('L',(x+7,36)),('A',(x,42),7,6,True),('A',(x-7,36),7,6,True),('L',(x,22))],True)
         join(side+'-stud',side+'-link');join(side+'-link',side+'-drop')
