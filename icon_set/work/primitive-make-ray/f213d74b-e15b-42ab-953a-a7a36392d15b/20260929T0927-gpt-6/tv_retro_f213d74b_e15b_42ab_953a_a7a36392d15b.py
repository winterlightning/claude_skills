from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'f213d74b-e15b-42ab-953a-a7a36392d15b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__tv-retro/20260929T090755Z-thuan-mac/reference/tv retro_f213d74b-e15b-42ab-953a-a7a36392d15b.svg'
AUTHOR = "gpt-6"
# Plan: Restore a large inset screen, paired tuning knobs, aerial and feet.
# Keyshape: SQUARE; preserve reference arrangement.
# Construction reference: tv.

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
    icon_id = 'tv-retro'
    keyshape = Keyshape.SQUARE
    exception = {'reason': 'Preserve a large retro television screen with two separate knobs and feet; clean 2px internal ink gaps are intentional.', 'approved_by': 'user-authorized visual judgment by gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'aebd85708b2ef12a50a883338f60fb5ed1fb6fe6e4121f51d860a29a1f7ab48c'}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()

    def build(self):
        _draw(self, 'cabinet', 'M 10 14 L 38 14 A 4 4 1 42 18 L 42 34 A 4 4 1 38 38 L 10 38 A 4 4 1 6 34 L 6 18 A 4 4 1 10 14 Z')
        _draw(self, 'screen', 'M 14 20 L 28 20 A 2 2 1 30 22 L 30 30 A 2 2 1 28 32 L 14 32 A 2 2 1 12 30 L 12 22 A 2 2 1 14 20 Z')
        _draw(self, 'knob-top', 'M 36 22 L 36 22')
        _draw(self, 'knob-bottom', 'M 36 30 L 36 30')
        _draw(self, 'antenna', 'M 16 6 L 24 14 L 32 6')
        _draw(self, 'foot-left', 'M 12 38 L 12 42')
        _draw(self, 'foot-right', 'M 36 38 L 36 42')
        owners = {member: contour.contour_id for contour in self.contours for member in contour.members}
        for a_index,a in enumerate(self.primitives):
            for b in self.primitives[a_index+1:]:
                if owners.get(a.element_id)!=owners.get(b.element_id) and ({a.start,a.end}&{b.start,b.end}):
                    self.relate("connect",a.element_id,b.element_id)
