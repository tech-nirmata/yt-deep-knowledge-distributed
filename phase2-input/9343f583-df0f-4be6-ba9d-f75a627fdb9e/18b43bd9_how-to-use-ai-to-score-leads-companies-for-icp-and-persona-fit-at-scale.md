---
notebook_id: 9343f583-df0f-4be6-ba9d-f75a627fdb9e
notebook_title: "Jordan Crawford (Blueprint)"
source_id: 18b43bd9-60c2-4b92-8578-1a0ee307f268
source_title: "How to use AI to Score Leads + Companies for ICP and Persona Fit (At Scale)"
source_type: SourceType.YOUTUBE
extracted_at: 2026-05-21 11:34:31 UTC
extractor: nlm_bulk_extract.py
---

# How to use AI to Score Leads + Companies for ICP and Persona Fit (At Scale)

## NotebookLM-extracted transcript (Google's ASR + indexing)

what up what up all right uh all we're doing here is going to conquer a exhibition show so I talked about how to dominate a market by going after events so what what I'm going to show you now is how I actually do that inside a clay how I Define ICP scores for both the exhibitors and the the attendees uh and so we've got a little bit of uh gbt training going on here so this is going to be a working session so you know you might get bored um 
uh but it's going to be a pretty intense working session so you know just tune out if You' like all right so the first thing I'm going to do is I have this promp to be able to uh give ICP score for a company and I'm just going to improve it here I'm I'm going to use chbt to improve the prompt to chbt uh love my super whisper here which is what I'm using I am trying to improve this prompt I want to go after only sleep cans and durable medical equipment companies and 
the list here are people that are actually exhibiting at Med trade and they aren't all perfect fits so I want to take the qualification prompt below and provide more context for gbt to be able to score a company now I generally want clinics I'm looking for Sleep clinics or durable durable medical equipment um and make sure that we have a wider breath of qualification and disqualification examples can you improve the prompt below 
my job is on the line I always say that because uh it turns out that emotional resonance really helps it's funny it updates the memory every time so gbt thinks I'm insane because I'm doing all sorts of things for a variety of different companies so this is problem yeah yeah 
yeah perfect so you see how basically GPT can structure the better calls to gbt which are really important here ah great this is good so 
I'm goingon to rep I'm going to replace this but the other thing that's really important is uh is you is you need to kind of need to sort of yell at it uh I always say like only ever give it a best guest never respond if and that seems to work really well uh I always do save and do not run which there's an interesting clay sort of bug here that every time you do that ites 
doesn't give you counts for did this run again oh double run I don't think yeah I don't think they're a fit so let's just rerun a couple of these guys this is something I might even want to have the Cent do so it can search a little bit wow everything's a five uh 
uh this is not right um okay uh this is a perfect example where I can go use the Cent save and do not run cian's going to do a little searching for me which is probably good I do want it to do a little Googling same price 
I did pull in a bunch of information I'm use my own API key all right uh search the web before you give me your answer uh we want a number zero I do 
oh let's just try it I don't mind spending money for find people on the internet uh save and do not run all right let's go I think this Respiratory Care is a oh uh oh I actually can turn all of these off uh dear clay please 
copy my saved preference when I all right save and do not run yeah that's pretty good about 4 cents uh these look kind of the same actually let's sort of see if we're getting better results I did try to bring the internet 
into into the search itself and the nice thing about the cigan is it gives you it actually tells you why uh I think we don't want revenue cycle management 
this is helpful if you do so Reven cycle management software companies anyone that isn't a specific DME provider or uh DME provider or Sleep Clinic should 
get a should get an automatic zero all right let's edit this column again and just update the zero condition should I do ASMR lead building hi everyone today 
we're going to be scoring some companies here soft sound of AI running in the background something to fall asleep too oh yeah oh yeah that's a great 10 out of 10 great 
well this is much much cheaper it looks like these are about the same let's actually see if I I mean makes sense right there going out the same information but this is 5 cents versus six t0 of a penny so I probably am going to just run this for I think this is looking pretty good let's actually just 
do a couple more to make sure that like like dignity lifts is probably pretty good let's actually just make sure that gbt 4 thinks the same thing it is really nice that uh gbd4 with the cayan explains its reasoning which is super helpful and I'm just looking for Divergence here so if it if it surfs the web and finds other things that I haven't brought into it with three 
.5 now 3.5 is good it works for most things yeah so specific yeah yeah so this is this is right now let's see yeah so this is really helpful because now you have an understanding about how it 
um how it's thinking and so you're just it referral volume isn't something that you could ever find so I probably shouldn't actually the company should re for months um but you'll never know you'll never know this so you can only make inferences based on things like headcount uh headcount uh services offered and variety 
of variety of services offered and number of locations all right so I'm going to actually update this yeah so I'm going to update both of these save and do not run 
all right let's update the eent to save and do not run all right let's just try a couple more of these again these are looking really good so I think I'm just going to run this for the whole thing now I need to also uh do the same thing on the people side so that's 
the thing that we'll do next and I'll show you that next I feel pretty good let's just look at a couple more like this should be a zero because it's not in the US oh all right five 
let's actually see what the clent says here sometimes I would change this to it to say explain your reasoning uh so the that's really helpful to to get that context so you know exactly what it's thinking so the clent's really helpful here I'm going to go do this to people actually I probably will end this video uh yeah the cloudbased platform 
yes software provider so perfect so I feel good about this now let's run the whole thing now we're going to do the same thing and I'll I might as well um keep you here and I'll do the same thing for people now and I probably will use the clent here because then I know um I both know the context 
let's actually copy over the The Prompt here all right so uh and actually let's go get some data here because what we actually want to know is titles too so in this case we're going to 
score titles so it's a little bit different we're looking at in my sleep clinics and we're looking to score based on their title and Company description uh let's do 10 
they must work at a Sleep Clinic or DME Company uh and have titles like 
but can have titles like 
okay they don't work at a Sleep Clinic they uh and let's see five they work at a Sleep Clinic or DME but don't have 
any of the types of titles like above they don't work and they they don't work at Sleep Clinic uh and they and they don't have any senior level titles here is the rubric uh rubric 
okay so sell devices okay 
let's keep this headcount piece uh with high headcount uh 50 plus variety of services offered and many locations 
they may have fewer employees fewer locations and fewer Services vanit 10 uh always give a zero if the company isn't in the USA USA USA why not 
PES are companies like linare which has which has more than 
great here is all I know here is all I know about the company and person all right so this is just I just put this in a comma separated list uh full name uh title and Company we did some further enrichment so we got the 
uh actually I don't want to use the domain finder because I did a little cleaning of my own uh company LinkedIn title uh LinkedIn URL maybe it'll go visit the person's profile that'd be nice uh I probably do well not what I want okay um I'm going 
going to save and do not run I'm going to map the company description here from the oh yeah I'm going to map the person summary I wonder if we've gotten the experience table let's see oh that's the summary of the person which is okay I want the summary of the 
company I may have to go enrich the company description uh I don't need to do that I'll let the AI go search the web oh that's their title do I have their title I think I have their title already summary I do have their title and Linkedin name okay this is actually pretty good let's give their summary as part of this 
all right I think this is pretty good uh number zero model let's see what it looks like how do we start I always start with gbt 3.5 uh usually because it's almost always good enough 
but I do oh I do have to yeah I have to so what I'm doing here is I'm actually turning off the requirement that any of these are here so it's okay if it's okay if we don't have some of this information and because you can't do conditional running in clay you just have to say like you know do 
what you have okay let's see what it so this is three cents ah okay that's actually pretty good 
nice nice good job clent okay medical equipment yeah perfect middle score five good job clay uh all right now let's like just run a couple more of these and let's see if the much cheaper so how much 8 cents wow 
wow uh well I'm not made of money uh let's like okay let's do not run all right so okay we got a five let's see what 3.5 gives us come on Big Money big money big money big money give me a five give me a five give me a five zero let's see what it says Ah 
it actually was smarter and you know why it was smarter because it contain more tokens so uh actually ironically the much much much cheaper model might be better here because the output is simpler and it can take in more context so this is really helpful all right let's see if this gives us seven here huh all right it's pretty good 
that's 310 of a penny ah great yeah okay so same same thing zero and seven let's see oh wow this fuck the same person and it's like could be a zero could be a seven those are vastly different numbers oh great oh okay so actually what I should do is like I should say if you don't have 
have enough information search your damn heart out on the web stop at no expense I need I need accuracy Above All Else uh all right let's let's see if it tries a little harder let's actually kind of pull up this person oh so they're in Canada 
so this should probably be a zero did I run I think I I don't know if I reun it let's see tell me if I clicked all right when this is done I'm going to I'm going to leave you here 24 25 minutes is good enough um so what I'm going to do next here is oh let's see if they said Canada 
yeah yeah yeah yeah yeah yeah yeah um so I might actually let's just do this here um uh try uh try Googling 
all right so this is kind of how unfortunately these like really large language models someone should develop an ICP model honestly uh that just is a trained um gosh that would be a really really good business is just to develop an API for ICP scoring um I don't know why anyone has done that ocean actually does something like that would look Al likes but I think it's actually better to do an ICP score it's a little bit more specific 
uh yeah I don't think we're going to get better than this uh I'm probably going to run this whole list because three cents so let's just to give you a sense uh if I'm pulling this whole list 1380 times this is $41 to do this whole thing so probably pretty good here um and if I have to redo it say l uh some inputs oh I think there's oh that's interesting 
I don't think I required any ah yes yes yes I this is this is not required one uh all right everyone I hope this is enjoyable uh thanks for watching me work and uh let me know if you need any ICP or lead score and happy to help out bye 
