# Detect Sound

A simple Python script that listens to your microphone and prints `"sound detected"` whenever it detects audio above a specified volume threshold.

## Requirements

- Python 3.6+
- [sounddevice](https://pypi.org/project/sounddevice/)
- numpy

Install dependencies with:

```bash
pip install sounddevice numpy
```
### output
```
Listening...
sound detected
sound detected
...
```

### Parameters

#### Adjust these
- threshold
```
threshold = 0.1  # Lower = more sensitive
```
- Duration
```
duration = 0.5  # Seconds per audio chunk
```

### Troubleshooting
If you encounter an error like PortAudioError: Error opening InputStream, it may be due to:
- Mic permissions not granted (Windows: Settings → Privacy → Microphone)
- Another application using the microphone
- No input device available
