



#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show() 
# Click on the code lens Run Cell
# Run Cell Hot key as in Chrome

# If you want to run cell with Ctrl+Enter, add those code in keybindings.json.
# { "key": "ctrl+enter",      "command": "jupyter.execCurrentCell",
#                                   "when": "editorTextFocus"
# }
# Remote Jupyter kernel on Server / Docker

# Try this to connect to a remote Jupyter kernel running on a server, or inside Docker container:

# Start a remote Jupyter Notebook or headless KernelGateway
# Find the token in the output of the Jupyter server logs: http://jupyter-notebook.readthedocs.io/en/latest/security.html
# Then in VS Code:

# ctrl+shift+p
# Jupyter: Enter the url of local/remote Jupyter Notebook
