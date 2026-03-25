from core.audio import record_audio
from core.transcription import transcribe_audio

# Step 1: Record audio
file = record_audio()

# Step 2: Convert to text
text = transcribe_audio(file)

print("\nTranscribed Text:")
print(text)