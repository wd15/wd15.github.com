# Daniel Wheeler's Research Blog

When posts are messed up and not displaying:

 * When posts are messed up try `jekyll --safe --no-lsi --pygments --no-server --no-auto`.

Embedding Youtube video:

 * Convert pngs to avi.
 
    `$ mencoder -nosound -ovc x264 -x264encopts preset=slow:tune=film:crf=20 -o out.avi mf://*.png type=png:fps=20:w=1920:h=108` or `$ mencoder "mf://*.png" -mf fps=10 -o output.avi -ovc lavc -lavcopts vcodec=mpeg4`

 * Speed up the movie by 0.25 (i.e slow it down).
 
    `$ ffmpeg -i out.avi -vf "setpts=(1/0.25)*PTS" out1.avi`
    
 * Embed in blog post. `?rel=0` stops suggested videos from being played.
 
    `<iframe width="480" height="360" src="http://www.youtube.com/embed/qE9fYpUG3TU?rel=0" frameborder="0"> </iframe>`
