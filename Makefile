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

show_core_path:
	echo "~/.pyenv/versions/3.7.10/lib/python3.7/site-packages/retro/cores"

update_retro_arch_cores:
	cp ~/.pyenv/versions/3.7.10/lib/python3.7/site-packages/retro/cores/genesis_plus_gx_libretro.so ~/snap/retroarch/current/.config/retroarch/cores/
	cp ~/.pyenv/versions/3.7.10/lib/python3.7/site-packages/retro/cores/genesis_plus_gx.json ~/snap/retroarch/current/.config/retroarch/cores/
	cp ~/.pyenv/versions/3.7.10/lib/python3.7/site-packages/retro/cores/*.so ~/snap/retroarch/current/.config/retroarch/cores/
	cp ~/.pyenv/versions/3.7.10/lib/python3.7/site-packages/retro/cores/*.json ~/snap/retroarch/current/.config/retroarch/cores/
	
update_states_for_kabal:
	cp ~/snap/retroarch/current/.config/retroarch/states/Mortal\ Kombat\ 3\ \(USA\).state7 ~/.pyenv/versions/3.7.10/lib/python3.7/site-packages/retro/data/MortalKombat3-Genesis/kabal2.state
	gzip ~/.pyenv/versions/3.7.10/lib/python3.7/site-packages/retro/data/MortalKombat3-Genesis/kabal2.state
	mv ~/.pyenv/versions/3.7.10/lib/python3.7/site-packages/retro/data/MortalKombat3-Genesis/kabal2.state.gz ~/.pyenv/versions/3.7.10/lib/python3.7/site-packages/retro/data/MortalKombat3-Genesis/kabal2.state
	cp ~/.pyenv/versions/3.7.10/lib/python3.7/site-packages/retro/data/MortalKombat3-Genesis/kabal2.state ./
