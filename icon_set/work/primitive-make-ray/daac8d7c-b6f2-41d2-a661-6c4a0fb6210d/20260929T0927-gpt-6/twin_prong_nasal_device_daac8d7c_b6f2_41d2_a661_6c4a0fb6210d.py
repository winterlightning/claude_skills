from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'daac8d7c-b6f2-41d2-a661-6c4a0fb6210d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__twin-prong-nasal-device/20260929T090755Z-thuan-mac/reference/anti snorting device_daac8d7c-b6f2-41d2-a661-6c4a0fb6210d.svg'
AUTHOR = "gpt-6"
# Plan: Restore two outward-angled soft prongs above a shallow curved bridge and lower shell.
# Keyshape: HRECT_L; preserve reference arrangement.
# Construction reference: none.

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
    icon_id = 'twin-prong-nasal-device'
    keyshape = Keyshape.HRECT_L
    exception = {'reason': 'Preserve outward-angled nasal inserts and sculpted bridge; openings are distinct with approximately 3px ink gaps.', 'approved_by': 'user-authorized visual judgment by gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'a026cecdbe99657b852666c16e9ff6867ae9094458d451277ffba0368909834b'}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()

    def build(self):
        _draw(self, 'left-prong', 'M 11 24 L 14 10 C 15 7 21 8 21 11 L 18 25')
        _draw(self, 'right-prong', 'M 30 25 L 27 11 C 27 8 33 7 34 10 L 37 24')
        _draw(self, 'shell', 'M 4 24 C 4 20 10 23 15 24 C 20 26 28 26 33 24 C 38 23 44 20 44 24 C 44 34 35 40 24 40 C 13 40 4 34 4 24 Z')
        _draw(self, 'seam', 'M 10 35 C 19 29 29 29 38 35')
        owners = {member: contour.contour_id for contour in self.contours for member in contour.members}
        for a_index,a in enumerate(self.primitives):
            for b in self.primitives[a_index+1:]:
                if owners.get(a.element_id)!=owners.get(b.element_id) and ({a.start,a.end}&{b.start,b.end}):
                    self.relate("connect",a.element_id,b.element_id)
