"""The rejected cube has stubby, filled-looking corner marks and short central axes. Restore open isometric corner junctions and longer center Y.
Symbol plan: coherent paths; repeated parts share parameters; actual attachments share nodes.
Lucide construction reference: box. Source determines semantic arrangement.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e879424e-4424-5a55-9724-37f5338a9a78'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__ar-cube-axis-arrows/20260928T165531Z-thuan-mac/reference/tools ar kit_e879424e-4424-5a55-9724-37f5338a9a78.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    exception = {'reason': 'Preserve six open isometric corners and the central Y. A 40x44 ink envelope and 3.0–3.6px local gaps maintain legibility without shortening the cube into stubs. User explicitly delegated exception decisions for UI/UX quality; reviewed at 48px in light and dark.', 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '58d17d3231c0ed17ff4cebad25da0c2103f211ef737000e94be94294ac507544'}
    icon_id = 'ar-cube-axis-arrows'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('tools', 'ar', 'kit')
    def build(self):
        line=self.add_line;poly=self.add_polyline;path=self.path;circle=self.circle
        join=lambda a,b:self.relate('connect',a,b)

        poly('north', (18,8),(24,4),(30,8)); line('north-axis',(24,4),(24,11)); join('north','north-axis')
        poly('south',(18,40),(24,44),(30,40)); line('south-axis',(24,38),(24,44)); join('south','south-axis')
        poly('center',(18,21),(24,25),(30,21)); line('center-axis',(24,25),(24,31)); join('center','center-axis')
        for s in (-1,1):
            p=lambda x,y:(24+s*x,y)
            n='left' if s<0 else 'right'
            poly(n+'-upper',p(13,12),p(18,15),p(18,21))
            line(n+'-upper-axis',p(18,15),p(13,18));join(n+'-upper',n+'-upper-axis')
            poly(n+'-lower',p(18,29),p(18,35),p(13,38))
            line(n+'-lower-axis',p(18,35),p(13,32));join(n+'-lower',n+'-lower-axis')


    def path(self,n,start,commands,closed=False):
        ids=[]
        for i,c in enumerate(commands):
            ident=f'{n}-{i}';k,end,*a=c
            if k=='L':self.add_line(ident,start,end)
            elif k=='A':self.add_arc(ident,start,end,radius_x=a[0],sweep=a[1])
            elif k=='C':self.add_bezier(ident,start,(a[0],a[1],end))
            ids.append(ident);start=end
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x+r,y),r,True),('A',(x-r,y),r,True)],True)

