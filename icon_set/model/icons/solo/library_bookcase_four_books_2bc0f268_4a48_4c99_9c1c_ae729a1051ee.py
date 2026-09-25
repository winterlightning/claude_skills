"""Library Bookshelf with Books.

Library case with two upright books on the upper-right and two on the lower-left. Centerline extremes (4,8)-(44,40). Lucide book-open informs shared book boundaries. Keep four books and their alternating placement; omit small spine marks.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2bc0f268-4a48-4c99-9c1c-ae729a1051ee'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/shelf books_2bc0f268-4a48-4c99-9c1c-ae729a1051ee.svg'
AUTHOR = 'gpt-6'

class LibraryBookcaseFourBooks(Solo48):
    icon_id = 'library-bookcase-four-books'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    categories = ('furnitures', 'primitives')
    aliases = ()
    keywords = ('library', 'bookshelf', 'with', 'books')

    def build(self):
        # Symbol plan: Library case with two upright books on the upper-right and two on the lower-left. Centerline extremes (4,8)-(44,40). Lucide book-open informs shared book boundaries. Keep four books and their alternating placement; omit small spine marks.

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

        self.add_polyline('case',(4,8),(44,8),(44,24),(44,40),(36,40),(28,40),(26,40),(20,40),(16,40),(12,40),(4,40),(4,24),closed=True)
        self.add_polyline('shelf',(4,24),(12,24),(20,24),(28,24),(36,24),(44,24));join('shelf','case')
        if False:
            self.add_polyline('upper-books',(12,24),(12,16),(20,16),(28,16),(28,24));line('upper-spine',(20,16),(20,24));join('upper-books','shelf');join('upper-spine','shelf');join('upper-spine','upper-books')
            self.add_polyline('lower-books',(16,40),(12,32),(22,32),(32,32),(36,40));line('lower-spine',(22,32),(26,40));join('lower-books','case');join('lower-spine','case');join('lower-spine','lower-books')
        else:
            self.add_polyline('upper-books',(20,24),(20,16),(28,16),(36,16),(36,24));line('upper-spine',(28,16),(28,24));join('upper-books','shelf');join('upper-spine','shelf');join('upper-spine','upper-books')
            self.add_polyline('lower-books',(12,40),(12,32),(20,32),(28,32),(28,40));line('lower-spine',(20,32),(20,40));join('lower-books','case');join('lower-spine','case');join('lower-spine','lower-books')
