"""Hooded infant in a rounded blanket with crossed folds. Human user.svg supplies circular face; source supplies capsule and folds. Shared hood axis24, cap16 and base radii8; face radius5; no facial marks."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e0eaa90e-ee21-4ae5-bede-0c17096fa38f'
SOURCE_PATH = 'work/drawn-unpublished-2026-09-21/batch-04/03-swaddled-newborn-baby/reference.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hooded-swaddle-with-crossed-blanket-folds-v2'
    variant_of = 'hooded-swaddle-with-crossed-blanket-folds'
    variant_label = 'Distilled reconstruction'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('hooded', 'swaddle', 'with', 'crossed', 'blanket', 'folds', 'v2')

    def build(self):
        def circle(name, x, y, r):
            pts=[(x-r,y),(x,y-r),(x+r,y),(x,y+r)]
            for i in range(4): self.add_arc(f'{name}-{i}',pts[i],pts[(i+1)%4],radius_x=r)
            self.add_contour(name,*[f'{name}-{i}' for i in range(4)],closed=True)
        def path(name, start, commands, closed=False):
            here=start; members=[]
            for i,(kind,end,*args) in enumerate(commands):
                part=f'{name}-{i}'
                if kind=='L': self.add_line(part,here,end)
                elif kind=='A': self.add_arc(part,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                else: self.add_bezier(part,here,(args[0],args[1],end))
                here=end; members.append(part)
            self.add_contour(name,*members,closed=closed)
        path('hood',(8,20),[('A',(24,4),16,16,True),('A',(40,20),16,16,True),('L',(40,28)),('L',(40,36)),('A',(32,44),8,8,True),('L',(16,44)),('A',(8,36),8,8,True),('L',(8,28)),('L',(8,20))],True)
        circle('face',24,17,5)
        self.add_polyline('fold-a',(8,28),(24,32),(40,36))
        self.add_line('fold-b',(40,28),(24,32))
        self.relate('connect','fold-a','hood')
        self.relate('connect','fold-b','hood')
        self.relate('connect','fold-a','fold-b')
