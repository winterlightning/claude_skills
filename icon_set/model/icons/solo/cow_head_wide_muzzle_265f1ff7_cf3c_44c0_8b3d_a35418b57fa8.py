"""Revision for bad-stroke feedback. Lucide cat informed mirrored facial silhouette; cow reference owns horns, ears and muzzle.
Omissions: Eyes and nostrils omitted because enclosed bands cannot hold marks with MIC 8.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '265f1ff7-cf3c-44c0-8b3d-a35418b57fa8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/farming/milk cow_265f1ff7-cf3c-44c0-8b3d-a35418b57fa8.svg'
AUTHOR = 'gpt-6'
class Revision(Solo48):
    icon_id = 'cow-head-wide-muzzle'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'farming'
    aliases = ()
    keywords = ('milk', 'cow')
    def build(self):

        # Typed continuous paths own their junctions. Repeated parts share parameters.
        def path(name, start, commands, closed=False):
            ids=[]; here=start
            for i, (kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                ids.append(ident);here=end
            self.add_contour(name,*ids,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        # Shared axis24, mirrored horns and leaflike ears; broad capsule muzzle.
        path('face',(16,28),[('L',(16,16)),('L',(32,16)),('L',(32,28))])
        path('muzzle',(16,28),[('L',(32,28)),('A',(39,35),7,7,True),('A',(32,42),7,7,True),('L',(16,42)),('A',(9,35),7,7,True),('A',(16,28),7,7,True)],True)
        join('face','muzzle')
        for side in (-1,1):
            def p(x,y):return (24+side*x,y)
            path('horn-'+str(side),p(18,6),[('A',p(8,16),10,10,side>0)])
            path('ear-'+str(side),p(8,16),[('L',p(18,16)),('A',p(8,26),10,10,side>0),('L',p(8,16))],True)
            join('face','horn-'+str(side));join('face','ear-'+str(side));join('horn-'+str(side),'ear-'+str(side))
