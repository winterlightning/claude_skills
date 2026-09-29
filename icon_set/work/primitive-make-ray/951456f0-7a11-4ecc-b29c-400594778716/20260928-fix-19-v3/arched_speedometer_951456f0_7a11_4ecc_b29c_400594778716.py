"""Rejected speedometer substitutes dots for ticks and shows few dial details. Restore radial tick strokes, open needle pivot and smooth domed housing.
Symbol plan: coherent paths; repeated parts share parameters; actual attachments share nodes.
Lucide construction reference: gauge. Source determines semantic arrangement.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '951456f0-7a11-4ecc-b29c-400594778716'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__arched-speedometer/20260928T165531Z-thuan-mac/reference/odometer_951456f0-7a11-4ecc-b29c-400594778716.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    exception = {'reason': 'Retain recognizable dial ticks and the separated needle/pivot within the arched housing. The smallest retained tick-to-rim gap is 2px; all marks remain distinct at native size. User explicitly delegated exception decisions for UI/UX quality; reviewed at 48px in light and dark.', 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '3a8052cfd5de70bcbe6111555df74b3e540c43802c49d03e75d9e012e1a7065a'}
    icon_id = 'arched-speedometer'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('odometer',)
    def build(self):
        line=self.add_line;poly=self.add_polyline;path=self.path;circle=self.circle
        join=lambda a,b:self.relate('connect',a,b)

        path('housing',(4,34),[('L',(4,28)),('A',(24,8),20,True),('A',(44,28),20,True),('L',(44,34)),('A',(38,40),6,True),('L',(10,40)),('A',(4,34),6,True)],closed=True)
        circle('pivot',24,29,3)
        line('needle',(27,29),(35,24));join('pivot','needle')
        for n,a,b in [('top',(24,14),(24,17)),('left',(11,26),(14,27)),('upper-left',(15,18),(17,21))]:line(n,a,b)


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

