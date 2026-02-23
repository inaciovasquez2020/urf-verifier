# URF Verifier

This repository provides the **verification tooling** for Unified Rigidity Framework (URF) artifacts.

It checks structural consistency, scope compliance, and certificate validity for released URF modules.

## What it verifies
- Structural correctness of URF certification artifacts.
- Conformance to declared schemas and invariants.
- Integrity of frozen, reference outputs.

## What it does not do
- Does not generate proofs.
- Does not establish mathematical truth.
- Does not resolve open theoretical questions.

## How to run
Typical usage:
- Select a released artifact or certificate.
- Run the verifier entry point provided in this repository.

(Exact commands are documented alongside the verifier scripts.)

## Output
- Pass / fail verification results.
- Structured diagnostics identifying violated constraints, if any.

## Status
Stable verification tool.
Intended for audit and reproducibility, not development.
