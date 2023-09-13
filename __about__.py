import os.path

__all__ = [
    "__title__",
    "__summary__",
    "__url__",
    "__version__",
    "__commit__",
    "__author__",
    "__email__",
    "__license__",
    "__copyright__",
]


try:
    base_dir = os.path.dirname(os.path.abspath(__file__))
except NameError:
    base_dir = None


__title__ = "PlugNLP"
__summary__ = "Use NLP service anywhere, anytime. 开箱即用的 NLP 工具池"
__url__ = "https://github.com/A-baoYang/PlugNLP"
__version__ = "0.0.1"

if base_dir is not None and os.path.exists(os.path.join(base_dir, ".commit")):
    with open(os.path.join(base_dir, ".commit")) as fp:
        __commit__ = fp.read().strip()
else:
    __commit__ = None

__author__ = "A-baoYang"
__email__ = "martech.tw@gmail.com"
__license__ = "Apache License, Version 2.0"
__copyright__ = "2023 %s" % __author__
