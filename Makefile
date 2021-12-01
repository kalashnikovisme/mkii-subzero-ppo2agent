install:
	echo "Install cmake"
	pyenv exec python -m pip install -r requirements.txt
	cp gym-retro-files/scenario.json ~/.cache/pypoetry/virtualenvs/mk3-train-GItkoUO3-py3.7/lib/python3.7/site-packages/retro/data/stable/MortalKombat3-Genesis/
	cp gym-retro-files/metadata.json ~/.cache/pypoetry/virtualenvs/mk3-train-GItkoUO3-py3.7/lib/python3.7/site-packages/retro/data/stable/MortalKombat3-Genesis/
	pyenv exec python -m retro.import ./

train:
	pyenv exec python train.py

docker_build:
	docker build . -t mk3-train

docker_train:
	docker run mk3-train
