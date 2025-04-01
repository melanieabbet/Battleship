
#obsidian
Inside the [[Asset]] folder we have all class used as game elements:


# [[Class Grid]]

The grid is the playground class.

It is made of [[Class Cell]] instance and has dictionary where they are mapped with there [[Class Coordinate]] self instance

the [[Class Grid]] also have an size attribute who is set at the instance construction

```python

class Grid

	def __init__(self, size):
		self.size = size
		self.grid = {}
```

the variable grid is a dictionary where the key is the [[Class Cell]] coordinate and the value the [[Class Cell]]

so a cell can be acces like this:
```python
cell = Grid[Coordinate]
```
