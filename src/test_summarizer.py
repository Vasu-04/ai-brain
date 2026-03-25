from core.audio import record_audio
from core.transcription import transcribe_audio
from core.summarizer import summarize_text

# Step 1: Record audio
file = record_audio()

# Step 2: Convert to text
text = transcribe_audio(file)
# text = "Due to ongoing Iran Israel war, the global economy is facing significant challenges. The conflict has disrupted supply chains, leading to increased costs for goods and services worldwide. Additionally, the war has caused a surge in oil prices, further exacerbating inflation and putting additional strain on consumers and businesses alike. The geopolitical instability has also led to decreased investor confidence, resulting in market volatility and economic uncertainty. Dollars price is also increasing due to the war, as investors seek safe-haven assets amidst the turmoil. and in India, the gold price decreasing due to the war, as investors shift their focus towards other assets amidst the geopolitical tensions"

# Step 3: Summarize
result = summarize_text(text)

print("\n--- FINAL OUTPUT ---")
print(f"Date: {result['date']}")
print(f"Time: {result['time']}")
print("\nSummary:")
print(result['summary'])