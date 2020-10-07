# mycroft-app-launcher:
a mycroft skill that allows you to open and run programs from mycroft

### usage:

say somehting to the effect of:
 -- open (prgram)
 -- launch (program)
 -- start (program)
 -- spin up (program)
 -- boot up (program)

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
 -- audio controller = pavucontrol
 -- chat client = caprine (facebook messenger client)


### TODO's:

1. Add online settigns update function. (This functionality is already in mycroft so
   it will be easy.)
2. Make user definable "Special Programs" (maybe by having a json text input on mycrofts
   	     	       			   website?)
3. Add a user toggleable proxychains mode. (If on every app is run through proxcychains
       	      		 	     	    if all apps are run normally)
4. Add more phrases for the intent parser. (recuring iterative process)