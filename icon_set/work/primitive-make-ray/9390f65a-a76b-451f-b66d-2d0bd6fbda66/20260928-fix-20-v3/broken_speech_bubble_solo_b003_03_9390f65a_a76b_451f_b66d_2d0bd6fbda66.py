"""Feedback explicitly says line not connected. Rejected bubble has two disconnected crack ends and a broken tail. Restore one continuous perimeter with a joined lightning-shaped crack and connected speech tail.
Symbol plan: coherent paths; repeated parts share parameters; actual attachments share nodes.
Lucide construction reference: message-square. Source determines semantic arrangement.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '9390f65a-a76b-451f-b66d-2d0bd6fbda66'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__broken-speech-bubble-solo-b003-03/20260928T165531Z-thuan-mac/reference/language barrier broken bubble_9390f65a-a76b-451f-b66d-2d0bd6fbda66.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    exception = {'reason': 'The closed speech-bubble perimeter and connected lightning crack satisfy the explicit connection feedback. Keep the intentional 2.56px crack opening, visibly open in both themes. User explicitly delegated exception decisions for UI/UX quality; reviewed at 48px in light and dark.', 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '924f26c51792ea572047a2220717058dc14a7b815aca21fa97810ee6b47b32dc'}
    icon_id = 'broken-speech-bubble-solo-b003-03'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('language', 'barrier', 'broken', 'bubble')
    def build(self):
        line=self.add_line;poly=self.add_polyline;path=self.path;circle=self.circle
        join=lambda a,b:self.relate('connect',a,b)

        path('bubble',(18,6),[('L',(10,6)),('A',(6,10),4,False),('L',(6,32)),('A',(10,36),4,False),('L',(14,36)),('L',(14,42)),('L',(22,36)),('L',(38,36)),('A',(42,32),4,False),('L',(42,10)),('A',(38,6),4,False),('L',(29,6)),('L',(32,15)),('L',(28,18)),('L',(32,28)),('L',(20,18)),('L',(25,14)),('L',(18,6))],closed=True)


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

