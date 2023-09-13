import sys
from test_data import prompt_template, bad_financial_nouns
from pathlib import Path

sys.path.append("..")

from PlugNLP.cleansing import TextCleanser


root_dir = Path(__file__).absolute().parents[0]

textcleanser = TextCleanser()
textcleanser.set_prompt(
    role="user", prompt_template=prompt_template, inputs=bad_financial_nouns
)
result = textcleanser.run(run_name="TEJ_bad_nouns_cleansing", output_dir="output_data")

name_correction = {}
for cl in result:
    name_correction.update(eval(cl))
