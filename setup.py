import os

from setuptools import find_packages, setup

cwd = os.path.dirname(os.path.abspath(__file__))
about_path = os.path.join(cwd, "__about__.py")
print(about_path)

about = {}
with open(file=about_path, mode="r", encoding="utf-8") as f:
    exec(f.read(), about)

requires_path = os.path.join(cwd, "requirements.txt")
with open(file=requires_path, mode="r", encoding="utf-8") as f:
    requires = f.read().split("\n")

setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__summary__"],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author=about["__author__"],
    author_email=about["__email__"],
    url=about["__url__"],
    packages=find_packages() + [about["__title__"]],  # dependencies
    data_files=["__about__.py", "requirements.txt"],
    python_requires=">=3.8",  # Python version requires
    install_requires=requires,
    zip_safe=False,
    # entry_points={
    #     "console_scripts": ["RippleFiNER-inference = RippleFiNER.inference:main"]
    # },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence :: Natural Language Generation :: OpenAI",  # noqa E501
    ],
    license=about["__license__"],
    keywords="gpt openai nlp classification extraction question-answering summarization chat generation",  # noqa E501
)
