# File: tests/test_connections/test_chat_gemini/test_chat_gemini.py
# Version: 1.0.0
import unittest
import sys
from pathlib import Path

# Add project root to path to allow importing the logic
PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT_ROOT))

from analyze import parse_and_enrich_file

class TestChatGemini(unittest.TestCase):
    """
    Tests the full chat pipeline for the Gemini provider.
    """

    def test_gemini_chat(self):
        """
        Verifies that the full chat pipeline works for the Gemini provider.
        """
        print("\n--- Testing Gemini Chat ---")
        
        # Create a dummy PHP file for testing
        test_file = Path(__file__).parent / "test.php"
        with open(test_file, "w") as f:
            f.write("<?php echo 'hello'; ?>")
            
        result = parse_and_enrich_file(test_file)
        
        self.assertIn("ai_analysis", result)
        self.assertIn("initial_analysis", result["ai_analysis"])
        
        # Clean up the dummy file
        test_file.unlink()
        
        print("✅ PASSED: Gemini chat test successful.")

if __name__ == "__main__":
    unittest.main(verbosity=2)
