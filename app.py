"""
Smart Video Clipper - Streamlit App
FREE Deployment untuk Personal Use
"""

import streamlit as st
from smart_clipper_ultimate import SmartVideoClipperUltimate
import os
import shutil
import json

# Page config
st.set_page_config(
    page_title="Smart Video Clipper",
    page_icon="🎬",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 1rem;
    }
    .subtitle {
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .stButton > button {
        width: 100%;
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 0.75rem;
    }
    .clip-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">🎬 Smart Video Clipper</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Upload video panjang → Dapetin clips pendek yang viral-ready!</div>', unsafe_allow_html=True)

# Sidebar - Settings
with st.sidebar:
    st.header("⚙️ Settings")
    
    st.markdown("### 📏 Clip Settings")
    duration = st.slider(
        "Target Duration (detik)", 
        min_value=20, 
        max_value=60, 
        value=45,
        help="Durasi ideal per clip (20-60 detik)"
    )
    
    max_clips = st.slider(
        "Maksimal Clips", 
        min_value=3, 
        max_value=10, 
        value=5,
        help="Berapa banyak clips yang mau dibuat"
    )
    
    st.markdown("### 🌍 Language")
    language = st.selectbox(
        "Bahasa Video",
        ["auto", "id", "en"],
        help="'auto' untuk auto-detect, 'id' untuk Indonesia, 'en' untuk English"
    )
    
    st.markdown("### 🎯 Custom Power Words")
    use_custom = st.checkbox("Customize Power Words")
    
    custom_words = ""
    if use_custom:
        niche = st.selectbox(
            "Pilih Niche",
            ["Custom", "Gaming", "Bisnis/Finance", "Tutorial", "Lifestyle"]
        )
        
        if niche == "Gaming":
            custom_words = "kill, ace, clutch, insane, epic, legendary, headshot, pentakill, pro, god"
        elif niche == "Bisnis/Finance":
            custom_words = "profit, uang, investasi, bisnis, passive income, jutaan, milyaran, cuan, money, rich"
        elif niche == "Tutorial":
            custom_words = "cara, tutorial, tips, trik, mudah, simple, cepat, gampang, rahasia, how to"
        elif niche == "Lifestyle":
            custom_words = "day in life, routine, favorite, recommend, honest, review, worth it, must have"
        else:
            custom_words = st.text_area(
                "Power Words (pisahkan dengan koma)",
                placeholder="rahasia, cara, tips, trik, viral, amazing"
            )
    
    st.markdown("---")
    st.markdown("### ℹ️ Info")
    st.info("""
    **Processing Time:**
    - 5 min video = 2-3 min
    - 10 min video = 3-5 min
    - 20 min video = 6-10 min
    
    **Tips:**
    - Clear audio works best
    - Good lighting helps
    - 10-20 min videos optimal
    """)

# Main content
uploaded_file = st.file_uploader(
    "📤 Upload Video", 
    type=['mp4', 'mov', 'avi', 'mkv'],
    help="Upload video yang mau di-clip (max 2GB)"
)

if uploaded_file:
    # Preview video
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📹 Preview Video")
        st.video(uploaded_file)
    
    with col2:
        st.markdown("### 📊 Video Info")
        file_size = uploaded_file.size / (1024 * 1024)  # MB
        st.metric("File Size", f"{file_size:.1f} MB")
        st.metric("Target Duration", f"{duration}s")
        st.metric("Max Clips", max_clips)
        st.metric("Language", language.upper())
    
    # Process button
    st.markdown("---")
    
    if st.button("🚀 Process Video", type="primary", use_container_width=True):
        # Create temp directories
        os.makedirs("temp_input", exist_ok=True)
        os.makedirs("output", exist_ok=True)
        
        # Save uploaded file
        temp_path = os.path.join("temp_input", uploaded_file.name)
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.read())
        
        # Progress indicators
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        try:
            # Initialize clipper
            status_text.text("🔧 Initializing clipper...")
            progress_bar.progress(10)
            
            clipper = SmartVideoClipperUltimate()
            
            # Custom power words
            if use_custom and custom_words:
                clipper.power_words = [w.strip() for w in custom_words.split(",")]
            
            progress_bar.progress(20)
            
            # Process video
            status_text.text("🎬 Processing video... (this may take 3-5 minutes)")
            
            clips, metadata = clipper.create_clips(
                video_path=temp_path,
                output_dir="output",
                target_duration=duration,
                max_clips=max_clips,
                vertical_crop=True,
                language=language
            )
            
            progress_bar.progress(100)
            status_text.empty()
            
            # Success message
            st.success(f"✅ Success! Created {len(clips)} high-quality clips!")
            
            # Load metadata
            with open(metadata, 'r', encoding='utf-8') as f:
                meta_data = json.load(f)
            
            # Show processing time
            processing_time = meta_data.get('processing_time', 0)
            st.info(f"⏱️ Processing completed in {processing_time:.1f} seconds ({processing_time/60:.1f} minutes)")
            
            # Display results
            st.markdown("---")
            st.markdown("## 🎥 Your Clips")
            
            for i, clip_info in enumerate(meta_data['clips']):
                with st.expander(f"📹 Clip {i+1} - Score: {clip_info['score']}", expanded=True):
                    col1, col2 = st.columns([3, 1])
                    
                    with col1:
                        # Video player
                        clip_path = clips[i]
                        st.video(clip_path)
                    
                    with col2:
                        # Clip info
                        st.markdown("**📊 Clip Details:**")
                        st.metric("Total Score", clip_info['score'])
                        st.metric("Duration", f"{clip_info['duration']:.1f}s")
                        
                        st.markdown("**🎣 Hook:**")
                        st.text(clip_info['hook'][:100] + "...")
                        
                        st.markdown("**⏰ Timing:**")
                        st.text(f"Start: {clip_info['start']:.1f}s")
                        st.text(f"End: {clip_info['end']:.1f}s")
                        
                        # Download button
                        with open(clip_path, 'rb') as f:
                            st.download_button(
                                label="⬇️ Download",
                                data=f,
                                file_name=clip_info['filename'],
                                mime="video/mp4",
                                use_container_width=True
                            )
            
            # Download all as ZIP
            st.markdown("---")
            st.markdown("### 📦 Download All")
            
            zip_path = "all_clips.zip"
            shutil.make_archive("all_clips", 'zip', "output")
            
            with open(zip_path, 'rb') as f:
                st.download_button(
                    label="⬇️ Download All Clips (ZIP)",
                    data=f,
                    file_name="all_clips.zip",
                    mime="application/zip",
                    use_container_width=True
                )
            
            # Download metadata
            with open(metadata, 'rb') as f:
                st.download_button(
                    label="📋 Download Metadata (JSON)",
                    data=f,
                    file_name="clips_metadata.json",
                    mime="application/json",
                    use_container_width=True
                )
            
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            st.exception(e)
        
        finally:
            # Cleanup
            progress_bar.empty()
            if os.path.exists("temp_input"):
                shutil.rmtree("temp_input")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem;'>
    <p>Made with ❤️ by Smart Video Clipper</p>
    <p>🎬 High Quality • ⚡ Fast Processing • 🎯 Context-Focused</p>
</div>
""", unsafe_allow_html=True)
