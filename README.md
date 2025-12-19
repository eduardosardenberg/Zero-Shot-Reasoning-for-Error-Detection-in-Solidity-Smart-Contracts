# Smart-Contract-LLM-Evaluation

This repository provides datasets and code to evaluate the ability of LLMs to detect and explain vulnerabilities in Solidity smart contracts. It supports zero-shot experiments with different reasoning strategies and includes both quantitative and qualitative evaluations.

---

## Project Structure

```
src/
├── dataset_analysis/
│   ├── dataset_analysis.csv
│   └── dataset_analysis.ipynb
├── experiments/
│   ├── __init__.py
│   ├── anthropic_models/
│   │   ├── claude-3-haiku.ipynb
│   │   ├── claude-3-opus.ipynb
│   │   └── claude-3-sonnet.ipynb
│   ├── gemini_models/
│   │   ├── gemini-1.5-flash.ipynb
│   │   ├── gemini-2.0-flash.ipynb
│   │   └── gemini-2.0-pro.ipynb
│   ├── gpt_models/
│   │   ├── __init__.py
│   │   ├── gpt_4.1-mini.ipynb
│   │   ├── gpt_4.1-nano.ipynb
│   │   ├── gpt_4.1.ipynb
│   │   ├── gpt_4o_mini.ipynb
│   │   ├── gpt_4o.ipynb
│   │   ├── o1.ipynb
│   │   ├── o3-mini.ipynb
│   │   └── o4-mini.ipynb
│   └── libs/
│       ├── __init__.py
│       ├── anthropic_lib.py
│       ├── exp_utils.py
│       ├── gemini_lib.py
│       ├── openai_lib.py
│       └── prompts.py
│       └── __pycache__/
```

---

## Main Components

- `dataset_analysis/`: Exploratory analysis of the dataset.
    - `dataset_analysis.csv`: Main dataset with vulnerability annotations.
    - `dataset_analysis.ipynb`: Notebook for dataset exploration and statistics.
- `experiments/anthropic_models/`: Notebooks for experiments with Claude 3 models (Haiku, Opus, Sonnet).
- `experiments/gemini_models/`: Notebooks for experiments with Gemini models (1.5, 2.0, Flash, Pro).
- `experiments/gpt_models/`: Notebooks for experiments with GPT models (4.1, 4o, nano, mini, etc).
- `experiments/libs/`: Utilities and wrappers for APIs, prompts, and evaluation functions.
    - `exp_utils.py`: Functions for quantitative and qualitative evaluation.
    - `prompts.py`: Prompt templates for each reasoning technique.
    - `openai_lib.py`, `gemini_lib.py`, `anthropic_lib.py`: API wrappers for each LLM provider.
- `bugLocationDappScan.json`: Ground truth metadata for vulnerability locations (used in experiments).
- Other subfolders (e.g., `DAppSCAN-main/`, `JiuZhou/`): Source files and audits for smart contracts (if present in your dataset root).

---

## Installation

1. **Clone the repository**
    ```sh
    git clone <repo-url>
    cd <repo-folder>
    ```

2. **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```

3. **Configure environment variables**
    - Create a `.env` file in the root directory, for example:
      ```
      OPENAI_API_KEY=your_openai_api_key
      GEMINI_API_KEY=your_gemini_api_key
      ANTHROPIC_API_KEY=your_anthropic_api_key
      DATASET_PATH=src/dataset_analysis/dataset_analysis.csv
      ```

---

## Usage

### Dataset Analysis

Open:
```sh
jupyter notebook src/dataset_analysis/dataset_analysis.ipynb
```
- Explore dataset statistics, distributions, and examples.
- Perform manual qualitative analysis of explanations and comparison with ground truth.

### Running Experiments

Open any notebook in `src/experiments/` to:
- Load the dataset
- Generate prompts for different models and strategies
- Query LLMs
- Evaluate detection metrics and explanation quality

Example:
```sh
jupyter notebook src/experiments/gpt_models/gpt_4o.ipynb
```

### Qualitative Analysis

- Can be performed manually or using scripts/notebooks.
- Compare model-generated explanations with ground truth (`bugLocation.json`).
- Use criteria such as correctness, completeness, clarity, and consistency.
- For manual evaluation, record observations in spreadsheets or Markdown files.
- For automated evaluation, use functions in `exp_utils.py` or create custom scripts.

---

## Evaluation Criteria

- **Quantitative (Detection):** Precision, recall, F1-score for binary vulnerability detection.
- **Qualitative (Explanation):** Correctness, completeness, clarity, and consistency of explanations.

---

## Contributing

Contributions are welcome! Submit issues or pull requests to improve the project, add qualitative analysis scripts, or suggest experiment adjustments.

Refer to the LICENSE files in dataset subfolders. This project is for academic and educational purposes only.

---

**Contact**
Open an issue or reach out via GitHub for questions or collaboration.
