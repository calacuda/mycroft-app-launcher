# mycroft-app-launcher:
a mycroft skill that allows you to open and run programs from mycroft

### usage:

say somehting to the effect of:
 -- open (prgram)
 -- launch (program)
 -- start (program)
 -- play (game)


### special programs:

I'm using "Special Programs" to mean programs that can be called based on what type of
prgram they are not just by their name.


These are so you could say "Hey Mycroft, Please launch a terminal." and Maycroft will
know what you mean even though there is no program called "terminal". (NOTE: You can
still explicitly specifiy the terminal to use, but this is easier. Right now one can
set the the default terminal in the "settingsmeta.json" file. This is located in the
root on the skill's install directory, "/opt/mycroft/skills/mycroft-app-launcher.calacuda"
by default on linux systems). Suport for changing this setting via the mycroft website
is coming soon.

other "special programs" include:
 -- web browser = firefox
 -- terminal = urxvt
 -- audio controller = pavucontrol (not working yet, when mycroft hears "audio 
    	  	       		    controller" it triggers a different skill)
 -- chat client = caprine (facebook messenger client)
 


### TODO's:

1. Add online settigns update function. (This functionality is already in mycroft so
   it will be easy.)
2. Fix audio controller. (I'll probably rename it or something)
3. Add more phrases for the intent parser. (recuring iterative process)