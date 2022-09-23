for file in *.mkv; do # change mkv to video format of choice
	echo ${file##*/}
	if test ! -f "${file%.*}.srt" ; then
	    ffmpeg -y -i "./${file##*/}" "${file%.*}.srt"  #rip subtitle track
	fi
	python3 translator.py "${file%.*}" #translate
done
