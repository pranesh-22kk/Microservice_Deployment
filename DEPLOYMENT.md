# 🚀 Deployment Guide - HephaestusForge

## Quick Deploy to Streamlit Cloud (Recommended)

### Prerequisites
- GitHub account
- Your code in a public GitHub repository

### Step


1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Select your repository
   - Main file path: `app.py`
   - Click "Deploy"!

3. **Your app will be live at:**
   `https://YOUR-APP-NAME.streamlit.app`

## Files Required for Deployment ✅

All necessary files are already included:

- ✅ `.gitignore` - Excludes unnecessary files
- ✅ `.streamlit/config.toml` - Streamlit configuration
- ✅ `requirements.txt` - Python dependencies
- ✅ `packages.txt` - System dependencies
- ✅ `runtime.txt` - Python version specification
- ✅ `app.py` - Main application (error-free)

## Environment Variables (Optional)

If you need API keys or secrets:

1. In Streamlit Cloud dashboard, go to "Settings" → "Secrets"
2. Add your secrets in TOML format:
   ```toml
   API_KEY = "your-api-key"
   DATABASE_URL = "your-db-url"
   ```

## Alternative Deployment Options

### Option 2: Hugging Face Spaces
1. Create account at [huggingface.co](https://huggingface.co)
2. Create new Space → Select "Streamlit"
3. Upload files or connect GitHub
4. Auto-deploys!

### Option 3: Railway
```bash
npm i -g @railway/cli
railway login
railway init
railway up
```

### Option 4: Render.com
- Build command: `pip install -r requirements.txt`
- Start command: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`

## Testing Locally Before Deploy

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
streamlit run app.py
```

Open http://localhost:8501 to test.

## Troubleshooting

### Issue: App crashes on startup
**Solution:** Check logs in Streamlit Cloud dashboard

### Issue: Dependencies fail to install
**Solution:** Update requirements.txt versions

### Issue: Port binding error
**Solution:** Streamlit Cloud handles this automatically

## Post-Deployment

1. **Test your live app** - Make sure all features work
2. **Share the link** - Add to resume, LinkedIn, GitHub
3. **Monitor usage** - Check Streamlit Cloud analytics
4. **Update anytime** - Just push to GitHub, auto-redeploys!

## Support

- Streamlit Docs: https://docs.streamlit.io
- Community Forum: https://discuss.streamlit.io
- GitHub Issues: Create in your repository

---

**Your app is now ready for deployment! 🎉**

No errors, fully configured, recruiter-ready.
