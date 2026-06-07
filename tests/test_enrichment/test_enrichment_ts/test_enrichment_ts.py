# File: tests/test_enrichment/test_enrichment_ts/test_enrichment_ts.py
# Version: 1.0.0
import unittest
import sys
import json
from pathlib import Path

# Add project root to path to allow importing the logic
PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT_ROOT))

from analyze import parse_and_enrich_file

class TestEnrichmentTS(unittest.TestCase):
    """
    Tests the live AI enrichment process for a representative TypeScript file.
    """

    def test_ts_enrichment_structure_and_relevance(self):
        """
        Verifies that the enrichment process produces a structurally correct
        and contextually relevant analysis for a TypeScript file.
        """
        print("\n--- Testing Live TypeScript Enrichment ---")
        
        source_file = Path(__file__).resolve().parent / "source.ts"
        self.assertTrue(source_file.exists(), "Source file 'source.ts' not found.")

        # Execute the full parsing and enrichment pipeline
        result = parse_and_enrich_file(source_file)

        # 1. Schema Validation
        self.assertIn("ai_analysis", result)
        self.assertIsInstance(result["ai_analysis"], dict)
        self.assertIn("initial_analysis", result["ai_analysis"])
        self.assertIn("rag_tasks", result["ai_analysis"])
        self.assertIsInstance(result["ai_analysis"]["rag_tasks"], dict)
        
        print("✅ PASSED: Schema validation successful.")

        # 2. Completeness Check
        expected_rag_tasks = ["detailed_analysis", "dependency_identification", "database_interaction"]
        for task in expected_rag_tasks:
            self.assertIn(task, result["ai_analysis"]["rag_tasks"])
        
        print("✅ PASSED: RAG task completeness check successful.")

        # 3. Content Sanity Check
        self.assertGreater(len(result["ai_analysis"]["initial_analysis"]), 20, "Initial analysis is too short.")
        for task, analysis_text in result["ai_analysis"]["rag_tasks"].items():
            self.assertGreater(len(analysis_text), 20, f"RAG task '{task}' analysis is too short.")

        print("✅ PASSED: Content sanity checks successful.")

        # 4. Keyword Spot-Checking for Contextual Relevance
        full_analysis_text = json.dumps(result["ai_analysis"])
        self.assertIn("ArcElement", full_analysis_text, "Class 'ArcElement' not mentioned in the analysis.")
        self.assertIn("BarController", full_analysis_text, "Class 'BarController' not mentioned in the analysis.")

        print("✅ PASSED: Keyword spot-checking for relevance successful.")
        print("✅ FULL PASS: TypeScript enrichment test successful.")

if __name__ == "__main__":
    unittest.main(verbosity=2)
