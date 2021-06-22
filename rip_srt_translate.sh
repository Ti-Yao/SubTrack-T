for file in *.mkv; do
echo ${file##*/}
#ffmpeg -i "./${file##*/}" "${file%.*}.srt"  #rip
python3 translator.py "${file%.*}" #translate
done
