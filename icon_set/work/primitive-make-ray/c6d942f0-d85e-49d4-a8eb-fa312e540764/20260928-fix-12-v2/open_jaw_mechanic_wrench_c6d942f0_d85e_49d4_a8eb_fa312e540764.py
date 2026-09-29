"""Rejected wrench has a cramped jaw, kinked neck and abrupt jaw-to-handle corner. Rebuild continuous rounded head and parallel handle with a clear diagonal jaw opening.
Symbol plan: coherent paths; repeated parts share parameters; actual attachments share nodes.
Lucide construction reference: wrench. Source determines semantic arrangement.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'c6d942f0-d85e-49d4-a8eb-fa312e540764'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__open-jaw-mechanic-wrench/20260928T165531Z-thuan-mac/reference/pipe wrench_c6d942f0-d85e-49d4-a8eb-fa312e540764.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'open-jaw-mechanic-wrench'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('pipe', 'wrench')
    def build(self):
        line=self.add_line;poly=self.add_polyline;path=self.path;circle=self.circle
        join=lambda a,b:self.relate('connect',a,b)

        path('wrench',(7,34),[('L',(20,21)),('C',(20,15),(22,19),(20,18)),('A',(32,3),12,True),('A',(44,15),12,True),('L',(44,17)),('L',(35,12)),('L',(29,18)),('L',(36,25)),('C',(29,28),(34,27),(31,28)),('C',(25,30),(27,28),(27,28)),('L',(14,41)),('A',(7,34),5,True)],closed=True)


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

