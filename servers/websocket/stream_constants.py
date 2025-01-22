# Constants

Vocals: list[int] = [50, 1000]  # Frequency range to detect sounds that could be speech

SampleRate = 24000  # Stream device recording frequency per second --> !!! Must be set like this to avoid conflict with the audio returned from the OpenAI TTS API !!!
BlockSizeMs = 30  # Block size in milliseconds
BlockSize=int(SampleRate * BlockSizeMs / 1000) # block size in sample captures


# 33 blocks = 1 second (aprox)
EndBlocks = 50  # ~33x1,5 Number of blocks to wait before sending (30 ms is block)
FlushBlocks = 33 * 25  # Number of blocks to wait before sending
ConnectionBlocks = 33 * 5 # Number of blocks to start saving the audio data to a new buffer before sending in order to preserve context