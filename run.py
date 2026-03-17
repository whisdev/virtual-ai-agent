#!/usr/bin/env python3
"""Run Virtuelle Agentur (multi-agent AI for DACH) from project root."""

import sys
from pathlib import Path

# Add src to path when running from project root
sys.path.insert(0, str(Path(__file__).parent / "src"))

from agentur.main import main

if __name__ == "__main__":
    main()
