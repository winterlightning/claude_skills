from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '27baa2fe-8381-4b9b-bb3a-d74e46fadb00'
SOURCE_PATH = 'icon_set/work/todo-references/spotify logo 1_27baa2fe-8381-4b9b-bb3a-d74e46fadb00.svg'
AUTHOR = 'gpt-6'
# Plan: Spotify circular logo with three progressively shorter curved broadcast lines.
# References: No exact local Lucide logo match; supplied reference owns the three nested curves.
# Reduction: No defining parts omitted.

class AuthoredIcon(Solo48):
    icon_id = 'spotify-logo-1'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ()
    keywords = ('spotify', 'logo', '1')

    def build(self):
        self.circle('badge',24,24,20)
        self.add_bezier('upper',(15,17),((21,15),(27,15),(33,17)))
        self.add_bezier('middle',(16,25),((22,24),(26,24),(32,25)))
        self.add_bezier('lower',(18,34),((22,33),(26,33),(30,34)))

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,l,t,r,b,q=3):
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q)]
        ids=[]
        for k in range(8):
            ident=f'{n}-{k}';ids.append(ident)
            if k%2:self.add_arc(ident,pts[k],pts[(k+1)%8],radius_x=q)
            else:self.add_line(ident,pts[k],pts[(k+1)%8])
        self.add_contour(n,*ids,closed=True)
