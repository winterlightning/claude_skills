"""Feedback names the burger. The rejected burger has a narrow stacked-bead silhouette and obscures the drink. Restore a wide domed bun, a visible filling band and a lower bun beside the tapered cup and long straw.
Symbol plan: shared dimensions and symmetry for paired parts; coherent contours and explicit real junctions.
Construction reference: sandwich.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='5d4383cc-7fa3-4af5-b119-dc3b67d08db0'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__burger-beside-drink-cup/20260928T171322Z-thuan-mac/reference/fast food burger drink_5d4383cc-7fa3-4af5-b119-dc3b67d08db0.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    exception = {'reason': 'Preserve the broad burger bun, filling band and lower bun beside the drink. The burger bands have deliberate 2px clear openings and remain distinct at native size; the entire composition stays within the canvas. User explicitly delegated exception decisions for UI/UX quality; reviewed at 48px in light and dark.', 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '9cf9e1c2fe9820303bf6b52da62e7f6f6609b32eb60b621d3c88688c08b314e4'}
    icon_id='burger-beside-drink-cup'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('fast', 'food', 'burger', 'drink')
    def build(self):
        path=self.path;circle=self.circle;box=self.box;line=self.add_line;poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('cup',(23,20),[('L',(24,14)),('L',(16,14)),('L',(4,14)),('L',(7,41)),('C',(10,44),(7,43),(8,44)),('L',(16,44))])
        poly('straw',(13,29),(16,14),(18,4),(26,4));join('straw','cup')
        path('burger',(22,31),[('A',(28,25),6,True),('L',(38,25)),('A',(44,31),6,True),('L',(44,37)),('A',(38,43),6,True),('L',(28,43)),('A',(22,37),6,True),('L',(22,31))],True)
        for n,y in [('bun-edge',31),('filling-edge',37)]:line(n,(22,y),(44,y));join(n,'burger')


    def path(self,n,start,commands,closed=False):
        ids=[]
        for i,c in enumerate(commands):
            ident=f'{n}-{i}';k,end,*a=c
            if k=='L':self.add_line(ident,start,end)
            elif k=='A':self.add_arc(ident,start,end,radius_x=a[0],sweep=a[1])
            elif k=='E':self.add_arc(ident,start,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
            elif k=='C':self.add_bezier(ident,start,(a[0],a[1],end))
            ids.append(ident);start=end
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x,y-r),[('A',(x+r,y),r,True),('A',(x,y+r),r,True),('A',(x-r,y),r,True),('A',(x,y-r),r,True)],True)
    def box(self,n,l,t,r,b,q):
        self.path(n,(l+q,t),[('L',(r-q,t)),('A',(r,t+q),q,True),('L',(r,b-q)),('A',(r-q,b),q,True),('L',(l+q,b)),('A',(l,b-q),q,True),('L',(l,t+q)),('A',(l+q,t),q,True)],True)

