# import time
# import torch
# from transformers import AutoTokenizer, AutoModelForCausalLM
#
#
# class CodeGenWrapper:
#     def __init__(self, model_name="Salesforce/codegen-350M-multi", device=None):
#         """
#         Initialize CodeGen model and tokenizer.
#         """
#         self.tokenizer = AutoTokenizer.from_pretrained(model_name)
#         self.model = AutoModelForCausalLM.from_pretrained(model_name)
#
#         # Set padding token
#         if self.tokenizer.pad_token is None:
#             self.tokenizer.pad_token = self.tokenizer.eos_token
#
#         # Device setup
#         self.device = device or torch.device("cuda" if torch.cuda.is_available() else "cpu")
#         self.model.to(self.device)
#
#     def translate(self, code, src_lang="java", tgt_lang="python", max_new_tokens=256):
#         """
#         Translate code from src_lang to tgt_lang using CodeGen.
#         Returns translated code and elapsed time.
#         """
#         prompt = f"""\"\"\"Translate the following {src_lang} code to {tgt_lang}:
#
# {code}
#
# {tgt_lang} function:\"\"\""""
#
#         start_time = time.time()
#
#         inputs = self.tokenizer(prompt, return_tensors="pt", padding=True, truncation=True).to(self.device)
#         output_ids = self.model.generate(
#             input_ids=inputs["input_ids"],
#             attention_mask=inputs["attention_mask"],
#             max_new_tokens=max_new_tokens,
#             num_beams=5,
#             early_stopping=True,
#             do_sample=False,
#             pad_token_id=self.tokenizer.pad_token_id
#         )
#
#         elapsed = time.time() - start_time
#         translated_code = self.tokenizer.decode(output_ids[0], skip_special_tokens=True)
#
#         # Remove the prompt from output
#         translated_code = translated_code.replace(prompt, "").strip()
#         translated_code = translated_code.split("\n\n")[0]  # keep only the first function
#
#         return {
#             "code": translated_code,
#             "time": elapsed
#         }



#
#
#
# import time
# import re
# import torch
# from transformers import AutoTokenizer, AutoModelForCausalLM
#
# class CodeGenWrapper:
#     def __init__(self, model_name="Salesforce/codegen-350M-multi", device=None):
#         """
#         Initialize CodeGen model and tokenizer.
#         """
#         self.tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
#         self.model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True)
#
#         # Set padding token
#         if self.tokenizer.pad_token is None:
#             self.tokenizer.pad_token = self.tokenizer.eos_token
#
#         # Device setup
#         self.device = device or torch.device("cuda" if torch.cuda.is_available() else "cpu")
#         self.model.to(self.device)
#
#     def extract_java_logic(self, java_code):
#         """
#         Extract the main logic inside Java main method or first function.
#         """
#         # Extract content inside main method if present
#         main_match = re.search(r'public static void main\s*\(.*?\)\s*\{(.*)\}', java_code, re.DOTALL)
#         if main_match:
#             logic = main_match.group(1)
#         else:
#             # Fallback: use everything inside class
#             class_match = re.search(r'public class .*?\{(.*)\}', java_code, re.DOTALL)
#             logic = class_match.group(1) if class_match else java_code
#         return logic.strip()
#
#     def translate(self, java_code, max_new_tokens=256):
#         prompt = f"""
#     Translate Java to Python 3.
#
#     ### Java
#     {java_code}
#
#     ### Python
#     """
#         start_time = time.time()
#
#         inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
#         output_ids = self.model.generate(
#             **inputs,
#             max_new_tokens=max_new_tokens,
#             do_sample=False,
#             temperature=0.0,
#             pad_token_id=self.tokenizer.eos_token_id,
#             eos_token_id=self.tokenizer.eos_token_id
#         )
#
#         elapsed = time.time() - start_time
#         decoded = self.tokenizer.decode(output_ids[0], skip_special_tokens=True)
#
#         # Extract only python part
#         python_code = decoded.split("### Python", 1)[-1].strip()
#
#         # Cleanup Java leftovers
#         python_code = python_code.replace("System.out.println", "print")
#         python_code = python_code.replace(";", "")
#         python_code = re.sub(r"class\s+\w+.*?:", "", python_code)
#
#         return {
#             "code": python_code,
#             "time": elapsed
#         }
#
#
# # 🔹 Usage example
# if __name__ == "__main__":
#     wrapper = CodeGenWrapper()
#
#     java_code = """
# import java.util.Scanner;
#
# public class SimpleInterest {
#     public static void main(String[] args) {
#         Scanner scanner = new Scanner(System.in);
#         System.out.print("Enter Principal amount: ");
#         double P = scanner.nextDouble();
#         System.out.print("Enter Rate of interest: ");
#         double R = scanner.nextDouble();
#         System.out.print("Enter Time (in years): ");
#         double T = scanner.nextDouble();
#
#         double interest = (P * R * T) / 100;
#         System.out.println("Simple Interest is: " + interest);
#         scanner.close();
#     }
# }
# """
#
#     result = wrapper.translate(java_code)
#     print("=== Translated Python Code ===\n")
#     print(result["code"])







import time
import re
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

class CodeGenWrapper:
    def __init__(self, model_name="Salesforce/codegen-350M-multi", device=None):
        """
        Initialize CodeGen model and tokenizer.
        """
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True)

        # Set padding token
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

        # Device setup
        self.device = device or torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)
        self.model.eval()

    # ✅ Clean + enforce Python behavior
    def postprocess_python(self, text: str) -> str:
        if not text:
            return ""

        # Remove Java leftover syntax
        text = text.replace("System.out.println", "print")
        text = text.replace("Scanner", "")
        text = text.replace(";", "")

        # Fix input & args usage
        text = re.sub(r"sys\.argv\[\d+\]", "input()", text)

        # Ensure Python3 print syntax
        text = re.sub(r"print\s+([^\(].*)", r"print(\1)", text)

        # Convert int parsing (simple cases)
        text = text.replace("Integer.parseInt", "int")
        text = text.replace("Double.parseDouble", "float")

        # Remove curly braces
        text = text.replace("{", "").replace("}", "")

        # Remove any class declarations
        text = re.sub(r"class\s+\w+.*:", "", text)

        # Strip junk whitespace
        return text.strip()

    # ✅ Matches your pipeline signature
    def translate(self, code, src_lang="Java", tgt_lang="Python 3", max_new_tokens=256):
        prompt = f"""
Translate the following Java code to modern Python 3 code.

RULES:
- Use input() instead of command line arguments
- Use print() with parentheses
- Remove Java syntax like semicolons/brackets
- Output must be complete & runnable Python

### Java
{code}

### Python
"""

        start_time = time.time()
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)

        output_ids = self.model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False,
            temperature=0.0,
            eos_token_id=self.tokenizer.eos_token_id,
            pad_token_id=self.tokenizer.pad_token_id,
        )

        elapsed = round(time.time() - start_time, 4)
        decoded = self.tokenizer.decode(output_ids[0], skip_special_tokens=True)

        # Extract python part
        python_code = decoded.split("### Python", 1)[-1].strip()

        # ✅ Apply our enforcement rules
        python_code = self.postprocess_python(python_code)

        return {
            "code": python_code,
            "time": elapsed,
        }


# 🔹 Local test execution
if __name__ == "__main__":
    wrapper = CodeGenWrapper()

    java_code = """
import java.util.Scanner;

public class SimpleInterest {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter Principal: ");
        double P = scanner.nextDouble();
        System.out.print("Enter Rate: ");
        double R = scanner.nextDouble();
        System.out.print("Enter Time: ");
        double T = scanner.nextDouble();
        double interest = (P * R * T) / 100;
        System.out.println("Simple Interest is: " + interest);
    }
}
"""

    result = wrapper.translate(java_code)
    print("✅ Output:\n")
    print(result["code"])
