# ADR-0016: SPEC to Candidate Requirement Pipeline

- Date: 2026-03-15
- Status: Accepted

## Context

veri-graph already treats `REQ` as a formal governed artifact. A direct `SPEC -> REQ` automation path would mix raw extraction output with approved requirements and would weaken the ownership boundary for `TR / TC / TS` traceability. Specification sources such as prose, numbered clauses, and table rows need an ingestion and review layer before they can become formal requirements.

## Decision

The automated pre-requirement pipeline is:

`SPEC -> SpecFragment -> CandidateRequirement -> Human Review -> REQ`

Definitions:

- `SPEC` is the source specification document, including internal `SPEC-*` files and external-style sources such as `S6867-07-blocked.md`
- `SpecFragment` is an ingestion unit derived from the source specification
- `SpecFragment` may be a `paragraph`, `clause`, or `table_row`
- `CandidateRequirement` is an automatically extracted candidate, not a formal `REQ`
- every candidate must be human-reviewed before it can become a formal requirement

## Risk Policy

Candidate risk follows this rule set:

- default risk is confidence-driven
- any candidate involving `safety`, regulatory obligation, `warning/telltale`, `fault reaction`, or `diagnostic behavior` is forced to `high risk`

This means:

- `confidence` drives most review prioritization
- critical domain classes override the default confidence-only rule

## Candidate Interface

`CandidateRequirement` must provide stable identifiers and provenance.

Minimum fields:

- `candidate_id`
- `source_spec_id`
- `source_anchor`
- `source_text`
- `normalized_statement`
- `modality`
- `confidence`
- `risk_level`
- `review_status`

Allowed `review_status` values:

- `pending`
- `approved`
- `rejected`
- `needs_split`
- `needs_merge`

## Consequences

### Positive

- formal `REQ` remains a governed approved artifact
- raw specification content can be ingested at higher scale without polluting the formal requirement chain
- extraction and review behavior can be improved independently from downstream traceability

### Negative

- the model now requires a candidate-review layer
- `SPEC -> REQ` remains indirect in v1 and adds review overhead

## Non-Goals

- no automatic promotion from candidate to formal `REQ`
- no direct mapping from candidate requirements into the Codebeamer requirement tracker
- no inclusion of candidate requirements in `trace-matrix.md`
