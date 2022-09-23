for file in *.mkv; do # change mkv to video format of choice
echo ${file##*/}
ffmpeg -f -i "./${file##*/}" "${file%.*}.srt"  #rip subtitle track
python3 translator.py "${file%.*}" #translate
done
