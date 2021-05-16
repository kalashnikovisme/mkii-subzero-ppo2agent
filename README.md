# Mortal Kombat II - Sub-Zero PPO2 Agent

## Video: https://youtu.be/-oUVr_B_cQo

The final Sub-Zero model I demo'ed in the video: https://drive.google.com/file/d/1_jyXBvkc7t1KzemiBqWyAsFkDGeqzsSd/view?usp=sharing  
The second-last model I demo'ed in the video, it's the same one but before I trained it specifically on the Baraka fight (works better on the first 4 fights): https://drive.google.com/file/d/1DZtZyaWInQlageeaBpAjupA9nj6S3kyA/view?usp=sharing

## Setup:
1. Install python 3.7.10 via `pyenv install 3.7.10`
2. Install pip packages and any dependencies `poetry install`
3. Find a Mortal Kombat II Sega Genesis ROM and install it with ```poetry run python -m retro.import /path/to/your/ROMs/directory/```
4. Copy the save states and the scenario.json (reward function definition) in gym-retro-files to /your-pip-install-folder/retro/data/stable/MortalKombatII-Genesis

Now you can play around with the train.py and play.py scripts

Refer to the Gym Retro docs for more info: https://retro.readthedocs.io/en/latest/index.html
