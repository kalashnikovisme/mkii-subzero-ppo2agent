# Mortal Kombat II - Sub-Zero PPO2 Agent

## Video: https://youtu.be/-oUVr_B_cQo

The final Sub-Zero model I demo'ed in the video: https://drive.google.com/file/d/1_jyXBvkc7t1KzemiBqWyAsFkDGeqzsSd/view?usp=sharing  
The second-last model I demo'ed in the video, it's the same one but before I trained it specifically on the Baraka fight (works better on the first 4 fights): https://drive.google.com/file/d/1DZtZyaWInQlageeaBpAjupA9nj6S3kyA/view?usp=sharing

## Setup:
1. Install python 3.7.10 via `pyenv install 3.7.10`
2. Install pip packages and any dependencies `poetry install`
3. Find a Mortal Kombat II Sega Genesis ROM and install it with ```poetry run python -m retro.import ./```
4. Copy the save SubZeroState.state, scenario.json (reward function definition), metadata.json in gym-retro-files to retro package installation directory

```
cp gym-retro-files/SubZeroState.state ~/.cache/pypoetry/virtualenvs/mk3-train-GItkoUO3-py3.7/lib/python3.7/site-packages/retro/data/stable/MortalKombat3-Genesis/
cp gym-retro-files/scenario.json ~/.cache/pypoetry/virtualenvs/mk3-train-GItkoUO3-py3.7/lib/python3.7/site-packages/retro/data/stable/MortalKombat3-Genesis/
cp gym-retro-files/metadata.json ~/.cache/pypoetry/virtualenvs/mk3-train-GItkoUO3-py3.7/lib/python3.7/site-packages/retro/data/stable/MortalKombat3-Genesis/
```

Now you can play around with the train.py and play.py scripts

Refer to the Gym Retro docs for more info: https://retro.readthedocs.io/en/latest/index.html
