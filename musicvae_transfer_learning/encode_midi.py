import magenta.music as mm
import magenta.models.music_vae.trained_model as trained_model
from magenta.models.music_vae.configs import CONFIG_MAP


def encode_midi(midi_file_path, checkpoint_file_path, model_type="hierdec-mel_16bar"): 
	tm = trained_model.TrainedModel(config=CONFIG_MAP[model_type], 
									batch_size=1, 
									checkpoint_dir_or_path=checkpoint_file_path)
	note_seq = mm.midi_file_to_note_sequence(midi_file)
	extracted_tensors = tm._config.data_converter.to_tensors(note_seq)
	inputs = [extracted_tensors.inputs[i] for i in range(len(extracted_tensors))]
	controls = [extracted_tensors.controls[i] for i in range(len(extracted_tensors))]
	lengths = [extracted_tensors.lengths[i] for i in range(len(extracted_tensors))]
	encoded_vectors = tm.encode_tensors(inputs, lengths, controls)
	return encoded_vectors