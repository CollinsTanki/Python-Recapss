from pathlib import Path


path = Path()
#print(path.mkdir())
for file in path.glob('*'):
    print(file)