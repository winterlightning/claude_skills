from pathlib import Path
import json,shutil
root=Path(__file__).parent;rows=json.loads((root/'batch.json').read_text())
AUTHOR='gpt-6'
SOURCE_ICON_ID=[r['source_uuid'] for r in rows]
SOURCE_PATH=[r['reference_path'] for r in rows]
for i,m in enumerate(rows,1):
    old=Path(m['result_dir']);rd=old.with_name(old.name.replace('-v1','-v2'));rd.mkdir(exist_ok=False)
    for p in old.glob('*.png'):
        if p.name in ('reference.png','before.png'):shutil.copyfile(p,rd/p.name)
    shutil.copyfile(old/'comparison.md',rd/'comparison.md')
    text=Path(m['module']).read_text()
    if i==1:
        text=text.replace("p(10,12),p(16,16),p(16,23)","p(13,12),p(18,15),p(18,21)").replace("p(16,16),p(10,20)","p(18,15),p(13,18)")
        text=text.replace("p(16,28),p(16,35),p(10,39)","p(18,29),p(18,35),p(13,38)").replace("p(16,35),p(10,31)","p(18,35),p(13,32)")
        text=text.replace("(24,37),(24,44)","(24,38),(24,44)").replace("(24,25),(24,32)","(24,25),(24,31)")
    if i==8:
        text=text.replace("circle('dial',24,18,14)","circle('dial',24,14,12)")
        text=text.replace("(20,18),(29,13),(26,24),(24,20)","(18,14),(29,9),(25,21)")
        text=text.replace("(28,36),(20,36),(20,40),(20,44),(28,44)","(28,32),(20,32),(20,38),(20,44),(28,44)").replace("(20,40),(26,40)","(20,38),(26,38)")
    if i in (10,11):
        text=text.replace("circle('source',9,9,5)","path('source',(13,12),[('A',(4,9),5,True),('A',(13,12),5,True)],closed=True)")
        text=text.replace("circle('upper-node',39,9,5)","path('upper-node',(43,12),[('A',(34,9),5,True),('A',(43,12),5,True)],closed=True)")
        text=text.replace("circle('lower-node',9,33,5)","path('lower-node',(12,37),[('A',(4,33),5,True),('A',(12,37),5,True)],closed=True)")
        text=text.replace("(13,13),(30,30)","(13,12),(30,29)").replace("(21,30),(30,30),(30,21)","(22,29),(30,29),(30,21)")
        text=text.replace("(47,18),(47,25)","(46,18),(46,25)")
    if i==12:
        text=text.replace("('L',(35,8)),('L',(27,16)),('L',(36,25))","('L',(35,12)),('L',(29,18)),('L',(36,25))")
    if i==16:
        a=text.index("        for n,pts in");b=text.index('\n    def path',a)
        text=text[:a]+'''
        rails={
            'upper-top':[(4,13),(16,10),(28,7),(40,4)],
            'upper-bottom':[(4,21),(12,19),(24,16),(40,12)],
            'lower-top':[(4,27),(16,30),(28,33),(40,36)],
            'lower-bottom':[(4,35),(12,37),(24,40),(40,44)]}
        for n,pts in rails.items():poly(n,*pts)
        for i in range(2):
            for band,y,dy in [('upper',10,-3),('lower',30,3)]:
                n=band+'-divider-'+str(i)
                line(n,(16+12*i,y+dy*i),(12+12*i,(19 if band=='upper' else 37)+dy*i))
                join(n,band+'-top');join(n,band+'-bottom')
''' + text[b:]
    if i==19:
        text=text.replace("circle('pivot',24,30,3)","circle('pivot',24,29,3)")
        text=text.replace("(27,28),(35,22)","(27,29),(35,24)")
        text=text.replace(",('upper-right',(33,18),(31,21))","")
    module=rd/Path(m['module']).name;module.write_text(text)
    m.update(result_dir=str(rd),module=str(module))
    (rd/(m['icon_id']+'.metadata.json')).write_text(json.dumps(m,indent=2))
(root/'batch-v1.json').write_text((root/'batch.json').read_text())
(root/'batch.json').write_text(json.dumps(rows,indent=2))
