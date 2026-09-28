"""A rounded bird with swept crest, paired angry brows and a projecting beak; beak is part of the silhouette rather than a crowded interior hole.
References: Lucide face-angry for brow direction; supplied bird crest and beak identity.
Authored directly on SOLO48; original retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6a537336-3a61-589f-bdab-c6977b97e933'
SOURCE_PATH = 'pictographic-primitives/video-games/batch-01/angry birds_6a537336-3a61-589f-bdab-c6977b97e933.svg'
AUTHOR = 'gpt-6'

class AngryBird(Solo48):
    icon_id = 'angry-bird'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('angry', 'bird')

    def build(self):
        # Symbol plan: A rounded bird with swept crest, paired angry brows and a projecting beak; beak is part of the silhouette rather than a crowded interior hole.

        def path(n, start, commands, closed=False):
            here=start; members=[]
            for j,c in enumerate(commands):
                kind,end,*args=c; ident=('body-top' if j==2 else 'body-top-right') if n=='body' and j in (2,3) else f'{n}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident);here=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y), [('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(n,l,t,r,b,rad=3):
            path(n,(l+rad,t), [('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line;poly=self.add_polyline;dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)
        path('bird',(16,10),[('L',(24,4)),('L',(28,8)),('C',(36,20),(33,10),(36,14)),('L',(44,24)),('L',(36,28)),('C',(22,42),(36,36),(30,42)),('C',(7,26),(12,42),(7,36)),('C',(16,10),(7,18),(10,12))],True)
        poly('brows',(16,23),(23,26),(27,22))
