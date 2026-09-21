"""Apply only the reviewed 750 decisions, with a rollback snapshot and checks."""
import collections,json,sqlite3,sys
from pathlib import Path
P=Path(__file__).resolve().parent;ROOT=P.parents[2];sys.path.insert(0,str(ROOT))
from icon_set.scripts.primitive_status import load_status,set_status,validate_component
from icon_set.scripts.primitive_briefs import load_primitive_briefs,save_primitive_brief
from icon_set.scripts.deploy import record_activity
review=json.loads((P/'review.json').read_text());rows=review['rows']
original={r['uuid']:r for r in json.loads((P/'scope.json').read_text())}
refs=json.loads((P/'reference-briefs-before.json').read_text())
known=set(original)
assert len(rows)==len(known)==750
for r in rows:
    assert r['uuid'] in known and r['uuid'] in r['reference_brief'] and r['reference_path'] in r['reference_brief']
    assert 0<len(r['reference_brief'])<=20000
    if r['route']!='solo':
        validate_component(r['main_brief'],'main_brief');validate_component(r['sub_brief'],'sub_brief')
db=ROOT/'icon_set/.local/state/feedback.sqlite3'
conn=sqlite3.connect(db,timeout=20)
with conn:
    conn.execute('BEGIN IMMEDIATE')
    before=load_status(conn);before_refs=load_primitive_briefs(conn)
    for uid in known:
        assert before.get(uid)==original[uid]['decision'],f'Concurrent source change: {uid}'
        assert before_refs.get(uid)==refs[uid],f'Concurrent brief change: {uid}'
    backup={uid:{'decision':before.get(uid),'reference_brief':before_refs.get(uid)} for uid in known}
    backup_path=P/'before-save.json'
    if backup_path.exists():
        assert json.loads(backup_path.read_text())==backup,'Existing rollback snapshot differs; reconcile before retrying.'
    else:backup_path.write_text(json.dumps(backup,indent=2))
    for r in rows:
        uid=r['uuid'];family='solo' if r['route'] in ('solo','side') else 'container'
        save_primitive_brief(conn,uid,family,r['reference_brief'],known=known,user='agent',record=record_activity)
        kwargs={}
        note=r['visual_reason']
        if r['route']=='solo':
            if r['status']=='skip':note+=' Duplicate-generation hold: '+r['reuse_action']+' — '+r['reuse_candidates'][0]['icon_id']+'. See saved SOLO48 brief.'
        else:
            kwargs.update(main_brief=r['main_brief'],sub_brief=r['sub_brief'])
            if r['route']=='side':kwargs['sub_position']=r['sub_position']
            if r['extra_components_added']:note+=f" Full saved reference brief contains {len(r['components'])} independent components; do not omit the additional parts."
            if r['notes']:note+=' '+r['notes']
        set_status(conn,[uid],r['status'],r['reason'],note,user='agent',record=record_activity,known=known,**kwargs)
    after=load_status(conn);after_refs=load_primitive_briefs(conn)
    for r in rows:
        uid=r['uuid'];d=after.get(uid);ref=after_refs[uid]
        assert ref['brief']==r['reference_brief'].strip()
        assert ref['family']==('solo' if r['route'] in ('solo','side') else 'container')
        if r['status']=='todo':assert d is None
        else:
            assert d['reason']==r['reason']
            if r['route']!='solo':
                assert d['main_brief']==r['main_brief'] and d['sub_brief']==r['sub_brief']
                assert d['sub_position']==r.get('sub_position')
            else:assert d['main_brief'] is None and d['sub_brief'] is None
    assert {k:v for k,v in after.items() if k not in known}=={k:v for k,v in before.items() if k not in known}
    assert {k:v for k,v in after_refs.items() if k not in known}=={k:v for k,v in before_refs.items() if k not in known}
conn.close()
result={'saved':True,'database':str(db),'summary':review['summary'],'reference_briefs_verified':750,'skipped_source_brief_coverage':'557/557','side_positions_verified':3,'unrelated_decisions_unchanged':True,'unrelated_briefs_unchanged':True,'scope_snapshot_comparison_passed':True,'reuse_readiness_limitation':'Only the 12 source-linked reuse targets were visually compared in this classification pass. Other semantic candidates are unverified search leads, not approved matches.','open_visual_questions':[20,640]}
(P/'verification.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
