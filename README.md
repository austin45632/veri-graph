# veri-graph

veri-graph is a Markdown-first verification knowledge graph prototype for an automotive instrument cluster domain.

## Canonical Chains

Formal graph chain:

`SPEC -> REQ -> TR -> TI -> TC -> TS`

Automated pre-requirement chain:

`SPEC -> SpecFragment -> CandidateRequirement -> Human Review -> REQ`

Minimum compliance gate:

`REQ -> TR -> TC -> TS`

## Scope

- text-first requirements and traceability modeling
- ADR-backed governance for model and process changes
- Markdown-first repository with NetworkX-oriented prototype documents
- Codebeamer / vTESTstudio mapping for formal requirements and executable tests
- automotive knowledge graph semantics and result-layer traceability

## Repository Structure

- `docs/architecture/model-mapping.md`: canonical model mapping across repo, knowledge graph, Codebeamer, and vTESTstudio
- `docs/architecture/codebeamer-configuration.md`: formal Codebeamer tracker and boundary rules
- `docs/architecture/vteststudio-integration.md`: vTESTstudio integration rules for `TS-*`
- `docs/automotive/`: automotive semantics samples and automotive review matrix
- `docs/results/`: result-layer samples and result review matrix
- `docs/specs/`: source specification documents, including external-style spec files such as `S6867-07-blocked.md`
- `docs/requirements/`: formal approved requirements (`REQ-*`)
- `docs/test-requirements/`: test requirements (`TR-*`)
- `docs/test-intents/`: scenario intent examples (`TI-*`)
- `docs/testcases/`: test cases (`TC-*`)
- `docs/test-scripts/`: test script index documents (`TS-*`)
- `docs/traceability/trace-matrix.md`: formal traceability review view
- `docs/decisions/adr/`: ADR documents
- `docs/decisions/decision-log.md`: decision index
- `prototype/`: graph schema and query requirements for the NetworkX prototype
- `.github/workflows/verification-gates.yml`: CI verification workflow

## ID Families

- `SPEC-###`, `REQ-###`, `TR-###`, `TI-###`, `TC-###`, `TS-###`
- `CANDREQ-###` for candidate requirements
- `FEAT-###`, `VSTATE-###`, `SIG-###`, `FAULT-###`, `DIAG-###`, `VAR-###`, `SG-###`
- `BUILD-###`, `RUN-###`, `RES-###`, `EVID-###`

## Core Model Notes

- `SpecFragment` is an ingestion node derived from a `SPEC` source unit
- `SpecFragment` may come from a `paragraph`, `clause`, or `table_row`
- `CandidateRequirement` is an automatically extracted candidate, not a formal `REQ`
- every candidate must be human-reviewed before it becomes a formal `REQ`
- risk is confidence-driven by default
- candidates involving `safety`, regulatory obligation, `warning/telltale`, `fault reaction`, or `diagnostic behavior` are forced to `high risk`
- `TR` carries requirement intent in Codebeamer as a formal tracker
- `TI` carries scenario intent in the graph and is represented in Codebeamer through a hierarchy parent node
- `TS` is carried by vTESTstudio as the executable test asset
- `S6867-07-blocked.md` is treated as a `SPEC`-class source document

See `docs/architecture/model-mapping.md` for the authoritative model definition.

## Verification

```powershell
python -m unittest discover -s tests -p 'test_*.py' -v
python scripts\check_traceability.py
python scripts\check_automotive_semantics.py
python scripts\check_result_evidence.py
python scripts\check_all.py
```

- `check_traceability.py`: minimum compliance gate for `REQ -> TR -> TC -> TS`
- `check_automotive_semantics.py`: automotive semantics integrity against `automotive-matrix.md`
- `check_result_evidence.py`: result-layer integrity against `result-matrix.md`
- `check_all.py`: runs all verification gates together
- GitHub Actions runs unittest plus `check_all.py` on `push` and `pull_request`
