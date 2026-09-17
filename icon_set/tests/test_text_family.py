import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from icon_set.scripts.primitives_catalog import build_catalog
from icon_set.scripts.text_family import gallery_records

class TextFamilyTests(unittest.TestCase):
    def test_text_source_links_survive_catalog_rebuild(self):
        links={k:{} for k in ['by_id','by_reference_id','by_path','by_reference_path','anonymous','families']}
        rows=[dict(uuid='source-1',path='letters/a.svg',category='letters',copies=1)]
        record=dict(icon_id='text-a',family='text',source_ids=['source-1'],key='text/text-a',preview_url='../text28/text-a.svg')
        with patch('icon_set.scripts.primitives_catalog.scan',return_value=rows),patch('icon_set.scripts.primitives_catalog.conversion_warning',return_value=None):
            catalog=build_catalog(Path('/unused'),{'text-a':record},{},links)
        self.assertEqual(catalog['rows'][0]['generated'][0]['key'],'text/text-a')
        self.assertEqual(catalog['rows'][0]['state'],'generated')

    def test_manifest_fallback_and_missing_export_rejection(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder);staged=root/'stage';published=root/'dist';target=root/'gallery'
            target.mkdir();text=published/'text28';text.mkdir(parents=True)
            record=dict(icon_id='text-a',family='text',canvas_height=28,source_ids=['source-1'])
            (text/'manifest.json').write_text(json.dumps(dict(family='text',canvas_height=28,icons=[record])))
            with self.assertRaisesRegex(ValueError,'Missing text export'):gallery_records(staged,published,target)
            (text/'text-a.svg').write_text('<svg/>')
            rows=gallery_records(staged,published,target)
            self.assertEqual(rows[0]['key'],'text/text-a')
            self.assertEqual(rows[0]['preview_url'],'../text28/text-a.svg')

if __name__=='__main__':unittest.main()
