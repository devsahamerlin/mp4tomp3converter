from moviepy.editor import *
import os

dir = "/Users/e-glodevsolutionsltd/Movies/film"

list = os.listdir(dir) # dir is your directory path
number_files = len(list)
print (number_files)


for file in os.listdir(dir):
     filename = os.fsdecode(file)
     print(f'/Users/e-glodevsolutionsltd/Movies/film/{filename}')
     mp4_file = f"/Users/e-glodevsolutionsltd/Movies/film/{filename}"

     filename1 = filename.replace(".mp4", ".mp3")

     #print(f'/Users/e-glodevsolutionsltd/Movies/film/{filename1}')
     mp3_file = filename1

     videoClip = VideoFileClip(mp4_file)

     audioClip = videoClip.audio

     audioClip.write_audiofile(mp3_file)

     audioClip.close()

     videoClip.close()


#mp4_file = "/Users/e-glodevsolutionsltd/Movies/film/Gucci Mane - Proud Of You (Official Music Video).mp4"

#mp3_file = "Gucci Mane - Proud Of You (Official Music Video).mp3"

#videoClip = VideoFileClip(mp4_file)

#audioClip = videoClip.audio

#audioClip.write_audiofile(mp3_file)

#audioClip.close()

#videoClip.close()
