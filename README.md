# Snapchat Detox

'Snapchat Detox' is a Python 3.x-based tool that parses through your Snapchat memories and accurately modifies the timestamp for the images downloaded. I was inspired to create this tool because I wanted to delete my Snapchat account but I wanted to make sure I could store all my memories correctly in my camera roll. Run the tool after [downloading data from Snapchat](https://help.snapchat.com/hc/en-us/articles/7012305371156-How-do-I-download-my-data-from-Snapchat) adjusting the `ORIGINAL_SNAPCHAT_MEMORY_FOLDER`, `COPY_SNAPCHAT_MEMORY_FOLDER` variables in `main.py` with the following shell commands:

```bash
git clone https://github.com/naveen-vivek/snapchat-detox.git;
cd snapchat-detox;
python -m pip install -r requirements.txt;
python main.py;
```

After this, you can officially uninstall Snapchat and still have all your wonderful memories intact!