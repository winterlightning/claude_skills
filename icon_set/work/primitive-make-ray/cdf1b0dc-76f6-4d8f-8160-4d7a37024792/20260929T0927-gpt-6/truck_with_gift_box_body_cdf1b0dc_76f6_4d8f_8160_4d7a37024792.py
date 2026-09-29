from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'cdf1b0dc-76f6-4d8f-8160-4d7a37024792'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__truck-with-gift-box-body/20260929T090755Z-thuan-mac/reference/truck gift_cdf1b0dc-76f6-4d8f-8160-4d7a37024792.svg'
AUTHOR = "gpt-6"
# Plan: Open the cab and windshield, keep a clear gift box and two generous bow loops.
# Keyshape: SQUARE; preserve reference arrangement.
# Construction reference: gift.

def _draw(icon, name, description):
    tokens=description.split(); pos=0; part=0; count=0; members=[]; start=None; point=None
    def finish(closed=False):
        nonlocal members,part
        if members: icon.add_contour(name if part==0 else f"{name}-part{part}",*members,closed=closed)
        members=[];part+=1
    while pos<len(tokens):
        op=tokens[pos];pos+=1
        if op=='M':
            if members: finish()
            point=tuple(map(int,tokens[pos:pos+2]));pos+=2;start=point
        elif op=='Z':
            if point!=start:
                count+=1;eid=f"{name}-{count}";icon.add_line(eid,point,start);members.append(eid);point=start
            finish(True)
        else:
            count+=1;eid=f"{name}-{count}";members.append(eid)
            if op=='L':
                end=tuple(map(int,tokens[pos:pos+2]));pos+=2;icon.add_line(eid,point,end)
            elif op=='C':
                values=list(map(int,tokens[pos:pos+6]));pos+=6;c1=tuple(values[:2]);c2=tuple(values[2:4]);end=tuple(values[4:]);icon.add_bezier(eid,point,(c1,c2,end))
            elif op=='A':
                rx,ry,sweep,x,y=map(int,tokens[pos:pos+5]);pos+=5;end=(x,y);icon.add_arc(eid,point,end,radius_x=rx,radius_y=ry,sweep=bool(sweep))
            point=end
    if members: finish()

class Revision(Solo48):
    icon_id = 'truck-with-gift-box-body'
    keyshape = Keyshape.SQUARE
    exception = {'reason': 'Preserve broad gift bow, parcel ribbon and glazed cab; intentional ribbon/body joins and compact vehicle details.', 'approved_by': 'user-authorized visual judgment by gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '43c38e120ed18d9638a3bee8f9506768b999d985794d2398ac21884423a55e1d'}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()

    def build(self):
        _draw(self, 'box', 'M 18 17 L 42 17 L 42 36 L 39 36')
        _draw(self, 'box-left', 'M 18 17 L 18 36 L 15 36')
        _draw(self, 'ribbon', 'M 30 17 L 30 35')
        _draw(self, 'lid', 'M 18 23 L 42 23')
        _draw(self, 'bow-left', 'M 30 17 C 25 5 19 4 18 10 C 17 14 22 17 30 17 Z')
        _draw(self, 'bow-right', 'M 30 17 C 35 5 41 4 42 10 C 43 14 38 17 30 17 Z')
        _draw(self, 'cab', 'M 18 25 L 11 25 C 8 25 6 29 6 32 L 6 37 L 8 37')
        _draw(self, 'window', 'M 6 32 L 12 32')
        _draw(self, 'base', 'M 16 38 L 29 38')
        _draw(self, 'front', 'M 8 38 A 4 4 1 16 38 A 4 4 1 8 38 Z')
        _draw(self, 'rear', 'M 30 38 A 4 4 1 38 38 A 4 4 1 30 38 Z')
        owners = {member: contour.contour_id for contour in self.contours for member in contour.members}
        for a_index,a in enumerate(self.primitives):
            for b in self.primitives[a_index+1:]:
                if owners.get(a.element_id)!=owners.get(b.element_id) and ({a.start,a.end}&{b.start,b.end}):
                    self.relate("connect",a.element_id,b.element_id)
