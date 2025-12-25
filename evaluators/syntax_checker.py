

import tempfile
import subprocess
import os
import re

def check_syntax(code, file_name=None, lang=None):
    """
    Checks syntax validity of given code.
    - Auto-detects language from file name
    - Adds stricter validation for Python to avoid false positives
    """
    # Detect language automatically
    if not lang and file_name:
        if file_name.endswith(".py"):
            lang = "python"
        elif file_name.endswith(".java"):
            lang = "java"

    if not lang:
        raise ValueError("Language not specified and could not be inferred from file name")

    # --- PYTHON SYNTAX CHECK ---
    if lang.lower() == "python":
        try:
            # Reject if clearly non-Python syntax is present
            if re.search(r"(public\s+class|System\.out|Scanner|;|\bvoid\b)", code):
                print(f"[Python Syntax Error]: Contains Java-like syntax.")
                return False

            # Check if there's any Python code structure
            if not re.search(r"(def\s+\w+\(|print\(|import\s+\w+|if\s+__name__|class\s+\w+)", code):
                print(f"[Python Syntax Error]: No recognizable Python code structure.")
                return False

            compile(code, "<string>", "exec")
            return True
        except Exception as e:
            print(f"[Python Syntax Error]: {e}")
            return False

    # --- JAVA SYNTAX CHECK ---
    elif lang.lower() == "java":
        tmp_file_path = None
        try:
            # Detect public class name if present
            match = re.search(r'public\s+class\s+([A-Za-z_]\w*)', code)
            class_name = match.group(1) if match else "TempClass"

            # Create temporary file
            tmp_dir = tempfile.gettempdir()
            tmp_file_path = os.path.join(tmp_dir, f"{class_name}.java")
            with open(tmp_file_path, "w", encoding="utf-8") as tmp_file:
                tmp_file.write(code)

            # Compile using javac
            result = subprocess.run(
                ["javac", tmp_file_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            if result.returncode != 0:
                print(f"[Java Compile Error]: {result.stderr.strip()}")

            return result.returncode == 0

        except Exception as e:
            print(f"[Java Exception]: {e}")
            return False
        finally:
            # Cleanup files
            try:
                if tmp_file_path and os.path.exists(tmp_file_path):
                    os.remove(tmp_file_path)
                class_file = tmp_file_path.replace(".java", ".class") if tmp_file_path else None
                if class_file and os.path.exists(class_file):
                    os.remove(class_file)
            except:
                pass

    else:
        raise ValueError(f"Unsupported language: {lang}")
