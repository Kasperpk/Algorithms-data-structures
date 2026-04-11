# AI Agent Instructions for Data Structures and Algorithms Specialization

## Project Overview
This repository contains educational Python implementations of classic algorithms and data structures from the Coursera specialization. The code prioritizes clarity and learning over production optimization.

## Repository Structure
- `/algorithms/courses/` - Course assignments (Coursera, etc.)
- `/algorithms/textbooks/` - Textbook exercises (Cormen/CLRS, etc.)
- `/algorithms/practice/` - Platform-based practice (CSES, LeetCode, Exercism, Project Euler)
- `/algorithms/python-concepts/` - Python language notes and experiments
- `/data-structures/` - Data structure implementations and notes

## Code Patterns & Conventions

### Algorithm Implementation Pattern
1. Each algorithm has a primary function with comprehensive docstrings:
```python
def algorithm_name(param1, param2, ...):
    """
    Description of what the algorithm does.
    
    Args:
        param1: Description
        param2: Description
    
    Returns:
        Description of return value
        
    Time complexity: O(...)
    Space complexity: O(...)
    """
```

2. Multiple variants are implemented as separate functions with descriptive suffixes:
   - Base version: `function_name()`
   - Optimized version: `function_name_optimized()`
   - Extended functionality: `function_name_with_x()`

### Input/Output Convention
All solution files follow the Coursera course format:
```python
if __name__ == "__main__":
    # Read input in specified format
    n = int(input())
    values = list(map(int, input().split()))
    
    # Call algorithm
    result = algorithm_name(values)
    
    # Print output in required format
    print(result)
```

### Jupyter Notebook Organization
Notebooks (`*.ipynb`) contain:
1. Problem statement/theory explanation in markdown
2. Implementation with detailed comments
3. Example usage and test cases
4. Visualization of algorithm behavior where applicable

## Common Development Tasks

### Running Solutions
1. Navigate to solution directory:
```bash
cd algorithms/practice/cses/
```
2. Run with input from file:
```bash
python3 algorithm_name.py < input.txt
```

### Working with Notebooks
1. Textbook exercises as notebooks:
   - `/algorithms/textbooks/cormen/`

2. Course work:
   - `/algorithms/courses/coursera-algorithmic-toolbox/`

## Key Reference Examples

1. Graph Algorithm Pattern:
   - Example: `algorithms/textbooks/cormen/20.2.ipynb`
   - Demonstrates graph representation and traversal techniques

2. Practice Problem Pattern:
   - Example: `algorithms/practice/cses/apartments.py`
   - Shows clean solution files with docstrings

3. LeetCode by Topic:
   - Example: `algorithms/practice/leetcode/graphs/`
   - Topic-based organization for focused practice