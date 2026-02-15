import numpy as np
import soundfile as sf
import os

# =========================
# MATCHED SETTINGS
# =========================
sample_rate = 44100
beep_duration = 0.05     # 50 ms
cycle_duration = 0.2      # 200 ms
gap_duration = cycle_duration - beep_duration     # 100 ms
frequency = 400           # Hz
amplitude = 0.4

output_folder = "audio_stimuli"
os.makedirs(output_folder, exist_ok=True)

# =========================
# GENERATE FILES
# =========================
for n_beeps in range(10, 21):

    t = np.linspace(0, beep_duration,
                    int(sample_rate * beep_duration),
                    False)

    beep = amplitude * np.sin(2 * np.pi * frequency * t)
    silence = np.zeros(int(sample_rate * gap_duration))

    full_signal = np.array([])

    for _ in range(n_beeps):
        full_signal = np.concatenate((full_signal, beep, silence))

    # Remove last silence
    full_signal = full_signal[:-len(silence)]
    filename = os.path.join(output_folder,f"A{n_beeps}.wav")
    sf.write(f"{output_folder}/A{n_beeps}.wav",
             full_signal,
             sample_rate)

    print(f"A{n_beeps}.wav generated")

print("All files recreated successfully.")
