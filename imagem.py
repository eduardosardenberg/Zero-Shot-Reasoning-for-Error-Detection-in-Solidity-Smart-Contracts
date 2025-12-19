import pandas as pd
import matplotlib.pyplot as plt

data = [
    # LLM, Prompt, F1-Score

    ['gpt-4.1', 'zero-shot', 73.0],
    ['gpt-4o', 'zero-shot', 82.0],
    ['gpt-4.1', 'zero-shot-cot', 65.5],
    ['gpt-4o-mini', 'zero-shot', 72.4],
    ['gpt-4o', 'zero-shot-cot', 65.5],
    ['gpt-4o-mini', 'zero-shot-cot', 62.1],
    ['o4-mini', 'zero-shot-tot', 62.6],
    ['gpt-4.1-mini', 'zero-shot', 72.4],
    ['gpt-4.1-mini', 'zero-shot-cot', 62.1],
    ['gpt-4.1-nano', 'zero-shot-cot', 44.8],
    ['o1', 'zero-shot-cot', 72.6],
    ['gpt-4.1-nano', 'zero-shot', 69.0],
    ['o1', 'zero-shot', 69.0],
    ['o3-mini', 'zero-shot-cot', 61.2],
    ['o3-mini', 'zero-shot', 58.7],
    ['o4-mini', 'zero-shot-cot', 64.2],
    ['o4-mini', 'zero-shot', 61.5],
    ['gpt-4.1', 'zero-shot-tot', 69.0],
    ['gpt-4.1-mini', 'zero-shot-tot', 79.3],
    ['gpt-4o', 'zero-shot-tot', 82.8],
    ['gpt-4o-mini', 'zero-shot-tot', 79.3],
    ['gpt-4.1-nano', 'zero-shot-tot', 48.3],
    ['o1', 'zero-shot-tot', 71.3],
    ['o3-mini', 'zero-shot-tot', 57.4],
    ['gemini-2.0-flash', 'zero-shot', 71.2],
    ['gemini-2.0-flash', 'zero-shot-cot', 69.1],
    ['gemini-2.0-flash', 'zero-shot-tot', 59.0],
    ['gemini-2.5-flash', 'zero-shot', 44.0],
    ['gemini-2.5-flash', 'zero-shot-cot', 41.5],
    ['gemini-2.5-flash', 'zero-shot-tot', 44.5],
    # Claude
['Claude 3 Haiku', 'zero-shot', 71.5],
['Claude 3 Haiku', 'zero-shot-cot', 51.5],
['Claude 3 Haiku', 'zero-shot-tot', 51.7],

['Claude 3 Opus', 'zero-shot', 85.5],
['Claude 3 Opus', 'zero-shot-cot', 90.0],
['Claude 3 Opus', 'zero-shot-tot', 89.7],

# gemini-2.5-pro
['gemini-2.5-pro', 'zero-shot', 69.5],
['gemini-2.5-pro', 'zero-shot-cot', 59.0],
['gemini-2.5-pro', 'zero-shot-tot', 56.0],



]

df = pd.DataFrame(data, columns=['LLM', 'Prompt', 'F1-Score'])

# 1. Calcule o maior F1-Score de cada LLM
max_scores = df.groupby('LLM')['F1-Score'].max().sort_values(ascending=False)
llm_order = list(max_scores.index)

prompt_order = ['zero-shot-tot', 'zero-shot-cot', 'zero-shot']

df['LLM'] = pd.Categorical(df['LLM'], categories=llm_order, ordered=True)
df['Prompt'] = pd.Categorical(df['Prompt'], categories=prompt_order, ordered=True)
df = df.sort_values(['LLM', 'Prompt'])

plt.figure(figsize=(13, 4))
bar_width = 0.25
x = range(len(llm_order))
colors = ["#2878B5", "#F3933A", "#43B284"]

for i, prompt in enumerate(prompt_order):
    vals = []
    for llm in llm_order:
        val = df[(df['LLM'] == llm) & (df['Prompt'] == prompt)]['F1-Score']
        vals.append(val.values[0] if not val.empty else 0)
    bars = plt.bar([p + i*bar_width for p in x], vals, width=bar_width, label=prompt, color=colors[i])
    for idx, v in enumerate(vals):
        height = bars[idx].get_height()
        if v > 0:
            if v < 10:
                y = height * 0.55
                plt.text(idx + i*bar_width, y, f"{int(round(v))}",
                         ha='center', va='center', fontsize=8,
                         color='white', fontweight='bold', rotation=90)
            else:
                y = height - 2
                if height < 5:
                    y = height * 0.5
                plt.text(idx + i*bar_width, y, f"{v:.2f}",
                         ha='center', va='top', fontsize=10,
                         color='white', fontweight='bold', rotation=90)

plt.xticks([p + bar_width for p in x], llm_order, rotation=25)
plt.xlabel('LLM Base - Micro')
plt.ylabel('F1-Score (%)')
plt.legend(title="Reasoning")
plt.ylim(10, 100)
plt.tight_layout()
plt.show()