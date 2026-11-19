# bleepy

A simple foul language filter for Python.

## Installation

```bash
pip install bleepy
```

## Usage

```python
from bleepy import Bleepy

b = Bleepy()

b.clean("What the hell is going on?")
# "What the **** is going on?"

b.contains("This is clean text")
# False
```

## License

TBD
