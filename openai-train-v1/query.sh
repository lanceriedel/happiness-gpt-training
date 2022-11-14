openai api completions.create -m ada:ft-personal-2022-11-08-22-31-51 -p "how to open up about how hard it is to be a parent"
openai api fine_tunes.create -m ada --n_epochs 2     -t ./datasets/train6.jsonl 
