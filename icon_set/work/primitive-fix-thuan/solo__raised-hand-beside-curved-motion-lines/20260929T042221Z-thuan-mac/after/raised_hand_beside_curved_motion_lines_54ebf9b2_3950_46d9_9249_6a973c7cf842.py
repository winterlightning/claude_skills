"""Restore a continuous four-finger hand with opposing thumb and wrist, beside two broad nested motion arcs; intentional right-weighted composition.
Reference comparison: The rejected hand was broken at the wrist, had only two clear fingers and tiny partial motion curves. Feedback asks to recover the raised hand beside curved motion lines.
Construction references: Lucide hand: digit hierarchy and continuous palm. Original controls left-side motion arcs.
Omissions: No defining features omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '54ebf9b2-3950-46d9-9249-6a973c7cf842'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__raised-hand-beside-curved-motion-lines/20260929T042221Z-thuan-mac/reference/massage point_54ebf9b2-3950-46d9-9249-6a973c7cf842.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'raised-hand-beside-curved-motion-lines'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()

    def path(self, name, start, *steps, closed=False):
        ids=[]; p=start
        for n,step in enumerate(steps):
            key=f"{name}-{n}"; end=step[1]
            if step[0]=='L': self.add_line(key,p,end)
            else: self.add_arc(key,p,end,radius_x=step[2],radius_y=step[3],sweep=step[4],large_arc=step[5] if len(step)>5 else False)
            ids.append(key);p=end
        if closed and p!=start:
            key=f"{name}-close";self.add_line(key,p,start);ids.append(key)
        self.add_contour(name,*ids,closed=closed)
    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True),closed=True)

    def build(self):
        self.path('hand',(23,29),('L',(23,12)),('A',(29,12),3,3,True),('L',(29,8)),('A',(35,8),3,3,True),('L',(35,12)),('A',(41,12),3,3,True),('L',(41,17)),('A',(46,17),3,3,True),('L',(46,29)),('A',(41,39),13,13,True),('L',(41,44)),('L',(29,44)),('L',(29,40)),('L',(17,28)),('A',(22,23),4,4,True),('L',(23,29)),closed=True)
        for x,y in [(29,12),(35,12),(41,17)]:
            self.add_line(f'finger-{x}',(x,y),(x,25));self.relate('connect','hand',f'finger-{x}')
        self.add_arc('motion-outer',(14,8),(8,35),16,16,False) if False else None
        self.add_arc('motion-outer',(14,8),(8,35),radius_x=16,radius_y=16,sweep=False)
        self.add_arc('motion-inner',(14,17),(12,28),radius_x=7,radius_y=7,sweep=False)

Drawing.exception = {'reason': 'Full hand plus motion arcs requires anatomical 6-unit finger pitch and narrow local gaps. The 48px silhouette and 4px strokes remain intact; user authorized visual exception.', 'approved_by': 'user', 'approved_on': '2026-09-29', 'svg_sha256': '55c8f9aecf955a278a846fb463537feb9c9510e4f6e26527843e5346b64b3e62'}
