from videogenerador import *
from textgenerator import *
import ast
from moviepy.editor import *
from moviepy.config import change_settings
from upload import subida


change_settings({"IMAGEMAGICK_BINARY": r"C:/Program Files/ImageMagick-7.1.1-Q16-HDRI/magick.exe"})

cleanup_folders()
ok=""
while not(ok=="yes" or ok=="Yes") or len(title)<3:
    title=input("\nEnter the title of the video: ")
    ok=input(f"\nThe title will be: {title}. Are you sure?(answer yes or no) ")
    if(len(title)<3):
        print("The title is too short, enter a different one.")

done=False
while not done:
    try:
        duration=float(input("\nEnter the desired length of the video (in minutes, for Shorts enter a number equal to or less than 1): "))
        done=True
    except Exception as e:
        print("Enter a posible value, ex: 4, 2.5, 0.7")

#json.loads(x)
voz=""

while not(voz=="1" or voz=="2"):
    voz=(input("\nEnter 1 for male voice or 2 for female voice: "))




done=False
while done==False:
    try:
        print("\n\nGenerating script...")
        guion=Creadortexto(title,duration)
        #print("\nGuión: "+guion)
        done=True

    except openai.error.ServiceUnavailableError as e:
        print("Service is overloaded. Retrying...")
        time.sleep(15) 

    except openai.error.OpenAIError as e:
        print(f"An error occurred: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

done=False
while not done:
    try:
        lista=jasonmomoa(guion)
        print("\nSuccessfully created script.")
        descripcion=lista[0]
        tags=lista[1]
        division=lista[2]
        tematicas=lista[3]
        done=True

    except openai.error.ServiceUnavailableError as e:
        print("Service is overloaded. Retrying...")
        time.sleep(15) 
                
    except openai.error.OpenAIError as e:
        print(f"An error occurred: {e}")
            
    except IndexError as e:
        print("No videos found that fit the script, this will be rewritten")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        cleanup_folders()

done=False
while not done:
    try:
        print("\n\nEditing video...")
        final=video(division,tematicas,duration,voz)
        done=True

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        cleanup_folders()

        time.sleep(30)


final.write_videofile("./output/"+title+".mp4")
print("\nUploading video to Youtube")
subida("./output/"+title+".mp4",title,descripcion,tags)
print("\nVideo has been uploaded successfully")