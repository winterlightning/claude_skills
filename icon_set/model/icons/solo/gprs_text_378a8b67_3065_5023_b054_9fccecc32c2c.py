"""The capital letters GPRS sit together on a shared baseline. Rounded bowls shape the G, P, and R, while the final S curves in opposite directions at its upper and lower ends."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '378a8b67-3065-5023-b054-9fccecc32c2c'
SOURCE_PATH = 'pictographic-primitives/mobile/gprs_378a8b67-3065-5023-b054-9fccecc32c2c.svg'
AUTHOR = 'gpt-6'

class MobileIcon(Solo48):
    icon_id = 'gprs-text'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'mobile'
    aliases = ()
    keywords = ('gprs', 'text', 'cellular', 'network', 'mobile', 'letters', 'data')

    def build(self):
        # Lucide construction references: none.
        # Typed paths own continuous joins; repeated shapes share dimensions.
        def path(name, start, commands, closed=False):
            members, here = [], start
            for i, (kind, end, *args) in enumerate(commands):
                ident = f"{name}-{i}"
                if kind == 'L':
                    self.add_line(ident, here, end)
                elif kind == 'C':
                    self.add_bezier(ident, here, (args[0],args[1],end))
                else:
                    rx, ry, sweep = args
                    self.add_arc(ident, here, end, radius_x=rx, radius_y=ry, sweep=sweep)
                members.append(ident)
                here = end
            self.add_contour(name, *members, closed=closed)
        def rounded(name,x0,y0,x1,y1,r,split_y=None):
            right = [('L',(x1,split_y))] if split_y is not None else []
            left = [('L',(x0,split_y))] if split_y is not None else []
            path(name,(x0+r,y0),[
                ('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),
                *right,('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),
                ('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),
                *left,('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        # VRECT_L extremes (8,4)-(40,44). A 2x2 letter grid: 12x16 letters, eight-unit gutters.
        path('g',(20,4),[('L',(12,4)),('A',(8,8),4,4,False),('L',(8,16)),('A',(12,20),4,4,False),('L',(20,20)),('L',(20,12)),('L',(16,12))])
        # P and R share their bowl definition and attachment nodes.
        def bowl(name,x,y):
            path(name,(x,y+8),[('L',(x,y)),('L',(x+8,y)),('A',(x+12,y+4),4,4,True),('A',(x+8,y+8),4,4,True),('L',(x,y+8))],True)
            self.add_line(name+'-stem',(x,y+8),(x,y+16))
            self.relate('connect',name,name+'-stem')
        bowl('p',28,4)
        bowl('r',8,28)
        self.add_line('r-leg',(16,36),(20,44))
        self.relate('connect','r','r-leg')
        path('s',(40,28),[('L',(32,28)),('A',(28,32),4,4,False),('A',(32,36),4,4,False),('L',(36,36)),('A',(40,40),4,4,True),('A',(36,44),4,4,True),('L',(28,44))])
