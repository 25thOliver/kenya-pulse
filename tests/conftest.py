"""
Configure pytest to find the ingestion source modules.
This runs automatically before any test file.
"""
import sys
from pathlib import Path

# Add ingestion/src to the Python path so tests can import
# clients, transformers, loaders etc. directly.
sys.path.insert(
    0,
    str(Path(__file__).parent.parent / "ingestion" / "src"),
)
