from pathlib import Path
import os
import re
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]
FAILURE_FIXTURE_ROOT = ROOT / 'tests/fixtures/traceability_failure'
AUTOMOTIVE_FAILURE_FIXTURE_ROOT = ROOT / 'tests/fixtures/automotive_failure'
RESULT_FAILURE_FIXTURE_ROOT = ROOT / 'tests/fixtures/result_failure'

REQUIRED_DIRS = [
    'docs/architecture',
    'docs/automotive',
    'docs/results',
    'docs/governance',
    'docs/specs',
    'docs/requirements',
    'docs/test-requirements',
    'docs/test-intents',
    'docs/testcases',
    'docs/test-scripts',
    'docs/traceability',
    'docs/decisions/adr',
    'prototype/sample-data',
]

REQUIRED_FILES = [
    'README.md',
    'docs/architecture/model-mapping.md',
    'docs/architecture/codebeamer-configuration.md',
    'docs/architecture/vteststudio-integration.md',
    'docs/automotive/README.md',
    'docs/automotive/automotive-matrix.md',
    'docs/automotive/FEAT-001.md',
    'docs/automotive/VSTATE-001.md',
    'docs/automotive/SIG-001.md',
    'docs/automotive/FAULT-001.md',
    'docs/automotive/DIAG-001.md',
    'docs/automotive/VAR-001.md',
    'docs/automotive/SG-001.md',
    'docs/results/README.md',
    'docs/results/result-matrix.md',
    'docs/results/BUILD-001.md',
    'docs/results/RUN-001.md',
    'docs/results/RES-001.md',
    'docs/results/EVID-001.md',
    'docs/governance/system-governance.md',
    'docs/traceability/trace-matrix.md',
    'docs/decisions/decision-log.md',
    'prototype/graph-schema.md',
    'prototype/queries.md',
    'scripts/check_all.py',
]


class TestProjectStructure(unittest.TestCase):
    def test_required_directories_exist(self):
        missing = [d for d in REQUIRED_DIRS if not (ROOT / d).is_dir()]
        self.assertFalse(missing, f'Missing directories: {missing}')

    def test_required_files_exist(self):
        missing = [f for f in REQUIRED_FILES if not (ROOT / f).is_file()]
        self.assertFalse(missing, f'Missing files: {missing}')

    def test_result_matrix_has_required_rows(self):
        content = (ROOT / 'docs/results/result-matrix.md').read_text(encoding='utf-8')
        self.assertIn('| TS-001 | RUN-001 | executed_in_run | active | 2026-03-15 |', content)
        self.assertIn('| RUN-001 | RES-001 | produced_result | active | 2026-03-15 |', content)

    def test_model_mapping_mentions_result_layer(self):
        content = (ROOT / 'docs/architecture/model-mapping.md').read_text(encoding='utf-8')
        self.assertIn('| `TestRun` | Yes | Yes | Result layer |', content)
        self.assertIn('| `Result` | Yes | Yes | Result layer |', content)

    def test_readme_mentions_check_all(self):
        content = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('python scripts\\check_all.py', content)
        self.assertIn('`check_all.py`', content)

    def test_ci_workflow_exists_and_runs_verification_gates(self):
        content = (ROOT / '.github/workflows/verification-gates.yml').read_text(encoding='utf-8')
        self.assertIn("python -m unittest discover -s tests -p 'test_*.py' -v", content)
        self.assertIn('python scripts/check_all.py', content)
        self.assertIn('actions/setup-python@v5', content)

    def test_result_samples_exist_and_link_to_main_chain(self):
        run = (ROOT / 'docs/results/RUN-001.md').read_text(encoding='utf-8')
        result_doc = (ROOT / 'docs/results/RES-001.md').read_text(encoding='utf-8')
        self.assertIn('TestRun', run)
        self.assertIn('Result', result_doc)

    def test_prototype_docs_match_extended_schema(self):
        schema = (ROOT / 'prototype/graph-schema.md').read_text(encoding='utf-8')
        queries = (ROOT / 'prototype/queries.md').read_text(encoding='utf-8')
        self.assertIn('TestRun (`RUN-*`)', schema)
        self.assertIn('Result (`RES-*`)', schema)
        self.assertIn('查詢某個 `Run-*` 產生了哪些 `Result-*`', queries)

    def test_governance_doc_mentions_all_layers(self):
        content = (ROOT / 'docs/governance/system-governance.md').read_text(encoding='utf-8')
        self.assertIn('`python scripts\\check_all.py`', content)
        self.assertIn('`TC -> BUILD`、`TS -> RUN`、`RUN -> RES`、`TS -> EVID`、`EVID -> BUILD` 是否正確', content)

    def test_decision_log_includes_result_layer_adrs(self):
        log = (ROOT / 'docs/decisions/decision-log.md').read_text(encoding='utf-8')
        self.assertIn('ADR-0010', log)

    def test_traceability_script_passes_on_main_dataset(self):
        result = subprocess.run(['python', str(ROOT / 'scripts/check_traceability.py')], cwd=ROOT, capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_automotive_script_passes_on_main_dataset(self):
        result = subprocess.run(['python', str(ROOT / 'scripts/check_automotive_semantics.py')], cwd=ROOT, capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_result_script_passes_on_main_dataset(self):
        result = subprocess.run(['python', str(ROOT / 'scripts/check_result_evidence.py')], cwd=ROOT, capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('result layer check passed (4 result nodes)', result.stdout)

    def test_check_all_passes_on_main_dataset(self):
        result = subprocess.run(['python', str(ROOT / 'scripts/check_all.py')], cwd=ROOT, capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('== traceability ==', result.stdout)
        self.assertIn('== automotive semantics ==', result.stdout)
        self.assertIn('== result layer ==', result.stdout)
        self.assertIn('check_all passed', result.stdout)

    def test_traceability_script_reports_fixture_failure(self):
        env = os.environ.copy()
        env.update({'TRACEABILITY_ROOT': str(FAILURE_FIXTURE_ROOT), 'TRACEABILITY_MATRIX': str(FAILURE_FIXTURE_ROOT / 'docs/traceability/trace-matrix.md')})
        result = subprocess.run(['python', str(ROOT / 'scripts/check_traceability.py')], cwd=ROOT, capture_output=True, text=True, check=False, env=env)
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        self.assertIn('[REQ missing TR]\nREQ-002', result.stdout)

    def test_automotive_script_reports_fixture_failure(self):
        env = os.environ.copy()
        env.update({'TRACEABILITY_ROOT': str(AUTOMOTIVE_FAILURE_FIXTURE_ROOT), 'AUTOMOTIVE_MATRIX': str(AUTOMOTIVE_FAILURE_FIXTURE_ROOT / 'docs/automotive/automotive-matrix.md')})
        result = subprocess.run(['python', str(ROOT / 'scripts/check_automotive_semantics.py')], cwd=ROOT, capture_output=True, text=True, check=False, env=env)
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        self.assertIn('[VAR missing matrix link]\nVAR-010', result.stdout)

    def test_result_script_reports_fixture_failure(self):
        env = os.environ.copy()
        env.update({'TRACEABILITY_ROOT': str(RESULT_FAILURE_FIXTURE_ROOT), 'RESULT_MATRIX': str(RESULT_FAILURE_FIXTURE_ROOT / 'docs/results/result-matrix.md')})
        result = subprocess.run(['python', str(ROOT / 'scripts/check_result_evidence.py')], cwd=ROOT, capture_output=True, text=True, check=False, env=env)
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        self.assertIn('[RUN missing matrix link]\nRUN-020', result.stdout)
        self.assertIn('[RES missing matrix link]\nRES-020', result.stdout)


if __name__ == '__main__':
    unittest.main()
