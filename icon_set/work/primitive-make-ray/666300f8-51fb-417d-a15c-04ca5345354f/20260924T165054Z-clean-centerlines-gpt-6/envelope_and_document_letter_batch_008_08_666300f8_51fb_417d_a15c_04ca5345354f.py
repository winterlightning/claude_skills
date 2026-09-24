"""envelope-and-document-letter-batch-008-08: Rounded envelope with an emerging folded-corner letter, one address line, and detached stamp; all contact points explicit.
Lucide construction: mail; original and atomic-debug inspected.
Omissions: Second address line omitted; stamp reduced to a circular postal seal for legibility.
Keyshape SQUARE: exact contract envelope; 4-unit stroke.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '666300f8-51fb-417d-a15c-04ca5345354f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__envelope-and-document-letter-batch-008-08/20260924T165054Z-thuan-mac/reference/read email letter_666300f8-51fb-417d-a15c-04ca5345354f.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'envelope-and-document-letter-batch-008-08'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('envelope', 'and', 'document', 'letter', 'batch', '008', '08')
    def build(self):

        def path(name, start, commands, closed=False):
            members=[]
            for i,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,start,end)
                elif kind=='A': self.add_arc(ident,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,start,(args[0],args[1],end))
                members.append(ident);start=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx,cy-ry),[('A',(cx+rx,cy),rx,ry,True),('A',(cx,cy+ry),rx,ry,True),('A',(cx-rx,cy),rx,ry,True),('A',(cx,cy-ry),rx,ry,True)],True)
        def rect(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('envelope',(12,22),[('L',(36,22)),('L',(39,22)),('A',(42,25),3,3,True),('L',(42,39)),('A',(39,42),3,3,True),('L',(9,42)),('A',(6,39),3,3,True),('L',(6,25)),('A',(9,22),3,3,True),('L',(12,22))],True)
        poly('letter',(12,22),(12,6),(28,6),(36,14),(36,22));join('letter','envelope')
        line('letter-text',(20,14),(24,14));line('address',(15,32),(22,32))
        # A small circular seal keeps the stamp distinct at 48px.
        oval('stamp',34,32,2,2)
