"""Restore grand piano silhouette, level keyboard edge and distinct even keys and legs.
Plan: coherent named contours and repeated dimensions. SQUARE natural subject envelope.
Construction reference: Lucide piano: smooth lid shoulder and repeated keys.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a53bd27a-5806-5a97-81ac-1e6b26e8a953'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__classical-piano/20260925T070532Z-thuan-mac/reference/classical piano_a53bd27a-5806-5a97-81ac-1e6b26e8a953.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'classical-piano'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('classical', 'piano')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                here=end;members.append(ident)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(name,l,t,r,b,rad=3):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('lid',(10,26),[('L',(10,10)),('A',(14,6),4,4,True),('L',(20,6)),('C',(32,17),(25,6),(25,17)),('L',(36,17)),('A',(42,23),6,6,True),('L',(42,26))])
        poly('keyboard',(10,26),(42,26),(42,36),(6,36),(6,31),(10,26),closed=True)
        join('keyboard','lid')
        for x in (16,24,32):
            line(f'key-{x}',(x,26),(x,31))
        for x in (12,36):
            line(f'leg-{x}',(x,36),(x,42))
