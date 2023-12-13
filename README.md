To install the program, write in cmd, in the folder where you want to install it: git clone https://github.com/salomonsa/fiverr-app_for_lolhaususa

IMPORTANT THINGS, READ BEFORE USING THE PROGRAM:

1. Change the name of the dotenv file to .env, open it and write your OPENAI API token and your PEXELS API token, you will find them on their respective websites.

2. Install all requirements in the requirements.txt file. Use the pip install -r requirements.txt command to install all Python modules and packages that are listed in your requirements.txt file. Additionally, and this is ESSENTIAL for the program to work, install Imagemagick separately on its official website.

2. Create your YouTube channel if it does not already exist and follow the steps in this video until you reach your Client ID and your Client Secret: https://youtu.be/aFwZgth790Q (it is not necessary to create an account in google cloud, just click in console when the tutorial does it), all this using the account of the YouTube channel to which you want to upload the videos. Once you have your Client ID and your Client Secret, replace them in the "client_secrets.json" file.

3. You should not touch the stockvideos and speech folders, in stockmusic you have to enter the music files (mp3) that you want the video to have, if you enter one it will only be repeated in a loop throughout the video, if you enter several the program will choose one at a time random and will loop it.

When you try to run the program you will be asked for the title of the video, the duration and the type of voice. Once the program has been chosen, it proceeds to create the script with OpenIA (which is usually fast), then proceeds to edit the video. In this part, some errors related to limits of demands on the APIs may appear (in these cases, waiting will fix it. ), and the longer the video, the greater the probability that these will appear, which is why I recommend you start by testing the program with short videos.

When changing devices it is not uncommon for unexpected errors to appear, if you have any questions write to me.
