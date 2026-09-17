"""Rounded Books on a Shelf.

Two rounded books on a low shelf: shorter book leaning left and taller upright book. Centerline extremes (6,6)-(42,42). Lucide book-open informs smooth book ends; preserve unequal heights and source lean. Keep the thick shelf and short supports.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '22233a6a-0b26-5074-b06d-ed3cf35d9aa1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/shelf books round_22233a6a-0b26-5074-b06d-ed3cf35d9aa1.svg'
AUTHOR = 'gpt-6'

class RoundedBooksOnLowShelf(Solo48):
    icon_id = 'rounded-books-on-low-shelf'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    aliases = ()
    keywords = ('rounded', 'books', 'on', 'a', 'shelf')

    def build(self):
        # Symbol plan: Two rounded books on a low shelf: shorter book leaning left and taller upright book. Centerline extremes (6,6)-(42,42). Lucide book-open informs smooth book ends; preserve unequal heights and source lean. Keep the thick shelf and short supports.

        def path(name, start, commands, closed=False):
            members=[]
            for i, command in enumerate(commands):
                kind,end,*args=command
                member=f'{name}-{i}'
                if kind=='L': self.add_line(member,start,end)
                elif kind=='A': self.add_arc(member,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,start,(args[0],args[1],end))
                members.append(member)
                start=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,x,y,rx,ry):
            path(name,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(name,l,t,r,b,rad=4):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        def bilateral(name, start, right, closed=True):
            # One half owns geometry; mirror and reverse it about the shared axis.
            axis=24
            mirror=lambda p:(2*axis-p[0],p[1])
            segments=[]
            here=start
            for kind,end,*args in right:
                segments.append((kind,here,end,args));here=end
            left=[]
            for kind,begin,end,args in reversed(segments):
                if kind=='C': left.append((kind,mirror(begin),mirror(args[1]),mirror(args[0])))
                elif kind=='A': left.append((kind,mirror(begin),*args))
                else:left.append((kind,mirror(begin)))
            if closed:path(name,start,right+left,True)
            else:path(name,mirror(here),left+right)
        line=self.add_line
        dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)

        self.add_polyline('shelf',(6,30),(10,30),(20,30),(28,30),(36,30),(42,30),(42,38),(36,38),(12,38),(6,38),closed=True)
        path('tall',(28,30),[('L',(28,10)),('A',(36,10),4,4,True),('L',(36,30))]);join('tall','shelf')
        path('short',(10,30),[('L',(6,18)),('C',(16,14),(6,13),(13,11)),('L',(20,30))]);join('short','shelf')
        for x in (12,36):line(f'foot-{x}',(x,38),(x,42));join(f'foot-{x}','shelf')
