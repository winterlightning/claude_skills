"""envelope-and-document-letter-batch-008-08: Rectangular envelope with an emerging folded-corner letter, one address line, and detached stamp; all contact points explicit.
Lucide construction: mail; original and atomic-debug inspected.
Omissions: Second address line and letter text omitted for spacing; square postal stamp retained.
Keyshape SQUARE: exact contract envelope; 4-unit stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '666300f8-51fb-417d-a15c-04ca5345354f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/emails/read email letter_666300f8-51fb-417d-a15c-04ca5345354f.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'envelope-and-document-letter-batch-008-08'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'emails'
    categories = ('emails', 'primitives')
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

        poly('envelope',(6,18),(12,18),(36,18),(42,18),(42,42),(6,42),closed=True)
        poly('letter',(12,18),(12,6),(28,6),(36,14),(36,18));join('letter','envelope')
        line('address',(14,30),(18,30))
        poly('stamp',(26,26),(34,26),(34,34),(26,34),closed=True)
