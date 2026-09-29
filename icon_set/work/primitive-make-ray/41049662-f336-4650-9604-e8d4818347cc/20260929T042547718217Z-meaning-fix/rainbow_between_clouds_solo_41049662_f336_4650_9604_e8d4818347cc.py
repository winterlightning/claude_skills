"""Restore three concentric rainbow bands and two opposing soft cloud ends; shared center and mirrored cloud geometry.
Reference comparison: The rejected rainbow had two bands and heavy cloud junctions. The reference and feedback require a three-band rainbow between two clouds.
Construction references: Lucide rainbow: repeated concentric semicircles with shared center.
Omissions: Cloud outer ends remain open at the composition edges as in the supplied reference.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '41049662-f336-4650-9604-e8d4818347cc'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__rainbow-between-clouds-solo/20260929T042221Z-thuan-mac/reference/weather clouds rainbow_41049662-f336-4650-9604-e8d4818347cc.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'rainbow-between-clouds-solo'
    keyshape = Keyshape.HRECT_L
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
        # Concentric upper arcs share center (24,30); three bands preserve rainbow identity.
        for name,r in [('outer',20),('middle',13),('inner',6)]:
            self.add_arc(name,(24-r,30),(24+r,30),radius_x=r,sweep=True)
        self.path('left-cloud',(4,29),('A',(13,32),8,8,True),('A',(13,42),5,5,True),('L',(4,42)))
        self.path('right-cloud',(44,29),('A',(35,32),8,8,False),('A',(35,42),5,5,False),('L',(44,42)))

Drawing.exception = {'reason': 'Three 4px rainbow bands use 7-unit centerline pitch (3px visible separation). Compact cloud contacts and natural lower envelope are visually accepted to retain all reference bands.', 'approved_by': 'user', 'approved_on': '2026-09-29', 'svg_sha256': 'b0b6b574a5929547fb989faa7649d0e633f24f3736dbab00e1186fc805de3c79'}
