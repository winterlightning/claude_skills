"""Saved combination briefs retain the exact source and component identity."""
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch
from icon_set.scripts.split_handoff import save_split_handoffs
from icon_set.scripts import queue_brief


class SplitHandoffTests(unittest.TestCase):
    def data(self, kind='container'):
        return {'reference_path': 'source.svg', 'combination_type': kind,
                'reason': 'Two independent subjects.', 'components': [
                    {'name': 'Frame' if kind=='container' else 'Document',
                     'family': 'container' if kind=='container' else 'solo', 'description': 'Main subject without the check.'},
                    {'name': 'Check', 'family': 'sub', 'description': 'Check without the main subject.'}]}

    def test_families_exact_source_and_idempotence(self):
        with TemporaryDirectory() as temp:
            root=Path(temp)
            source=root/'reference_12345678-1234-1234-1234-123456789abc.svg'
            content=b'<svg xmlns="http://www.w3.org/2000/svg"><!-- preserve exact bytes --></svg>\n'
            source.write_bytes(content)
            for kind, family in [('container','container'),('side','solo')]:
                data=self.data(kind);data['reference_path']=source.name
                targets=save_split_handoffs(source,data,root/kind)
                self.assertEqual([path.parent.name for path in targets],[family,'sub'])
                for index,target in enumerate(targets):
                    self.assertEqual((target/source.name).read_bytes(),content)
                    record=json.loads((target/'brief.json').read_text())
                    self.assertEqual(record['family'],data['components'][index]['family'])
                    self.assertEqual(record['component_position'],index+1)
                    self.assertEqual(record['source_id'],'12345678-1234-1234-1234-123456789abc')
                    self.assertIn('$icon-making',(target/'brief.md').read_text())
                self.assertEqual(save_split_handoffs(source,data,root/kind),targets)
            self.assertEqual(source.read_bytes(),content)

    def test_edited_handoffs_are_not_overwritten_and_new_source_gets_new_folder(self):
        with TemporaryDirectory() as temp:
            root=Path(temp);source=root/'source.svg';source.write_text('<svg/>')
            target=save_split_handoffs(source,self.data(),root/'out')[0]
            (target/'brief.md').write_text('Human edits to preserve')
            with self.assertRaises(FileExistsError):
                save_split_handoffs(source,self.data(),root/'out')
            self.assertEqual((target/'brief.md').read_text(),'Human edits to preserve')
            source.write_text('<svg><!--new--></svg>')
            self.assertNotEqual(save_split_handoffs(source,self.data(),root/'out')[0],target)

    def test_files_only_does_not_create_database(self):
        with TemporaryDirectory() as temp:
            root=Path(temp).resolve();(root/'source.svg').write_text('<svg/>')
            data=root/'split.json';data.write_text(json.dumps(self.data()))
            database=root/'db.sqlite3'
            with patch.object(queue_brief,'ROOT',root):
                self.assertEqual(queue_brief.main(['--file',str(data),'--files-only','--database',str(database)]),0)
            self.assertFalse(database.exists())
            self.assertEqual(len(list((root/'work/pending-brief').glob('*/*/brief.md'))),2)


if __name__=='__main__':
    unittest.main()
