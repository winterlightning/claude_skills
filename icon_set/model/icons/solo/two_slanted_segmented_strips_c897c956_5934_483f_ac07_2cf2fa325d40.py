"""Two slanted segmented strips with a shared near-vertical divider pattern and separated rails. Lucide clapperboard informed the stripe rhythm. Ends remain open as in the source; no enclosure invented."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c897c956-5934-483f-ac07-2cf2fa325d40'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/scene_c897c956-5934-483f-ac07-2cf2fa325d40.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-slanted-segmented-strips'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'crime'
    categories = ('crime', 'primitives')
    aliases = ()
    keywords = ('two', 'slanted', 'segmented', 'strips')

    def build(self):
        # Plan: Two slanted segmented strips with a shared near-vertical divider pattern and separated rails. Lucide clapperboard informed the stripe rhythm. Ends remain open as in the source; no enclosure invented.
        def path(n, start, steps, closed=False):
            p=start; ids=[]
            for i,s in enumerate(steps):
                name=f'{n}-{i}'; kind,end,*args=s
                if kind=='L': self.add_line(name,p,end)
                elif kind=='A': self.add_arc(name,p,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(name,p,(args[0],args[1],end))
                ids.append(name); p=end
            self.add_contour(n,*ids,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        line=self.add_line; poly=self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        for name,top,bottom in [('upper',[(4,10),(18,9),(32,8),(44,8)],[(4,20),(14,19),(28,18),(44,18)]),('lower',[(4,28),(18,29),(32,30),(44,32)],[(4,38),(14,39),(28,40),(44,40)])]:
            poly(name+'-top',*top);poly(name+'-bottom',*bottom)
            for j in [1,2]:
                line(f'{name}-divider-{j}',top[j],bottom[j]);join(f'{name}-divider-{j}',name+'-top');join(f'{name}-divider-{j}',name+'-bottom')
