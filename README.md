# py4N-gram

N-gram Python Library

## Getting Started

This project is simply implementation of N-gram algorithm in python programming language.

### Prerequisites

This Project Has No Prerequisites


### Installing

The easiest way to install py4N-gram is using pip

```
pip install py4N-gram
```

### Usage
It's only a function named Ngram. It takes 2 argument, the first argument is the text and the second argument is the number of N.
```
from py4N_gram.tokenize import Ngram
x = "i love python programming language"
unigram = Ngram(x,1)
bigram = Ngram(x,2)
trigram = Ngram(x,3)
```
