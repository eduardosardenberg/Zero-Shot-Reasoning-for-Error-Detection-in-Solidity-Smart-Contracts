def create_zeroshot_prompt(file_path):
    return f"""
    Analyze the following Solidity and determine if it contains errors.
    Code:
    {open(file_path, 'r', encoding='utf-8').read()}

    Respond in JSON format with the following structure:
    {{
        "has_error": true/false
    }}
    """

def create_zeroshot_cot_prompt(file_path):
    return f"""
    Analyze the following Solidity code and determine if it contains errors. 
    Provide a step-by-step explanation of your reasoning before arriving at a conclusion.
    Code:
    {open(file_path, 'r', encoding='utf-8').read()}

    Respond in JSON format with the following structure:
    {{
        "has_error": true/false,
        "reasoning": "Step-by-step explanation of the analysis"
    }}
    """

def create_zeroshot_tot_prompt(file_path):
    return f"""
    Analyze the following Solidity code and determine if it contains errors. 
    Explore multiple reasoning paths to evaluate the code comprehensively. 
    For each path, provide a detailed explanation of your analysis and then consolidate the findings to arrive at a final conclusion.
    Code:
    {open(file_path, 'r', encoding='utf-8').read()}

    Respond in JSON format with the following structure:
    {{
        "has_error": true/false,
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