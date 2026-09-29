"""Restore a complete symmetric handset with rounded earpieces above a softly tapered desk base and an enlarged round dial.
Reference comparison: The rejected phone reduced the handset to an open arc and the rotary dial to a small dot-like hole. The source shows a complete receiver with two earpieces and a broad circular dial.
Construction references: Lucide phone: rounded receiver ends and coherent handset contour; supplied rotary-phone reference owns desk base and dial.
Omissions: No defining features omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1ac72916-7ade-454e-ab5a-35dfc8365bf8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__round-dial-desk-telephone/20260929T051531Z-thuan-mac/reference/phone rotary_1ac72916-7ade-454e-ab5a-35dfc8365bf8.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'round-dial-desk-telephone'
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
            elif step[0]=='C': self.add_bezier(key,p,(step[2],step[3],end))
            else: self.add_arc(key,p,end,radius_x=step[2],radius_y=step[3],sweep=step[4],large_arc=step[5] if len(step)>5 else False)
            ids.append(key);p=end
        if closed and p!=start:
            key=f"{name}-close";self.add_line(key,p,start);ids.append(key)
        self.add_contour(name,*ids,closed=closed)
    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True),closed=True)

    def build(self):
        # Mirrored handset lobes sit on a wide desk-phone body.
        self.path('handset',(4,18),('C',(24,6),(3,8),(11,6)),('C',(44,18),(37,6),(45,8)),('A',(40,21),3,3,True),('L',(36,21)),('A',(33,18),3,3,True),('L',(33,16)),('A',(30,13),3,3,False),('L',(18,13)),('A',(15,16),3,3,False),('L',(15,18)),('A',(12,21),3,3,True),('L',(8,21)),('A',(4,18),4,3,True),closed=True)
        self.path('base',(17,21),('L',(31,21)),('C',(42,37),(35,24),(42,32)),('A',(37,42),5,5,True),('L',(11,42)),('A',(6,37),5,5,True),('C',(17,21),(6,32),(13,24)),closed=True)
        self.circle('rotary-dial',24,31,6)

Drawing.exception = {'reason': 'Complete handset earpieces and large rotary dial need compact openings and close body spacing. Native-size legibility is prioritized under the user-authorized visual exception.', 'approved_by': 'user', 'approved_on': '2026-09-29', 'svg_sha256': 'a928bcf3b5054257db909b730fccff70a45f24d8aabdc7712093317e00468926'}
