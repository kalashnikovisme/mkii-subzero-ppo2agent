install:
	echo "Install cmake"
	pyenv exec python -m pip install -r requirements.txt
	pyenv exec python -m retro.import ./

train:
	pyenv exec python train.py

play:
	pyenv exec python play.py

docker_build:
	docker build . -t mk3-train

docker_train:
	docker run mk3-train
