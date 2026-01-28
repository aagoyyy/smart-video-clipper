# 🎬 Smart Video Clipper

Upload video panjang → Dapetin clips pendek yang viral-ready!

## ✨ Features

- ✅ **AI-Powered Hook Detection** - Auto deteksi momen viral
- ✅ **Smart Context Analysis** - Hanya export clips berkualitas tinggi
- ✅ **Face-Tracking Crop** - Auto crop ke 9:16 (TikTok/Reels/Shorts)
- ✅ **Fast Processing** - 10 min video = 3-5 min processing
- ✅ **High Quality Output** - 8000k bitrate
- ✅ **No Subtitle** - Pure content focus (bisa add manual nanti)

## 🚀 Quick Start

### Option 1: Google Colab (Easiest)

1. Go to [Google Colab](https://colab.research.google.com/)
2. Upload `smart_clipper_ultimate.py`
3. Run the code below:

```python
!pip install openai-whisper moviepy torch opencv-python --break-system-packages -q

from google.colab import files
from smart_clipper_ultimate import SmartVideoClipperUltimate

# Upload video
uploaded = files.upload()
video_path = list(uploaded.keys())[0]

# Process
clipper = SmartVideoClipperUltimate()
clips, _ = clipper.create_clips(video_path)

# Download
for clip in clips:
    files.download(clip)
```

### Option 2: Streamlit Web App

1. Deploy to [Streamlit Cloud](https://streamlit.io/cloud) (FREE)
2. Upload files to GitHub
3. Connect & deploy
4. Get shareable URL!

See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for detailed instructions.

## 📊 How It Works

1. **Transcribe** - Extract text dengan Whisper AI
2. **Detect Hooks** - Find viral moments (power words, questions, etc)
3. **Analyze Quality** - Score berdasarkan 10+ faktor
4. **Smart Crop** - Track wajah untuk crop yang perfect
5. **Export** - High quality MP4 ready to post

## 🎯 Scoring System

**Total Score = Quality Score + Hook Score**

- **50+**: Viral Potential 🔥🔥🔥
- **40-49**: Excellent ⭐⭐⭐
- **30-39**: Very Good ⭐⭐
- **20-29**: Good ⭐
- **15-19**: Acceptable ✓
- **<15**: Not exported

## 💡 Customize per Niche

```python
clipper = SmartVideoClipperUltimate()

# Gaming
clipper.power_words = ['kill', 'ace', 'clutch', 'insane', 'epic']

# Business
# clipper.power_words = ['profit', 'uang', 'investasi', 'cuan']

# Tutorial
# clipper.power_words = ['cara', 'tutorial', 'tips', 'mudah']

clips, _ = clipper.create_clips(video_path)
```

## ⏱️ Processing Time

| Video Length | Processing Time |
|--------------|----------------|
| 5 min | 2-3 min |
| 10 min | 3-5 min ⭐ |
| 20 min | 6-10 min |
| 30 min | 10-15 min |

## 🆓 100% Free

- Google Colab: FREE (with GPU!)
- Streamlit Cloud: FREE (web app)
- Hugging Face: FREE (CPU)
- All code: Open source

## 📝 Requirements

- Python 3.10+
- FFmpeg
- 2GB+ RAM
- GPU recommended (optional)

## 🛠️ Tech Stack

- **Whisper AI** - Transcription
- **OpenCV** - Face detection
- **MoviePy** - Video processing
- **PyTorch** - AI models
- **Streamlit** - Web UI (optional)

## 📖 Documentation

- [Deployment Guide](DEPLOYMENT_GUIDE.md) - How to deploy
- [Ultimate Guide](ultimate_guide.py) - Full usage guide
- [Troubleshooting](DEPLOYMENT_GUIDE.md#troubleshooting) - Common issues

## 🎓 Use Cases

- Content creators (TikTok, Reels, Shorts)
- Podcasters (highlight clips)
- Educators (lesson snippets)
- Marketers (promo clips)
- Agencies (client deliverables)

## ⚡ Optimizations

- Model "small" (best speed/quality balance)
- Fast face detection (sample every 30 frames)
- Multi-threading export
- GPU acceleration
- Smart algorithms

## 🤝 Contributing

Contributions welcome! This is for personal use, but feel free to fork and improve.

## 📄 License

MIT License - Free to use for personal & commercial projects

## 🙏 Credits

Built with:
- OpenAI Whisper
- MoviePy
- OpenCV
- PyTorch

## 💪 Made for Content Creators

Automate your short-form content creation. Focus on creativity, let AI handle the rest! 🚀

---

**Questions?** Check the [Deployment Guide](DEPLOYMENT_GUIDE.md) or open an issue!
