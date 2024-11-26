from typing import Any, List, Optional
from pydantic import BaseModel

def generate_wav(bird_list):
	from diffusers import AudioLDM2Pipeline
	import torch
	import scipy

	repo_id = "cvssp/audioldm2"
	device = "cuda" if torch.cuda.is_available() else "cpu"

	pipe = AudioLDM2Pipeline.from_pretrained(repo_id, torch_dtype=torch.float16).to(device)

	birds_string = ", ".join(bird_list)
	prompt = "dawn chorus containing the following birds: {birdlist}.".format(birdlist=birds_string)

	sample_rate = 16000
	audio = pipe(prompt, num_inference_steps=200, audio_length_in_s=10.0).audios[0]

	#scipy.io.wavfile.write("techno.wav", rate=sample_rate, data=audio)
	#display(Audio(audio, rate=sample_rate))

	return (audio, sample_rate)
