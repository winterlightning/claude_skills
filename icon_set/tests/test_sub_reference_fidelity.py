import hashlib
import json
from icon_set.scripts.sub_reference_fidelity import annotate_sub_references

def test_fidelity_findings_apply_only_to_reviewed_model_revision(tmp_path):
    source=tmp_path/'model.py';source.write_text('old model')
    data=tmp_path/'icon_set/data';data.mkdir(parents=True)
    (data/'sub-reference-fidelity.json').write_text(json.dumps({'letter-b-sub':{'model_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'status':'superseded'}}))
    row={'family':'sub','icon_id':'letter-b-sub','python_source':{'path':'model.py'}}
    annotate_sub_references([row],tmp_path)
    assert row['reference_fidelity']['status']=='superseded'
    source.write_text('new complete model')
    annotate_sub_references([row],tmp_path)
    assert 'reference_fidelity' not in row

def test_missing_source_does_not_inherit_fidelity_verdict(tmp_path):
    data=tmp_path/'icon_set/data';data.mkdir(parents=True)
    (data/'sub-reference-fidelity.json').write_text(json.dumps({'x':{'model_sha256':'abc','status':'superseded'}}))
    row={'family':'sub','icon_id':'x'}
    annotate_sub_references([row],tmp_path)
    assert 'reference_fidelity' not in row
