.PHONY: verify test demo

verify:
	python3 -m pytest -q tests/test_canonical_surface.py
	./scripts/reproduce demo

test:
	python3 -m pytest -q tests/test_canonical_surface.py

demo:
	./scripts/reproduce demo
