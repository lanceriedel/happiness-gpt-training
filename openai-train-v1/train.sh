openai tools fine_tunes.prepare_data -f <LOCAL_FILE>
openai api fine_tunes.create -m ada --n_epochs 2     -t ./datasets/train6.jsonl 
