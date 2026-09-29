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
        poly('south',(18,40),(24,44),(30,40)); line('south-axis',(24,37),(24,44)); join('south','south-axis')
        poly('center',(18,21),(24,25),(30,21)); line('center-axis',(24,25),(24,32)); join('center','center-axis')
        for s in (-1,1):
            p=lambda x,y:(24+s*x,y)
            n='left' if s<0 else 'right'
            poly(n+'-upper',p(10,12),p(16,16),p(16,23))
            line(n+'-upper-axis',p(16,16),p(10,20));join(n+'-upper',n+'-upper-axis')
            poly(n+'-lower',p(16,28),p(16,35),p(10,39))
            line(n+'-lower-axis',p(16,35),p(10,31));join(n+'-lower',n+'-lower-axis')


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

