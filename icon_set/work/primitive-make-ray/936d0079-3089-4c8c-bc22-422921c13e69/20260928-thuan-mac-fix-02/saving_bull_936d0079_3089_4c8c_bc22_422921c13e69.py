"""One coherent body contour with integrated foreleg and hindleg; separate curved horn and rising trend arrow. Ink extremes (2,6)-(46,42).
Lucide piggy-bank: continuous animal outline with integrated legs. No exact local bull match; the original owns the horn, lowered head and arched back. Intentional natural asymmetry."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '936d0079-3089-4c8c-bc22-422921c13e69'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__saving-bull/20260928T175139Z-thuan-mac/reference/saving bull_936d0079-3089-4c8c-bc22-422921c13e69.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'saving-bull'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('saving', 'bull')

    exception = {'reason': 'User authorized visual exceptions for UI quality. Integrated outlined legs and lowered head retain their natural narrow channels, approximately 1.1–3px, preserving the left-facing bull silhouette and planted legs. Openings remain visible at 48px in both themes. The trend arrow shares a real body endpoint; all strokes 4px and no false connections.', 'approved_by': 'user: delegated visual-exception decision to gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'bbf5456cef4f99a6bbd187c568dcae4c84537556fa9ad75f5ae2b73203710de1'}

    def build(self):

        def curve(name,start,c1,c2,end):
            self.add_bezier(name,start,(c1,c2,end))
        def path(name,start,steps,closed=False):
            point=start
            ids=[]
            for j,(kind,end,*args) in enumerate(steps):
                part=f'{name}-{j}'
                if kind=='L': self.add_line(part,point,end)
                elif kind=='A': self.add_arc(part,point,end,radius_x=args[0],sweep=args[1])
                elif kind=='C': curve(part,point,args[0],args[1],end)
                ids.append(part)
                point=end
            self.add_contour(name,*ids,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,True),('A',(x-r,y),r,True)],True)

        path('body',(8,25),[
            ('C',(21,18),(13,21),(16,16)),
            ('C',(29,21),(25,18),(27,20)),
            ('C',(36,24),(31,22),(33,24)),
            ('A',(42,30),6,True),('L',(41,35)),('L',(39,40)),
            ('L',(33,40)),('L',(35,33)),('L',(24,33)),
            ('L',(19,40)),('L',(13,40)),('L',(17,32)),
            ('C',(12,29),(18,28),(14,26)),
            ('C',(8,36),(10,31),(11,36)),
            ('C',(4,31),(5,36),(4,34)),('L',(8,25))],True)
        curve('horn',(8,25),(8,21),(4,19),(4,17))
        self.relate('connect','horn','body')
        self.add_line('tail',(42,30),(44,38))
        self.relate('connect','tail','body')
        self.add_line('trend',(29,21),(42,8))
        self.relate('connect','trend','body')
        self.add_polyline('arrow',(34,8),(42,8),(42,16))
        self.relate('connect','trend','arrow')
