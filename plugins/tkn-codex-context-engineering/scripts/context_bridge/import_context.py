#!/usr/bin/env python3
"""Wrapper for snapshot-importing user-global Codex context into a repository."""

from context_bridge import main


if __name__ == "__main__":
    raise SystemExit(main(["import", *(__import__("sys").argv[1:])]))
