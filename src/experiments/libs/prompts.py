def create_zeroshot_locate_prompt(file_path):
    return f"""
    Analyze the following Solidity code. Carefully review the following Solidity code and determine if it contains any errors or vulnerabilities.

    If you identify a bug or vulnerability, specify:
    - The type of bug or vulnerability in the "bug_type" field.

    If you do NOT find any bug or vulnerability, set the value "NONE" for "bug_type".
    If you find a bug, specify the line number where the error is located in the "location" field. If no error is found, set "location" to 0.

    Code:
    {open(file_path, 'r', encoding='utf-8').read()}

    Respond in JSON format:
    {{
        "has_error": true/false,
        "location": "line number of where the error is located, otherwise 0 if no error",
        "bug_type": "type of the bug if any, otherwise 'NONE'"   
    }}
    """

def create_zeroshot_cot_locate_prompt(file_path):
    return f"""
    Analyze the following Solidity code. Carefully review the following Solidity code and determine if it contains any errors or vulnerabilities.

    If you identify a bug or vulnerability, specify:
    - The type of bug or vulnerability in the "bug_type" field.

    If you do NOT find any bug or vulnerability, set the value "NONE" for "bug_type".
    If you find a bug, specify the line number where the error is located in the "location" field. If no error is found, set "location" to 0.
    Respond step-by-step with your reasoning in the "reasoning" field, explaining how you analyzed the code, what checks you performed, and why you arrived at your conclusion.

    Then, in the JSON, specify:
    - "has_error": true/false,
    - "bug_type": the type of the bug if any, otherwise "NONE",
    - "reasoning": your step-by-step explanation.

    Code:
    {open(file_path, 'r', encoding='utf-8').read()}

    Respond ONLY in JSON format as follows:
    {{
        "has_error": true/false,
        "bug_type": "type of the bug if any, otherwise NONE",
                "location": "line number of where the error is located, otherwise 0 if no error",
        "reasoning": "Step-by-step explanation of the analysis"
    }}
    """


def create_zeroshot_tot_locate_prompt(file_path):
    return f"""
    Analyze the following Solidity code by considering multiple possible reasoning paths (tree-of-thought) to determine whether it contains any errors or vulnerabilities.

    If you identify a bug or vulnerability, specify:
    - The type of bug or vulnerability in the "bug_type" field.

    If you do NOT find any bug or vulnerability, set the value "NONE" for "bug_type".
    If you find a bug, specify the line number where the error is located in the "location" field. If no error is found, set "location" to 0.
    Code:
    {open(file_path, 'r', encoding='utf-8').read()}

    Respond in JSON format with the following structure:
    {{
        "has_error": true/false,
        "location": "line number of where the error is located, otherwise 0 if no error",
        "reasoning_paths": [
            {{
                "path": "Description of the reasoning path",
                "analysis": "Detailed analysis for this path"
            }},
            ...
        ],
        "final_reasoning": "Consolidated explanation based on all reasoning paths",
        "bug_type": "Type of vulnerability or error (if any)",
    }}
    """

def create_zeroshot_error_comparison_prompt(error1, error2):
    return f"""
    You will receive below two errors found in Solidity smart contracts.
    Each error can be a textual description or a line number indicating where the error occurs.
    Analyze whether both errors refer to the same vulnerability/problem or not.
    If the errors are numbers, compare if they refer to the same line. If they are texts, compare the descriptions. If one is a number and the other is a text, try to match the line number with the correct error description.

    Error 1:
    {error1}

    Error 2:
    {error2}

    Respond in JSON format as follows:
    {{
        "same_error": true/false"
    }}
    """

def create_cot_error_comparison_prompt(error1, error2):
    return f"""
    You will receive below two errors found in Solidity smart contracts.
    Each error can be a textual description or a line number indicating where the error occurs.
    Analyze whether both errors refer to the same vulnerability/problem or not.
    Explain your reasoning before answering.
    If the errors are numbers, compare if they refer to the same line. If they are texts, compare the descriptions. If one is a number and the other is a text, try to match the line number with the correct error description.

    Error 1:
    {error1}

    Error 2:
    {error2}

    Respond in JSON format as follows:
    {{
        "same_error": true/false,
        "reasoning": "Brief explanation of your decision"
    }}
    """

def create_tot_error_comparison_prompt(error1, error2):
    return f"""
    You will receive below two errors found in Solidity smart contracts.
    Each error can be a textual description or a line number indicating where the error occurs.
    Explore multiple reasoning paths to decide whether both errors refer to the same vulnerability/problem or not.
    For each path, provide a detailed explanation of your analysis and then consolidate the findings to arrive at a final conclusion.
    If the errors are numbers, compare if they refer to the same line. If they are texts, compare the descriptions. If one is a number and the other is a text, try to match the line number with the correct error description.

    Error 1:
    {error1}

    Error 2:
    {error2}

    Respond in JSON format as follows:
    {{
        "same_error": true/false,
        "reasoning_paths": [
            {{
                "path": "Description of the reasoning path",
                "analysis": "Detailed analysis for this path"
            }},
            ...
        ],
        "final_reasoning": "Consolidated explanation based on all reasoning paths"
    }}
    """