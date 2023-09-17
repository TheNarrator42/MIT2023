import os

userPrompt = 'Confucious the Philosopher'

input = "\"" + userPrompt + "\""

terminalPrompt = "modal run backend/stable_diffusion_cli.py --prompt " + str(input)
os.system(terminalPrompt)