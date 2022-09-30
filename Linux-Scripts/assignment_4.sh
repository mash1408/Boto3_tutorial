#!/bin/bash
if [[ -f $1 ]]

then
lines==$(wc -l $1 | cut -c 1,2)
echo -ne "India’s fifth and final Test against England in Manchester was cancelled at the last moment due to COVID-19 outbreak in the Indian camp.\nThe cancellation wasn’t without it’s share of controversies though a mail to Board of Control for Cricket in India (BCCI) at midnight asking them to call-off the Test match." >  $1
word_count=$(wc -w $1 | cut -c 1,2,3)
char_count=$(wc -m $1 | cut -c 1,2,3,4)

echo -e "\nWord Count: $word_count\nChar Count: $char_count\nLine Count:$lines"

else

  echo "The file $1 cannot be found."

fi
exit



