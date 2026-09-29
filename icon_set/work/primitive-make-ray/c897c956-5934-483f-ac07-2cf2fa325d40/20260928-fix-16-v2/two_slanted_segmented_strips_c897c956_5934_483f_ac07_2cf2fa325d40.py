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


        rails={
            'upper-top':[(4,13),(16,10),(28,7),(40,4)],
            'upper-bottom':[(4,21),(12,19),(24,16),(40,12)],
            'lower-top':[(4,27),(16,30),(28,33),(40,36)],
            'lower-bottom':[(4,35),(12,37),(24,40),(40,44)]}
        for n,pts in rails.items():poly(n,*pts)
        for i in range(2):
            for band,y,dy in [('upper',10,-3),('lower',30,3)]:
                n=band+'-divider-'+str(i)
                line(n,(16+12*i,y+dy*i),(12+12*i,(19 if band=='upper' else 37)+dy*i))
                join(n,band+'-top');join(n,band+'-bottom')

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

