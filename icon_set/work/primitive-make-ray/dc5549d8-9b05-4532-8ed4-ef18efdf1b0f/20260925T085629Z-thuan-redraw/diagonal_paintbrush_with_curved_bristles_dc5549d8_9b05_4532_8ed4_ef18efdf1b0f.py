"""Round the handle tip, taper the neck and make the bristle tuft flow smoothly into its pointed tip.
Symbol plan: Each outline owns its smooth contour. Shared endpoints connect attached parts.
Lucide construction: paintbrush. Original source establishes full subject and arrangement.
Keyshape: SQUARE; preserve natural source proportions where a documented exception is needed.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'dc5549d8-9b05-4532-8ed4-ef18efdf1b0f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__diagonal-paintbrush-with-curved-bristles/20260925T085629Z-thuan-mac/reference/brush_dc5549d8-9b05-4532-8ed4-ef18efdf1b0f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'diagonal-paintbrush-with-curved-bristles'
    keyshape = Keyshape.SQUARE
    exception = {'reason': 'Preserve the slender tapered handle and broad pointed bristle tuft. Handle interior clearance remains approximately three pixels at native size. Reviewed in light and dark at 48px. User explicitly authorized case-specific exceptions for UI/UX quality.', 'approved_by': 'user-directed-gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': '0ed2fa59b1b765391925c5ae08cef26b1cea386a4eb7e83e3805d27f2713ca93'}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('diagonal', 'paintbrush', 'with', 'curved', 'bristles')
    def build(self):

        self.path('outline',(6,42),[('C',(12,28),(10,39),(10,31)),('C',(20,25),(14,23),(17,23)),('L',(35,7)),('C',(38,6),(36,6),(37,6)),('C',(42,10),(40,6),(42,8)),('C',(41,13),(42,11),(42,12)),('L',(25,30)),('C',(6,42),(29,39),(18,42))],True)
        self.add_line('joint',(20,25),(25,30));self.relate('connect','joint','outline')


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

