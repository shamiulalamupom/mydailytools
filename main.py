import os
from pathlib import Path
import pickle

Path(f'{os.getcwd()}/todo_list.pkl').touch()
with open('todo_list.pkl', 'wb') as file:
    pickle.dump([], file)
