"""Rejected strips have near-horizontal rails and inconsistent separators. Restore two distinctly slanted bands with parallel rails and consistently spaced diagonal dividers.
Symbol plan: coherent paths; repeated parts share parameters; actual attachments share nodes.
Lucide construction reference: clapperboard. Source determines semantic arrangement.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'c897c956-5934-483f-ac07-2cf2fa325d40'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__two-slanted-segmented-strips/20260928T165531Z-thuan-mac/reference/scene_c897c956-5934-483f-ac07-2cf2fa325d40.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'two-slanted-segmented-strips'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('scene',)
    def build(self):
        line=self.add_line;poly=self.add_polyline;path=self.path;circle=self.circle
        join=lambda a,b:self.relate('connect',a,b)

        for n,pts in [('upper-top',[(4,10),(16,8),(28,6),(40,4)]),('upper-bottom',[(4,22),(16,20),(28,18),(40,16)]),('lower-top',[(4,26),(16,29),(28,32),(40,35)]),('lower-bottom',[(4,35),(16,38),(28,41),(40,44)])]:
            poly(n,*pts)
        for i in range(2):
            x=16+12*i
            line('upper-divider-'+str(i),(x,8-2*i),(x-4,20-2*i+1))
            line('lower-divider-'+str(i),(x,29+3*i),(x-4,38+3*i-1))


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

