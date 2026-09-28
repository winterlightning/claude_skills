"""Restore a tapered rounded handle with a distinct broad ferrule and flowing bristle tuft.
Symbol plan: Each outline owns its smooth contour. Shared endpoints connect attached parts.
Lucide construction: paintbrush. Original source establishes full subject and arrangement.
Keyshape: SQUARE; preserve natural source proportions where a documented exception is needed.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '68c9a911-9c9b-57a2-b9c1-85dc1f98044d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__diagonal-paintbrush-with-ferrule-band/20260925T085629Z-thuan-mac/reference/color brush_68c9a911-9c9b-57a2-b9c1-85dc1f98044d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'diagonal-paintbrush-with-ferrule-band'
    keyshape = Keyshape.SQUARE
    exception = {'reason': 'Preserve the slender handle and distinct ferrule. Approximately three-pixel handle opening and locally reduced ferrule separation remain clear in both themes. Reviewed in light and dark at 48px. User explicitly authorized case-specific exceptions for UI/UX quality.', 'approved_by': 'user-directed-gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': '12408fedc260b926505faf533c18323baf5408707c3cf26a812bb4391d4123dc'}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('diagonal', 'paintbrush', 'with', 'ferrule', 'band')
    def build(self):

        self.path('outline',(6,42),[('C',(12,28),(10,39),(10,31)),('C',(20,25),(14,23),(17,23)),('L',(25,19)),('L',(35,7)),('C',(38,6),(36,6),(37,6)),('C',(42,10),(40,6),(42,8)),('C',(41,13),(42,11),(42,12)),('L',(30,24)),('L',(25,30)),('C',(6,42),(29,39),(18,42))],True)
        self.add_line('joint',(20,25),(25,30));self.relate('connect','joint','outline')
        self.add_line('ferrule',(25,19),(30,24));self.relate('connect','ferrule','outline')


    def path(self, name, start, commands, closed=False):
        members=[]
        for i, (kind,end,*args) in enumerate(commands):
            tag=f'{name}-{i}'
            if kind=='L': self.add_line(tag,start,end)
            elif kind=='C': self.add_bezier(tag,start,(args[0],args[1],end))
            else: self.add_arc(tag,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            start=end;members.append(tag)
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.path(name,(x,y-r),[('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True)],True)

    def box(self,name,l,t,r,b,k):
        self.path(name,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)

