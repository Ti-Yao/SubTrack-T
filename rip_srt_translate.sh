for file in *.mkv; do # change mkv to video format of choice
echo ${file##*/}
ffmpeg -i "./${file##*/}" "${file%.*}.srt"  #rip subtitle track
python3 translator.py "${file%.*}" #translate
done
