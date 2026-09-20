'Pocket Wallet with Snap Button.\nPlan: Rounded wallet with exposed angled card and projecting snap tab. Bounds4,8..44,40.\nConstruction reference: Lucide wallet rounded body and projecting tab; diagonal card from source.\nReduction: Omit tiny snap dot and wallet edges hidden behind card/tab.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '114ddaa5-c570-4bb4-b10e-88469985798b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/wallet_114ddaa5-c570-4bb4-b10e-88469985798b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'wallet-with-snap-tab'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('wallet', 'with', 'snap', 'tab')

    def build(self):

        def path(name, start, steps, closed=False):
            members, point = [], start
            for index, step in enumerate(steps):
                member = f"{name}-{index}"
                if len(step) == 2:
                    self.add_line(member, point, step)
                    point = step
                else:
                    end, rx, ry, sweep = step
                    self.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
                    point = end
                members.append(member)
            self.add_contour(name, *members, closed=closed)

        def ellipse(name, x, y, rx, ry):
            path(name, (x-rx,y), [((x+rx,y),rx,ry,True), ((x-rx,y),rx,ry,True)], True)

        def circle(name, x, y, radius):
            ellipse(name,x,y,radius,radius)

        def box(name, left, top, right, bottom, radius=4):
            r = radius
            path(name, (left+r,top), [(right-r,top), ((right,top+r),r,r,True),
                 (right,bottom-r), ((right-r,bottom),r,r,True), (left+r,bottom),
                 ((left,bottom-r),r,r,True), (left,top+r), ((left+r,top),r,r,True)], True)

        path('wallet-right',(40,24),[(40,20),((36,16),4,4,False)])
        path('wallet',(12,16),[(8,16),((4,20),4,4,False),(4,36),((8,40),4,4,False),(36,40),((40,36),4,4,False),(40,32)])
        path('card',(12,16),[(30,8),((36,14),6,6,True),(36,16)])
        self.relate('connect','card','wallet');self.relate('connect','card','wallet-right')
        path('tab',(40,24),[(34,24),((34,32),4,4,False),(44,32),(44,24),(40,24)],True)
        self.relate('connect','tab','wallet');self.relate('connect','tab','wallet-right')
