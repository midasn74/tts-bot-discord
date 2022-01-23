
# Simple Text-To-Speech Bot For Discord

This is a very simple TTS bot for discord made with python.  
For this bot you need FFMPEG, see installation to see how to install it.


## Usage/Examples
Commands:
```discord
help: returns a help message
```
```discord
tts: Plays your message in the voice channel you are currently in
```
```discord
setlanguagetts: Changes the tts language for your server
```


## Installation 
#### FFMPEG Windows:  
Download the latest zip at https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z  
Unzip the file and rename the folder to ffmpeg.  
Move the ffmpeg folder to root directory (C:/).  
Then add C:\ffmpeg\bin to path, manually or with:
```bash
setx /m PATH "C:\ffmpeg\bin;%PATH%"
```

#### FFMPEG Linux:  
```bash
  sudo apt install ffmpeg
```

#### Installing the bot:  
```bash
  git clone https://github.com/midasn74/tts-bot-discord.git
  cd tts-bot-discord
  pip install -r requirements.txt
```
Create a bot if you haven't already then copy the TOKEN and paste it into the settings.ini file.   
You can find your token / create a bot at https://discord.com/developers/applications.
```ini
  TOKEN = YOURTOKEN
```
## Running the bot
simply run the main.py file
```bash
  py main.py
```
    
## License

[MIT](https://choosealicense.com/licenses/mit/)

