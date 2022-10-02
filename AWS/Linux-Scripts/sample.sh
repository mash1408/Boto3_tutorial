#!/bin/bash
if [[ -f $1 ]]

then
  echo "India’s fifth and final Test against England in Manchester was cancelled at the last moment due to COVID-19 outbreak in the Indian camp. The cancellation wasn’t without it’s share of controversies thou>
word_count=$(wc -w $1 | cut -c 1,2,3)
char_count=$(wc -m $1 | cut -c 1,2,3,4)

echo -e "\nWord Count: $word_count\nChar Count: $char_count\nLine Count:"

else
echo "The file $1 cannot be found."

fi
exit
