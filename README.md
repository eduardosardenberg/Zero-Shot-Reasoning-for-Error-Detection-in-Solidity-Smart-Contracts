# Smart-Contract-LLM-Evaluation

This repository provides datasets and source code for evaluating the capabilities of large language models (LLMs) in both detecting and explaining vulnerabilities in Solidity smart contracts. It supports zero-shot experiments across different reasoning strategies and includes both quantitative (e.g., F1-score) and qualitative (e.g., explanation correctness, completeness, and clarity) evaluation.

---

## Project Structure

```
Datasets/
    bugLocation.json
    dataset.csv
    DAppSCAN-main/
    JiuZhou/
    openzeppelin-contracts-master/
    v2-core-master/
    v3-core-main/
src/
    dataset_analysis/
        dataset_analysis.ipynb
        dataset_analysis.csv
    experiments/
        gpt_4.1.ipynb
        gpt_4.1-mini.ipynb
        gpt_4.1-nano.ipynb
        gpt_4o.ipynb
        gpt_4o_mini.ipynb
        o1.ipynb
        o3-mini.ipynb
        o4-mini.ipynb
        libs/
            exp_utils.py
            openai.py
            prompts.py
requirements.txt
.env
```

---

## Main Components

- **.env**: Environment variables for API keys and configuration.
- **Datasets/**: Contains datasets and Solidity source code from various audits and projects.
    - `dataset.csv`: Main dataset with vulnerability annotations.
    - `bugLocation.json`: Ground truth metadata for vulnerability locations.
    - Subfolders (e.g., `DAppSCAN-main/`, `JiuZhou/`, etc.): Source files and audits.
- **src/dataset_analysis/**: Code and notebooks for statistical and qualitative exploration of the dataset.
- **src/experiments/**: Zero-shot experiments using various LLMs and reasoning strategies.
    - `libs/exp_utils.py`: Utilities for both quantitative and qualitative evaluation.
    - `libs/openai.py`: OpenAI API wrapper.
    - `libs/prompts.py`: Prompt templates for each reasoning technique.
- **requirements.txt**: Python dependencies for running the project.

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
    - Create a `.env` file in the root directory:
      ```
      OPENAI_API_KEY=your_openai_api_key_here
      ```

---

## Usage

### Dataset Analysis

Run:
```sh
jupyter notebook src/dataset_analysis/dataset_analysis.ipynb
```
- Explore dataset statistics, distributions, and examples.
- Perform qualitative analysis, such as manual review of explanations and comparison with ground truth.

### Running Experiments

Open any notebook in `src/experiments/` to:
- Load the dataset
- Generate prompts for different models and reasoning strategies
- Query LLMs
- Evaluate both detection metrics and explanation quality

Example:
```sh
jupyter notebook src/experiments/gpt_4o.ipynb
```

### Qualitative Analysis

- Qualitative analysis can be performed manually or using scripts/notebooks.
- Compare model-generated explanations with ground truth (`bugLocation.json`).
- Use criteria such as correctness, completeness, clarity, and consistency.
- For manual evaluation, record observations and notes in spreadsheets or Markdown files.
- For automated evaluation, use functions in `exp_utils.py` or create custom scripts.

---

## Evaluation Criteria

- **Quantitative (Detection)**: Precision, recall, F1-score for binary vulnerability detection.
- **Qualitative (Explanation)**: Correctness, completeness, clarity, and consistency of model-generated explanations compared to ground truth.

---

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve this project, add new qualitative analysis scripts, or suggest experiment adjustments.

---

## License

Please refer to the LICENSE files in dataset subfolders. This project is intended for academic research and educational purposes only.

---

**Contact**  
Open an issue or reach out to the maintainer via GitHub for questions or collaboration.
