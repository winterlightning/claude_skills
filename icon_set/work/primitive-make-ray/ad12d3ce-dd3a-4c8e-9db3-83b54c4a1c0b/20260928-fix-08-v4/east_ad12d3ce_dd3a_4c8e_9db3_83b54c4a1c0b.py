"""Rejected E is displaced left and the needle merges with the rim. Center E below the dial and restore an independent northeast compass pointer.
Symbol plan: coherent paths; repeated parts share parameters; actual attachments share nodes.
Lucide construction reference: compass. Source determines semantic arrangement.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ad12d3ce-dd3a-4c8e-9db3-83b54c4a1c0b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__east/20260928T165531Z-thuan-mac/reference/east_ad12d3ce-dd3a-4c8e-9db3-83b54c4a1c0b.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    exception = {'reason': 'Keep the compass and centered E in the original vertical arrangement. The E has readable 1px inter-bar gaps and the independent triangular pointer remains separated from the rim; the upright natural envelope is retained. User explicitly delegated exception decisions for UI/UX quality; reviewed at 48px in light and dark.', 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '4871e0bc2a7968c58e5abef66485252f24ef0f95da0c7b88765074a982828a69'}
    icon_id = 'east'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('east',)
    def build(self):
        line=self.add_line;poly=self.add_polyline;path=self.path;circle=self.circle
        join=lambda a,b:self.relate('connect',a,b)

        circle('dial',24,16,13)
        poly('needle',(18,16),(29,11),(25,23),closed=True)
        poly('e',(29,35),(19,35),(19,40),(19,45),(29,45))
        line('e-middle',(19,40),(27,40));join('e','e-middle')


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

