
#### 4. **setup.py**
Create a `setup.py` file to package the project:
```python
from setuptools import setup, find_packages

setup(
    name='agricultural_yield_analysis',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'scikit-learn'
    ],
    entry_points={
        'console_scripts': [
            'agricultural_yield_analysis=src.main:main',
        ],
    },
)
