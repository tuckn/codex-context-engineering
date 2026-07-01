#!/usr/bin/env python3
"""Wrapper for distilling a Codex session note into a review candidate."""

from context_bridge import main


if __name__ == "__main__":
    raise SystemExit(main(["distill-session", *(__import__("sys").argv[1:])]))
