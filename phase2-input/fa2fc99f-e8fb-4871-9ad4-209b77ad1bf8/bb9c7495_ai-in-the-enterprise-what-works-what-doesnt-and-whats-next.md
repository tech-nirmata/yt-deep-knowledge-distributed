---
notebook_id: fa2fc99f-e8fb-4871-9ad4-209b77ad1bf8
notebook_title: "Stanford Graduate School of Business"
source_id: bb9c7495-a8b6-4ea4-bacd-224b199dec69
source_title: "AI in the Enterprise: What Works, What Doesn’t, and What’s Next"
source_type: SourceType.YOUTUBE
extracted_at: 2026-05-21 12:32:21 UTC
extractor: nlm_bulk_extract.py
---

# AI in the Enterprise: What Works, What Doesn’t, and What’s Next

## NotebookLM-extracted transcript (Google's ASR + indexing)

[MUSIC]
Good morning, everyone, and
good afternoon, good evening, or
good night to those of you joining
us from other parts of the world.
Welcome to our Value
Chain Innovation Speaker Series,
my name is Barchi Gillai and
I'm the Associate Director of the
Value Chain Innovation Initiative
at Stanford Graduate School of
Business.
We're excited to have with us today
Professor Yoav Shoham with the
co-founder and co-CEO at AI21 Labs.
Professor Shoham is a leading AI
expert who received multiple awards
for his significant
contributions to the field.
One example to illustrate his
foresight and
impact on the field is that while
everyone talks about agents today,
Professor Shoham defined
the framework for agent oriented
programming as early as 1993.
Professor Shoham is the co-founder
of several other successful AI
companies in addition to AI21 Labs.
He is also a professor emeritus of
computer science at
Stanford University.
In today's event, we will explore
the evolving landscape of AI in the
enterprise examining its current
state and future trajectory.
Moderating the discussion is
Haim Mendelson who is a professor
at the Stanford Graduate School of
Business and
the faculty director of the Value
Chain Innovation Initiative.
Before we begin the discussion I'd
like to quickly go over
a few housekeeping items.
First, the event is recorded,
the recording will be available
in a few days on
the Stanford GSB YouTube channel as
well as on the website of the Value
Chain Innovation Initiative.
If you have any questions
to Professor Shoham, you're welcome
to submit them at any point
during the moderated discussion.
We ask that you please
use the Q&A box
to share your questions with us.
Towards the end of the webinar,
we will have a Q&A session, and
during that time Professor Shoham
will address as many of your
questions as time permits.
If you would like your name to be
mentioned when we read your
question, please include it at
the end of your message.
As for closed captioning,
if you would like to activate this
feature, please click on
the Show Captions or CC icon.
Finally, we kindly ask that you
take a moment at the end of the
webinar to complete a brief survey.
We value your feedback, and we'll
use it to improve future events.
And now I'm delighted
to hand things over to
Professor Haim Mendelson.
>> Thank you very much, Barchi,
and thank Yoav for joining us, it's
a real treat to have you with us.
Let's get started,
I remember many years ago,
you were a superstar faculty member
at the computer science department,
and you got the entrepreneurship
bug and started the company.
What gave you that bug?
>> I don't know where I went wrong,
I have to confess.
Honestly, I came in almost, I would
say, despising practical matter and
somehow something in the air.
At the end of the day, though,
I think at some point you you can
prove just that many theorems.
At some point you want to see
something move in the world, and
that's very addictive,
I would have to say that, yeah.
>> Can you tell us a little bit
about some of the companies that
you started or
participated in before AI21 Labs?
>> Yeah, I mean,
I guess the common denominator is
where I saw an arbitrage between
ideas that in AI, either I was
involved in directly or indirectly.
And what I saw in the world, and
try to capitalize on that really
kind of moving the needle that way.
And some people are really good at
execution, and
that's what makes them successful.
And to the extent that I was
successful, is not because of that,
it's because the ideas had enough
force that they could withstand
whatever poor execution I brought
to the table.
>> It's great.
>> Yeah, we had the first company,
it was called Trading Dynamics,
back in the days of B2B trading and
I've been involved in game theory
for many years.
I have a course on game theory
that's been on Coursera and
other places.
Over a million people have seen it,
which is weird because it's not
really useful.
So I got exposed to your colleagues
in the business school and
Econ to the the energy auction in
California, and also the spectrum
auctions, and that
was already real world, real money.
And I was amazed at how backward
the software was, using closed
standards, very ossified.
And it was obvious that we could
build a much kind of more nimble,
flexible, quick to deploy, kind of
system at the fraction of the cost.
So that was an example of the first
company that I was involved with
Trading Dynamics, it was called.
>> And we move forward,
I remember in, I think it was 2017,
we were talking and
you are starting, you were involved
in a secretive effort,
which I think became AI21 Labs.
Can you tell us about that period
and what was the prompt that led
you to think about those new ideas?
>> Well, it's interesting, yeah, so
that is the company that I'm
currently involved with and
I helped start it with two other
colleagues, Ori Goshen, who kind of
has no degree in anything, but
is smarter than
anybody else in the room.
And Amnon Shashua has a degree, but
probably better known for
having started and
running Mobileye and
few other companies.
But really what prompted
the company was seeing where
the field was with the whole
emphasis on deep learning.
So LLMs weren't a thing, well,
they were happening,
coincidentally, as we started
the company, but deep learning was
clearly dominating the field.
And I felt that deep learning was
necessary, but not sufficient that
you wouldn't get the robust
reasoning that we expect and
that AI used to deal with before
statistics took over.
And so we started the company with
a goal of kind of marrying the two,
which is maybe an odd reason to
start the company, but
that's why it happens, and it's
seven years later, here we are.
>> And was that before or
after the transformers paper?
>> Same year.
>> Same year?
>> As it happens, 2017, yeah, we
started the company after it, but
it hadn't yet made the headlines.
But as we were working,
clearly language was where
the action was going to be.
And as we were working on it,
this end-to-end training enabled by
transformers was kind of creating
a buzz, so
it was kind of fortuitous that we
started around the same time.
>> And can you tell us a little
bit about the evolution
of the company over those years?
>> Yeah, so
first maybe I'll start with basics
where, like I said,
we're about seven years old,
we're about 250 people.
About 100 of them are sort of
technical kind of AlgoEdge
type stuff, type people.
And for three years, we did nothing
but work on technology.
But we really wanted to be a
business, not a research lab only.
We say kind of somewhat tongue in
cheek, we don't want to be a deep
mind, and we, of course, say this
with utmost admiration f or
the guys, but there was not a big
business in solving Atari Games.
So the question is,
what business would we be in?
And it was clear to us,
we wanted to be a B-to-B company.
We felt this, but it was also clear
that there wasn't a business yet
to be had there, we're talking
about 2000 to about 2020, or so.
And so we created our own market
with a writing assistant called
Wordtune.
Today you have no end of writing
assistants, some of them built into
the big platform but at the time,
it was really transformative and
very successful.
We passed 10 million users,
which was a kind of a freemium kind
of model, so we crossed 20 million
IRR very quickly and so
it's doing well.
But then what happened is then
enterprise suddenly happened.
So we still have that business, and
it's a good little business, but
our focus is on the enterprise.
And so I can tell you more about
our technology, but basically,
if I speak to Suzuma and speak
about how we see the industry,
we think we're about to move from
the second to the third phase of
the modern AI revolution.
I'll tell you what I mean by that.
So, until roughly GPT3 timeframe,
enterprise couldn't care less.
There was sporadic experimentation.
They had just finished transition
to the cloud and so maybe, yeah,
go ahead and play with it.
And then we transitioned so
that there's no CEO in the world
that doesn't say,
I'm an AI-first company, I want to
be an AI-first company, and a ton
of experimentation, but a dramatic
drop from experimentation to mass
deployment.
There's one study by AWS that picks
it at a 94% drop.
So 6% of the project had to go too,
and we see it for firsthand.
We think we're about to cross into
the third phase where you'll
see mass deployment.
And the two biggest changes will be
much more efficient models in terms
of the cost because the economics
of large language models is very
different from the economics of
traditional software,
as you know, and so you need to do
something about that.
But second,
as I think is well known,
these models are wonderful,
sometimes just brilliant and
sometimes dumb as nails.
And in the enterprise for most use
cases, if you're brilliant 95%
of the time and ridiculous 5% of
the time, you're dead in the water.
And so
we think that the next transition
would be to really change that and
it's not just a matter of so-called
more guardrails and so on,
it's really moving from models to
complete AI systems, and
we can speak about that.
But that's kind of the landscape
and what we do as a company.
We have our own language models and
we're extremely good.
Our latest family called Jamba kind
of broke the transform a mold and
gained dramatic efficiency,
especially with so-called long
context, and it's doing well,
and we're very active in the AI
systems.
I can't elaborate a lot, but
it's an area that's really
the reason we started the company.
So anyway, that's maybe a little
too much about us as a company.
>> So let's kind of a go into some
of the details.
So first of all, can you tell us
a little bit more about Jamba,
what it is, and how does it improve
over other markets?
>> Yeah, sure.
So if we take a step back and think
about really almost all the models
you know, whether it's GPT,
or Claude, or Mistral, you name it,
they're all transformer-based.
And transformer is what enables
suddenly these models to do well,
not just on vision,
which is in a sense, quote unquote
easy problems, very local to know
that this here is a phone.
I don't care what the pixel over
here on the other side is,
that roughly true.
In language, there's nothing local.
I changed a word here,
the whole sentence that you
can't get away from semantics, and
transformers suddenly enable us to
deal with that.
Up until then, there were
convolution neural nets and
recurrent neural nets, and
very good for kind of object
recognition, but not for language.
Transformers changed that and
and the basic mechanism there
is the attention mechanism, which
allows you to relate to attend,
as it's called, the attention,
to attend to different parts of
the input that could can be quite
disparate, quite far apart.
So that's good, and suddenly,
you saw the needle move on language
task, but
the price you pay is complexity.
It's quadratic complexity in
the input size, the so
called the context length.
And if you have a context length
of, say, 1,000 tokens,
2,000 tokens, that's okay,
you got a couple of million.
Sort of a 1,000 squared is okay,
but we're now pushing a million.
A million squared is not okay.
And so that's transformers,
what do you do about that?
Turns out that there's
an alternative architecture,
without getting too geeky,
called state space models, SSMs.
And recently, about a year ago,
there was a special version of that
called Mamba, came out at academia,
I want to say Princeton and CMU,
I think, that made it more
efficient, more interesting.
So our guys, what our guys did,
did something very innovative,
I take no Credit for it.
They did a hybrid architecture that
mostly Mamba, but a little bit of
transformer, a little bit, and so
you get the best of both worlds.
You get the quality of
the answer is very competitive with
the transformer models and
complexity that's not quite linear,
but almost linear.
And so the latency is tiny,
the memory footprint, for example,
we have two models.
Now the small model, I'm forgetting
small model, I want to say,
I think it's 52 billion total
available parameters, of which 12
billion are active at a given point
in time, what's called the mixture
of expert kind of architecture that
recently became discussed because
of Deep DeepSeek, but
it's an old it's an old technique.
And so that's our small model which
is fun to call it small, but our
big model is almost 400 billion,
392 billion parameters and
94 active.
The small one fits on the single
gigabyte GPU,
which is mind blowing,
now the model can come close.
And the large one on a single eight
GPU pod.
So, we've had very large companies,
switch to Jamba, because suddenly
the unit economics and
the latency makes sense.
>> So when we talked about some of
the factors that slow down
adoption of the enterprise.
The first one efficiency and cost,
can you unpack that and
give us more details about that?
>> Well, I mean,
you see that the most successful
Gen AI company, terrible term,
by the way, generative AI, but
it is what it is.
So open AI making, I don't know,
they claim 4 or $5 billion a year,
and losing much more than that.
It's very expensive, little lower,
I'm not speaking about even
training these model,
just serving these models.
And so the unit economics are very
different, and
so you need to somehow do something
about it.
So one way of tackling the problem
is making the architecture such
that it's much cheaper, and
that's what Jamba does.
The other is to realize that
the world doesn't start and
end with LLM, not everything you
want to give an LLM.
So LLM do arithmetic, for
example, which is in some sense
very impressive.
On the other hand,
they do it slowly and poorly, and
they'll never be as efficient and
as precise as an HP calculator
from 1970.
So the switch to AI systems,
which have ALN, but
they have tools like a calculator,
an API code, a custom code, and
some are orchestrating all of that,
that is doing two things.
First of all,
it's making the system more
efficient where possible.
And second, they're making them
much more precise.
And that's the other key thing
in the enterprise, this
precision that without which it'll
forever remain experimentation.
>> So can you tell us a bit more
about how to solve these problems?
>> I can, but I won't, but
I'll say a few things about it.
We'll be coming out before too long
with a product in the space which
I think would be interesting thing,
and we'll give many of the details.
I can say a few things, in fact,
just yesterday, a peace of mind
came out in fortune that spoke
a little about these things.
So let's think a little
under the hood, what's
happening with these models.
So when you run a model, basically,
you have this probability
distribution and
you're sampling from it,
doing some kind of posterior
based on the input, which means you
have something stochastic.
And so you have to sample multiple
time to iron out the variants here.
And sometimes, like you said,
you don't want to appeal to this
probably a distribution.
But another one, and
maybe it's not a distribution,
it's a point distribution,
namely a deterministic tool.
And so, what you see here
are a bifurcation, there are some
people who are trying to shoehorn
all the smarts into an LLM.
There's an approach called React,
which some of the audience here
will be familiar with.
It tries to teach this mini system,
this LLM to take an action,
get the feedback, to some kind of
analysis with it and repeat.
There's cherry-picked examples
where you get kind of wonderful
things, but by and large, it's
uncontrollable, it doesn't work.
What you see in the enterprise is
the polar opposite of handcrafted
sort of static chain.
So if somebody wrote code and
said I'm going to call this LLM.
And with this kind of input and
I don't trust this output so
I'm going to try it multiple times
with different inputs.
And then I'll look at the output
and I'll decide do I like it or
not, and depending on that, and
now I'll call it calculator.
I want to know some proprietary
information and proprietary
database, I'll call the APIs.
Somebody wrote a script to do that,
the AI didn't play a role here, but
except when some of the tools were
LLMs.
What you're going to see is coming
out are approaches that kind of do
the best of both worlds, do let AI
do the smart kind of scripting
execution when it makes sense.
And still give the user control and
observability so
you can trust these systems.
That's kind of the direction we're
going in the world.
These are these AI systems.
So one of my colleagues,
very well-known, Yan LeCun, likes
to diss LLM and says that within n
years, and for some small n nobody
will speak about LLMs.
I don't think that's true, but
I do think that there won't be
the end all in, be all.
And I actually think that by the
end of 25, people will speak about
AI systems and the core and central
concept that enable us to kind of
move forward in the enterprise.
>> So before we talk some more
about the implications of debt for
enterprise decision makers, I want
to take a step at another question.
Lots of people talk about agents
today, and you've put together
that framework many years ago.
What do you think about,
what people are saying about agent?
>> Let me start with a positive,
I think there is a there there.
I don't think people should ignore
concept or think it's irrelevant.
But AI, specially in recent years,
has had this bad habit of taking
ill-defined terms and using them as
if they're well-defined.
And based on that raising money,
or doing PR, or
promising products to customers,
and it's kind of quicksand.
So my favorite example has always
been AGI, it's not a thing.
So I would never raise money by
appealing, I'm going to create AGI,
I just don't
think it's a well-defined thing.
Agents are a little like it,
agents really under that,
if you went to Davos this year,
which I did, but my co founder did,
everybody speaking about agents.
It was clearly they're talking
across each other.
There's several different things
that are taking place there, and
they all make sense in isolation.
They don't necessarily come
together to make a complete whole,
and because we can list them, but
it has to do with doing AI systems.
Have to do with using tools and
not letting just the language model
do the whole thing.
It has to do with having some
amount of reflection, so
that because to compensate for
the inaccuracies of Of the LLMs.
It has to do with running long
press of LLMs,
typically very transactional.
You put in the prompt, and
seconds or a fraction of a second
later you get the response,
whereas these agents can run for
a long time, minutes, or hours, or
sometimes months, and
they can be proactive.
It's not necessarily a stimulus
response, they can initiate that.
So it's sort of become more of
an active assistance than a passive
tool.
So there's a whole collection of
concepts here that it's a mistake
to try and call anything agent
because it'll mean everything and
nothing.
But having said that,
like I said at the beginning,
there are exciting things
are happening in the space, so.
>> So let's kind of think,
I imagine a decision maker in
the enterprise is facing a terrible
dilemma, on the one hand
everybody's asking them,
what are you doing about AI?
So they go with today's technology,
which may not fit the architecture
of the future.
So can you help people think about
that question?
How do you trade off the desire
to get good results today, or
at least experiment with the desire
to architect everything so that it
works better in the enterprise.
>> Yeah, so we're engaged with lots
of companies,
typically very large corporations.
And I mean, my first advice is
always absolutely experiment.
If you and your people don't have
a visceral feel for technology,
experiment.
Experiment with something that's
meaningful, not a throwaway thing,
but perhaps, don't bet the farm on
quite that application right now.
That's one thing.
The other thing is, we've had
companies very thoughtfully put
together 200, sometimes 400
potential use cases for Gen AI.
And they speak to us about,
so which of those.
And you want to take something
where the technology risk is fairly
low, and nonetheless, it's not
trivial, and if you're successful,
you'll actually move the needle.
I'll give you an example of that,
so it's not abstract.
So we have one very large retailer,
they have very robust online
market, and I forgot if I'm allowed
to say the name,
so I won't just to be on safe side.
And they have millions of products
on their website.
Thousands come up every day,
and they need to provide product
descriptions.
And that's a very labor-intensive,
costly in money and time process to
do over and over again.
And so, we actually had a system
which is not just a language model,
it's language model at the core.
But you start with,
I don't want to call it rag, people
familiar probably with retrieval,
augmented generation, but
there is input to the system that
wasn't available at training time.
And based on that,
and with highly customized post
training that we did, is very good
at product description, so much so
that they've slowly start to wean
themselves off checking every
product description that comes
online.
And that's also a good trade-off,
people speak about
product-market fit,
I speak about product-algo fit.
What I mean by that is
that technology is error prone,
it's certainly AI technology.
So if you're creating a product or
service, you need to be aware of
its strengths and weaknesses, and
craft the offering to leverage
the strength and compensate for
the weaknesses.
And so human in the loop is part of
it, and also it depends on the cost
of error.
If 1 in every 1,000 products
distributed is off the world will
not crash, and you can fix it.
That's a good kind of trade-off to
do here.
>> So when we think about
a product-algo fit, one parameter
is the cost of an error or
the required reliability.
What are some other guidelines you
would have, or people who say,
well, I want to experiment with
today's LLMs and I want to get as
much productivity out of it.
So what would be some of
the parameters of the best fits?
>> I think that practical algo
is more of a how question,
not a whether or which question.
I think your question to me was
more about, so where do you focus,
not how you.
And I go back to what I said
before, it's got to be important
enough for you to care if it's
successful or not.
But bite size if that's your first
project.
And we typically have people
working on two or
three projects simultaneously,
maybe two or three different teams,
sometimes experimenting with
different technologies.
I think that routinely people
are speaking with a language model
trying several,
that's always a good thing to do,
and you learn from that.
This day and age related to what I
said before, you will never just
take a language model and use it,
you will always craft an AI system.
And you want a partner to help you
architect that system in a way that
won't crumble under its own weight.
Yeah, so
that's what I can say right now.
>> So AI system is more
open-mindset than a product?
>> Right now you don't have
a packaged offering that says,
here's a way to create an AI
system.
Right now it's mostly description
of what people do
in IT departments.
It will become a product category
this year.
Again, you have to be careful
because people latch onto
concepts and
turn them into marketing slogans.
I mean, you can go to all the cloud
providers, and
you'll have agentic offerings.
And they're very thin layer
that does very little for
you, I mean, you'll
still need to do most of the work.
And what you'll see, I think,
this year, is more and more
people will offer you to offload
a lot of this burden from your own
IT custom development effort.
And we'll be coming out of With our
own product before too long here,
and we probably won't be the only
ones.
>> So when we think about
the architecture of an AI system,
is there a clear migration path
from today's architecture to
the future architecture?
Or is it more like a greenfield,
some you have to rip apart what you
have and rebuild?
>> It's a good question, and
I'm not smart enough to answer it.
I think that, I don't really know,
I mean, there are elements
that are really new and
that will upend traditional.
In fact, it's open question
about how transformative AI will
be to the enterprise.
And it's not just these the IT sort
of infrastructure, it's also that.
I forget if it was Satya or
Jensen that said that IT
departments are going to transform,
they're going to
be HR departments for agents.
I think that too cute to be
a correct description, especially
since agents are well defined,
but certainly they'll change.
In fact, when you think about this
Android organization,
where more and more functions
are done by machines.
I don't think, by the way that all
functions will be taken over by AI,
I really don't believe that.
But more are and will, and
really there'll be a collaborative
relationship between these sort of
AI workers and human workers.
I think it will have an impact on
the enterprise, and honestly I'm
not smart enough to really say much
more intelligent things about it.
>> So we have quite a number of
great questions from our
participants, so we're going to
go to some of these questions.
So one of the participants
is asking,
today have you seen ad deployments
that augment to replace workers,
and where we will be on that scale
between augment and replacing five
years, given what's happening?
>> So I'm in the non-alarmist camp,
but not the complacent camp, I'll
try to say what I mean by that.
So there are lots of studies about
the future of work because of AI,
I mean they're well intentioned,
but I think they're much more
speculation than based on real
fact.
Historically, technology created
more job than it replaced,
that's historically true.
Some people saying this time is
different, I think the onus of
the kind of argument is on them,
because I don't see a reason to
think that.
I think we're just not smart enough
to anticipate what jobs our kids
and our grandkids will have, but
there's no question there's some
jobs that are going away.
I mean, just let's take writing,
copy editing,
we used to have copy editors,
that's gone.
I mean,
software does this extremely well.
Editors as in a sort of magazine
editor or a book editor,
they haven't gone away, and
I don't think they'll go away.
I think their job, they'll
have better tools to work with, but
I don't think they'll go away.
And so I think it'll be a mixed
bag, and I know there
are predictions by percentage of
white collar job that will go away.
All I can say is, I don't know
the answer, but what I've seen,
I've found highly speculative.
For example, the movement for UBI,
Universal Basic Income,
because all work will go away.
And so what we need is to
give people money, and give them
a different meaning to their lives.
I think it's a little good
question, what's the meaning for
our lives and why sometimes work
is so a central part of it?
That's always a good question to
ask, but I don't think that jobs
will go away at such a scale to
make humans workless.
>> So we have a question from
Nalan Sipar,
who is a journalist from Germany,
and she's obviously interested in
what will happen to journalism.
So where are some of the big
opportunities for AI and
journalism?
>> So my favorite answer to
this question,
is enjoy your while you have it,
but I don't really believe that.
Okay, I think journalist or writers
are probably the most important
people in the world today,
because the information layer that
underlies the liberal democracy is
under relentless attack.
And if we could rely on good
editors, good journalists to get at
the fact and present to us in
a compelling way, and to sift
the important from the unimportant.
Now technology has made us
very challenging,
by the way, it's not just AI.
I know people like to speak about
fake news and how AI is the main
culprit here, AI has a role to play
here, both Positive and negative.
I can speak about that, but I think
the dissemination technology,
social networks, in general,
the flat world,
is even a stronger sort of force.
And it has to do with social and
psychological and economical
factors, so it's very complicated,
but I think journals job will be
not just to get the facts, but to
persuade us to listen to the facts.
And I think it's super
important and super hard.
>> Great, Danny Wong is asking,
in addition to the kind of a factor
that block adoption that we've
discussed so far.
What is the other most important
factor that is
holding back companies
from using more AI systems?
>> I honestly think all the rest
are sort of second,
if not third order.
But sometimes it has to do with
lack of expertise in the area,
which is not different from
adopting new technology in general,
but maybe this is new
in a different way.
So that's sometimes part of it.
It's understanding the use cases
well, and
they're mapping to the strength and
weakness technology.
[COUGH] I think those
are the main factors.
Sometimes it's lack of access to
compute, but I think that's rarely
the real factor.
>> So I'll interject my own
follow up, what should we be
doing in universities to help
alleviate that problem?
>> Where by university, I mean,
you probably mean specifically
in In the business school or
people working with industry.
>> So I'm asked about universities
but really it's about education so,
what should the education system do
at any level?
>> Okay, if you- >> What value we
get out of these systems?
>> Well, if we widen the question
sufficiently, I think
that being AI educated is something
we need to inculcate at all levels.
There's no reason you shouldn't
have already in elementary school.
My youngest son is in middle
school, and I gave a lecture to
the kids there, and they asked me
as intelligent questions as I get
from Stanford students and at least
I got while I'm still teaching.
And so I think we should have at
all levels.
Obviously, if you kind of go to
the other extreme and
think about re-skilling, because
even if I'm right and the overall
trend is positive to the workforce,
there's a transition period that
some people can find painful, and
so we need to help with that too.
So I think there's a role
everywhere, I think it's happening.
I don't know if the optional way in
the right capacity, but
the universities I know all have
executive education on these
topics, and certification for
people want to transition from and
so on,
I think it's across the board.
>> Great, we have another question
about the impact of DeepSeek and
some of it is just about
DeepSeek itself, and some of it is,
what do you think about it?
What do you think is going to be
the impact of that?
>> Okay, [COUGH], so maybe 30
seconds of just facts, DeepSeek
is a company, they have a couple
of 100 quite smart people in China.
Part of it, this hedge fund,
which managed a lot of money,
then managed less money.
They've had models come out for
the last several years,
we've known them, and we've always
known them to be a legit shop.
Their DeepSeek,
particular model R1,
is a fast follow on OpenAI's O1,
and the reason they made so
much noise is not so
much because of their innovations.
They had a few,
they have latent attention,
multi mixture of experts have.
And by the way, OpenAI didn't
invent anything with O1, but
the typical factor, they did it
robustly for the first time.
R1, also their innovation over O1
are nothing they invented, but
that's the nature of the community.
But the main reason they got
attention was for two reasons.
One is they open-sourced the model
unlike the closed source of OpenAI,
ironically.
And by the way, open-source is
a misnomer because really,
they share the weights, but not
the code, not the training data,
which limits the usability.
They're also fairly open,
not completely, but
fairly open in describing how they
train and so on.
So that's one reason the community
now could just take it and
run with it.
The second reason is the claim that
they did it very cheaply on weak
hardware, and that we should
take with a big grain of salt.
There's no way the model total cost
was six million dollars,
it was at least one and probably
two orders of magnitude larger than
that, and I can explain why and
what really made it explode was
their chat application, which
became the number one application
in the app store.
So those are the reasons.
I didn't understand the sell off on
Wall Street,
didn't make any sense to me.
First of all,
like I said, they didn't do it as
cheaply as some people thought.
Number two,
most of compute spend is going to
be on using the model on inference,
not on training.
As expensive as training is,
especially as AI gets widely
adopted, inference is going to
dominate the spend, and so I think
the hoopla around O1 was overblown
and the counter hoopla around
DeepSeek was equally overblown.
But a nice model, by the way,
people have tried DeepSeek against
Jamba, special certain problems of
question answering, and
Jamba was just better,
much more factual, and so on.
So, it's a good model, but yet
another model.
>> Some people are saying, open
source is winning against closed
sources, what's your view on that
kind of debate between open source
and semi open closed >> Yeah,
certainly, there's a strong
pressure on closed source, and
I'm not sure that Tenable, I think,
for example,
DeepSeek may force OpenAI's hand.
In fact, Sam, on record, saying
something along the lines of, we've
been on the wrong side of history.
So I think you see people share
more, not everything, but more, and
we shared one version of the Jamba,
open sourced, it served us well,
and so
I think you can see more of it.
Are the open or semi open source
models as strong as the strongest
closed source ones?
Not yet, but
they're getting stronger.
>> We have a question that asked
you to summarize, but
really project, so I'll kind of
rephrase it as, what do you think
enterprises should be thinking
about and focused on in 2025,
given what we've seen to date,
and given the trends that we
are observing already?
>> A broad question, I'm not sure
there's a pat answer across all
enterprise, I think this varies,
but I would say.
By the end of the year, try to
commit to one real deployment.
Keep yourself honest,
it's fine to experiment, but
the time now is to be part, and
I really think that if you don't,
you'll be left behind because I
think we are moving to more of
a mass deployment.
Some large fraction of Fortune 500
companies were going to have
mass deployments,
which isn't the case now.
And so, you want to get to
mass deployments whatever it takes.
And which means you need to handle
the issues of reliability and
controllability but
just make your CIO or CAIO.
Make them make it happen.
>> Great.
>> And we have another question.
It's a broad question, but
let's try to compress it to four
minutes about kind of what will
happen between China and the US.
And do you see kind of the industry
going to be a Chinese branch of
the industry and the US branch and
they compete with each other.
What do you foresee, at least on
some of these dimensions?
>> I think the short answer is yes.
We've already seen it happen.
For a long time now, China has not
been just the quick implementer of
the big innovation of the West and
so I'm not sure it'll be quite
bipolar.
I think there are more and more
pockets of strength in the world.
Obviously now Europe is making
a big bush after the recent action
summit in Paris, a lot of fanfare.
So you see more action of Europe,
obviously, the Emirates and
Saudi Arabia are spending
a lot here.
So I think it's going to be a more
interesting dynamic than the simple
Chinese, US, but those are
certainly going to be major polls.
I think that it is going to remain
fairly bifurcated for
geopolitical reasons, not for
technological reasons.
>> So basically, you see increasing
competition between US and
China learning from each other,
but developing as a duopoly
essentially, or not.
>> So, again, I'm pushing back
a little bit on the duopoly I think
it's going to be a little more
multipolar than that.
But certainly these are very strong
polls and you're going to see,
more and
more competition across the stack,
not only at the model level, but
all the way down to the chips, and
clearly, especially now with
current geopolitical sort of
configurations.
There's going to be even more of
division lines, and constraints,
and so on, restrictions.
So I think you're going to see
a lot of independent development
in China.
And you'll see resistance to
adopting the Chinese technology in
the West.
So I think that's likely in the
next few years, likely dynamics.
>> And what do you foresee for
Europe?
>> Interesting,
I think they're spending or
claiming to spend a little money.
It varies, so we have our German
friend on the call.
Germany has been a little hard to
do business in.
On the other hand, France has been
quite innovative and nimble here.
And doesn't end there, I mean, as
you know, we're based in Israel and
very small country, but we've
always punched above our weight and
you'll probably see this here also.
So, I mean, US will continue to be
the main center of gravity here,
that won't change, but
I think you'll see others centers
that are of meaning as well.
>> That's great Yoav.
Thank you so much for
giving us a glimpse into the future
of AI and the enterprise.
And we look forward to seeing more
announcements later this year.
And thank everybody for
participating in the webinar.
Before we wrap up today's session,
I would like to give you a preview
for our next webinar in
the speaker series.
On March 19th,
we'll be hosting Michael Marks,
who is the founding and managing
partner of Celeste Capital and
is the former CEO and chairman of
Flex, which is a company which
has redefined the past and
is redefining the future of
global manufacturing.
Michael will share his insights on
how AI is impacting the business
world and
the opportunities that he sees for
AI to drive value creation.
Thank you very much.
And Barchi has a few additional
words to share with us.
>> Thank you, Haim, and many thanks
to Yoav for a very engaging and
insightful discussion.
As I mentioned in my opening
remarks, we kindly ask that you
take a moment to complete our brief
survey, you can
access it easily using the QR
code displayed on the screen.
We also invite you to use the link
shown on the right to access the
value Chain Innovation Initiative
website and take a look at
our upcoming webinars.
This website is also
the place where we will post
the recording of today's event.
And with that,
we conclude today's webinar.
Thank you all for joining us,
we hope you have a wonderful rest
of your day, and we look forward to
seeing you in future events.
[MUSIC]
