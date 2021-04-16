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

These are so you could say "Hey Mycroft, Please launch a terminal." and Mycroft will
know what you mean even though there is no program called "terminal". (NOTE: You can
still explicitly specifiy the terminal to use, but this is easier on the brain. Right now
one can set the the default terminal in the "settingsmeta.json" file or on the mycroft
website. The "settingsmeta.json" file is located in the root on the skill's install
directory, "/opt/mycroft/skills/mycroft-app-launcher.calacuda" by default on linux
systems).

other "special programs" include:
 -- web browser = firefox
 -- terminal = urxvt
 -- audio controller = pavucontrol
 -- chat client = caprine (facebook messenger client)

### aliases:

you can set up aliases from the mycroft website skills settings menu or by directily
editing the skills "settingsmeta.json". I recomend the website as it is MUCH easier
the format is as follows: uterance_1=program_1, uterance_2=program_2. with these
settings mycroft will run [program_1] when you say "run [uterance_1]" where [uterance_1]
is the alias or "nickname" of [program_1]. [program_X] can be a path to the excacutable or
an excecutable in your path. this functionality was added so you can launch programs with 
names that are either hard to say or that mycroft wont regognize. (you can also write custom
scripts, make them executable, then point an alias to said script and run it with your voice.)


### TODO's:

1. [x] Add online settigns update function. (This functionality is already in mycroft so
       	   	  	   	  	     it will be easy.)
2. [x] Make user definable "Special Programs" (maybe by having a json text input on mycrofts
   	     	       			       website?) (effectively done with the aliases
					       functionality)
3. [x] Make a julia/python repl mode. (the user would say something like "launch julia", the
   	  	       	    	   skill would open an interactive julia repl, with voice
				   control and typing, in a fully equiped terminal emulator)
				   (this brock off to a whole different mycroft skill called
				   [mycroft-julia-skill-2](https://github.com/calacuda/mycroft-julia-skill-2))
4. [ ] Add more phrases for the intent parser. (recuring iterative process)