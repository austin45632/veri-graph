# Decision Log

| date | decision_id | summary | impacted_ids |
|---|---|---|---|
| 2026-03-15 | ADR-0001 | Adopt a Markdown-first plus NetworkX prototype strategy | SPEC-001, REQ-001, TR-001, TI-001, TC-001, TS-001 |
| 2026-03-15 | ADR-0002 | Collapse the formal traceability chain to SPEC-REQ-TC-TS and align with Codebeamer and vTESTstudio | SPEC-001, REQ-001, TC-001, TS-001 |
| 2026-03-15 | ADR-0003 | Promote TR into a Codebeamer tracker and change the formal chain to SPEC-REQ-TR-TC-TS | SPEC-001, REQ-001, TR-001, TI-001, TC-001, TS-001 |
| 2026-03-15 | ADR-0004 | Recast TI as a Codebeamer test case hierarchy parent node instead of a folder | TI-001, TC-001 |
| 2026-03-15 | ADR-0005 | Add TI as a formal knowledge graph node and establish the SPEC-REQ-TR-TI-TC-TS structure | TI-001, TC-001, TS-001 |
| 2026-03-15 | ADR-0006 | Adopt a dual-axis automotive knowledge graph with automotive semantics nodes | FEAT-001, VSTATE-001, SIG-001, FAULT-001, SG-001 |
| 2026-03-15 | ADR-0007 | Add DiagnosticEvent to the automotive semantics axis and separate diagnostic events from fault reactions | DIAG-001, FAULT-001, TC-001 |
| 2026-03-15 | ADR-0008 | Add Variant to the automotive semantics axis to express applicability by vehicle or equipment | VAR-001, REQ-001, TC-001 |
| 2026-03-15 | ADR-0009 | Add Build and Evidence to the result layer and connect tests to executed artifacts | BUILD-001, EVID-001, TC-001, TS-001 |
| 2026-03-15 | ADR-0010 | Add TestRun and Result to the result layer and separate execution batches from outcomes | RUN-001, RES-001, BUILD-001, TS-001 |
| 2026-03-15 | ADR-0011 | Use PR-based GitHub governance for a single-maintainer repository while keeping verify and branch protection enabled | .github/workflows/verification-gates.yml, .github/CODEOWNERS, .github/PULL_REQUEST_TEMPLATE.md |
| 2026-03-15 | ADR-0012 | Define a GitHub triage label taxonomy across type, impact axis, and tooling dimensions | .github/ISSUE_TEMPLATE, .github/CODEOWNERS, .github/PULL_REQUEST_TEMPLATE.md |
| 2026-03-15 | ADR-0013 | Enable GitHub Discussions as the entry point for open-ended architecture and process exploration | .github/ISSUE_TEMPLATE/config.yml, README.md, docs/governance/system-governance.md |
| 2026-03-15 | ADR-0014 | Create the GitHub Project `veri-graph Triage` as the central triage workspace | GitHub Project #2, .github/ISSUE_TEMPLATE, docs/governance/system-governance.md |
| 2026-03-15 | ADR-0015 | Add Type, Axis, and Tooling triage fields to the GitHub Project and align them with labels | GitHub Project #2, labels, issue templates |
| 2026-03-15 | ADR-0016 | Establish `SPEC -> SpecFragment -> CandidateRequirement -> Human Review -> REQ` pipeline, separating candidate requirements from formal requirements | SPEC-001, S6867-07-blocked, REQ-001 |
