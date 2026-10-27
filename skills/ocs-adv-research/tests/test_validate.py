import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class ValidationTests(unittest.TestCase):
    def run_check(self, root):
        script = ROOT / 'scripts/validate.py'
        self.assertTrue(script.exists(), 'validator must exist')
        spec = importlib.util.spec_from_file_location('validator', script)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module.validate(root)

    def fixture(self, directory):
        root = Path(directory) / 'ocs-adv-research'
        root.mkdir()
        (root / 'SKILL.md').write_text('---\nname: ocs-adv-research\ndescription: Research and validate product improvements.\n---\n# Method\n')
        return root

    def test_valid_minimal_skill(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(self.run_check(self.fixture(d)), [])

    def test_missing_entrypoint(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertIn('missing SKILL.md', self.run_check(Path(d)))

    def test_mismatched_name(self):
        with tempfile.TemporaryDirectory() as d:
            root = self.fixture(d)
            p = root / 'SKILL.md'
            p.write_text(p.read_text().replace('name: ocs-adv-research', 'name: wrong'))
            self.assertTrue(any('name' in e for e in self.run_check(root)))

    def test_broken_relative_reference(self):
        with tempfile.TemporaryDirectory() as d:
            root = self.fixture(d)
            with (root / 'SKILL.md').open('a') as f:
                f.write('[guide](references/missing.md)\n')
            self.assertTrue(any('broken link' in e for e in self.run_check(root)))

    def test_symlink_escape(self):
        with tempfile.TemporaryDirectory() as d:
            root = self.fixture(d)
            (root / 'leak').symlink_to('/etc/passwd')
            self.assertTrue(any('symlink' in e for e in self.run_check(root)))

    def test_packaged_skill(self):
        self.assertEqual(self.run_check(ROOT), [])

if __name__ == '__main__':
    unittest.main()
