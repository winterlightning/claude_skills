from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '5fda1d00-7833-4fcb-89e8-8b235809140b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__truck-carrying-a-house/20260929T090755Z-thuan-mac/reference/real estate truck house_5fda1d00-7833-4fcb-89e8-8b235809140b.svg'
AUTHOR = "gpt-6"
# Plan: Separate a left-facing cab, flatbed and full house with open doorway.
# Keyshape: HRECT_L; preserve reference arrangement.
# Construction reference: truck.

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
    icon_id = 'truck-carrying-a-house'
    keyshape = Keyshape.HRECT_L
    exception = {'reason': 'The recognizable cab, open house doorway and flatbed need compact internal openings at 48px; visually distinct at native size.', 'approved_by': 'user-authorized visual judgment by gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'a68a65d4fdc82c429c83fd2758e11529e0345aee69c2c18b88a2e50706b8bb35'}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()

    def build(self):
        _draw(self, 'roof', 'M 18 18 L 31 8 L 44 18')
        _draw(self, 'house', 'M 20 17 L 20 29 L 42 29 L 42 17')
        _draw(self, 'door', 'M 27 29 L 27 24 A 4 4 1 35 24 L 35 29')
        _draw(self, 'cab', 'M 9 34 L 4 34 L 4 27 L 8 21 L 16 21 L 16 29')
        _draw(self, 'window', 'M 4 27 L 10 27')
        _draw(self, 'bed', 'M 16 29 L 44 29 L 44 34 L 39 34')
        _draw(self, 'axle', 'M 19 35 L 29 35')
        _draw(self, 'wheel-front', 'M 9 35 A 5 5 1 19 35 A 5 5 1 9 35 Z')
        _draw(self, 'wheel-rear', 'M 29 35 A 5 5 1 39 35 A 5 5 1 29 35 Z')
        owners = {member: contour.contour_id for contour in self.contours for member in contour.members}
        for a_index,a in enumerate(self.primitives):
            for b in self.primitives[a_index+1:]:
                if owners.get(a.element_id)!=owners.get(b.element_id) and ({a.start,a.end}&{b.start,b.end}):
                    self.relate("connect",a.element_id,b.element_id)
