def create_multiclass_prompt(file_path, file_name, taxonomy):
    return f"""
    Consider the following taxonomy of possible error types:
    {taxonomy}

    Given the following code snippet: {file_name}

    Identify which category from the taxonomy best describes the error in the code.
    If there is no error, respond with "NONE".

    Return the result in valid JSON format:
    {{
        "bug_type": "name of the category or 'NONE'",
        "location": "line number where the error occurs, or 0 if none"
    }}

    Code:
    {open(file_path, 'r', encoding='utf-8').read()}
    """

def create_multiclass_prompt_cot(file_path, file_name, taxonomy):
    return f"""
    You are an expert in smart contract security analysis.

    Consider the following taxonomy of possible error types:
    {taxonomy}

    Given the following code snippet: {file_name}

    Think step-by-step to determine whether an error exists and which category it belongs to.

    Respond ONLY in JSON format as follows:
    {{
        "has_error": true/false,
        "bug_type": "type of the bug if any, otherwise 'NONE'",
        "location": "line number of where the error is located, otherwise 0 if no error",
        "reasoning": "Step-by-step explanation of the analysis"
    }}

    Code:
    {open(file_path, 'r', encoding='utf-8').read()}
    """
def create_multiclass_prompt_tot(file_path, file_name, taxonomy):
    return f"""
    You are an expert in smart contract security analysis.

    Consider the following taxonomy of possible error types:
    {taxonomy}

    Analyze the following code snippet: {file_name}
    using a Tree-of-Thought reasoning process to determine whether it contains an error and which category from the taxonomy best describes it.

    Instructions:
    - Respond ONLY with a strictly valid JSON object, nothing else.
    - Use at least 5 reasoning paths.
    - The JSON must be valid, compact (no line breaks inside fields), and fit in a single output.
    - Do NOT use markdown code blocks, explanations, or any content before or after the JSON.
    - The "path" field MUST be a short summary (max 8 words).
    - The "analysis" field MUST be concise (max 20 words) and should not repeat the "path".
    - The JSON must follow exactly the field order below.

    Required JSON format and field order:
    {{
        "has_error": true/false,
        "location": "line number of where the error is located, otherwise 0 if no error",
        "reasoning_paths": [
            {{
                "path": "Description of the reasoning path",
                "analysis": "Detailed analysis for this path"
            }},
            {{
            
            }}, ...
        ],
        "final_reasoning": "Consolidated explanation based on all reasoning paths",
        "bug_type": "Type of vulnerability or error from the taxonomy, or 'NONE'"
    }}

    Code:
    {open(file_path, 'r', encoding='utf-8').read()}
    """

def create_zeroshot_locate_prompt(file_path):
    return f"""
    Analyze the following Solidity code. Carefully review the following Solidity code and determine if it contains any errors or vulnerabilities.

    If you identify a bug or vulnerability, specify:
    - The type of bug or vulnerability in the "bug_type" field.

    If you do NOT find any bug or vulnerability, set the value "NONE" for "bug_type".
    If you find a bug, specify the line number where the error is located in the "location" field. If no error is found, set "location" to 0.

    Respond in JSON format:
    {{
        "has_error": true/false,
        "location": "line number of where the error is located, otherwise 0 if no error",
        "bug_type": "type of the bug if any, otherwise 'NONE'"   
    }}

    Code:
    {open(file_path, 'r', encoding='utf-8').read()}
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

    **IMPORTANT:**
    - Respond ONLY with a valid JSON object in a **single line**.
    - Do NOT use Markdown formatting, code blocks, or any text outside the JSON.
    - Do NOT insert any real line breaks or ENTERs inside the JSON fields; keep everything in one line.
    - If you need to separate steps in the reasoning field, use the escape sequence `\\n` (two characters: backslash + n).
    - Do NOT include any explanations, formatting, or commentary outside the JSON object.

    Respond ONLY in JSON format as follows:
    {{
        "has_error": true/false,
        "bug_type": "type of the bug if any, otherwise NONE",
        "location": "line number of where the error is located, otherwise 0 if no error",
        "reasoning": "Step-by-step explanation of the analysis"
    }}

    Code:
    {open(file_path, 'r', encoding='utf-8').read()}
    """

def create_zeroshot_tot_locate_prompt(file_path):
    return f"""
    Analyze the following Solidity code by considering multiple possible reasoning paths (tree-of-thought) to determine whether it contains any errors or vulnerabilities.

    Instructions:
    - Respond ONLY with a strictly valid JSON object, nothing else.
    - The JSON must contain ONLY the fields: has_error, location, bug_type.
    - Do NOT output reasoning_paths, final_reasoning or any other field.
    - The first character must be '{' and the last character must be '}'.

    - Do NOT use markdown code blocks (no triple backticks), explanations, or any content before or after the JSON.
    - The "reasoning_paths" array MUST contain only ONE item.
    - The "path" field MUST be a short summary (no more than 8 words), not an explanation.
    - The "analysis" field MUST be no more than 20 words.
    - Do not repeat or restate the explanation in the "path" field.
    - The JSON must be valid, compact (no line breaks inside fields), and fit in a single output.

    Required JSON format and field order:
    {{
        "has_error": true/false,
        "location": "line number of where the error is located, otherwise 0 if no error",
        "reasoning_paths": [
            {{
                "path": "Description of the reasoning path",
                "analysis": "Detailed analysis for this path"
            }}
        ],
        "final_reasoning": "Consolidated explanation based on all reasoning paths",
        "bug_type": "Type of vulnerability or error, or 'NONE'"
    }}

    Code:
    {open(file_path, 'r', encoding='utf-8').read()}
    """