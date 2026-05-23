---
notebook_id: fa2fc99f-e8fb-4871-9ad4-209b77ad1bf8
notebook_title: "Stanford Graduate School of Business"
source_id: 1b48eeea-fda8-4e3d-9425-8f44000e35ec
source_title: "What We Actually Learn From Experience"
source_type: SourceType.YOUTUBE
extracted_at: 2026-05-21 12:54:46 UTC
extractor: nlm_bulk_extract.py
---

# What We Actually Learn From Experience

## NotebookLM-extracted transcript (Google's ASR + indexing)

[NARRATOR] Meet Ann Miura-Ko.
She's been making early stage
investments in Silicon Valley
startups for seventeen years.
[ANN MIURA-KO] I guess the one that most
people would recognize is Lyft,
where I was the seed investor
and led that seed from a
five million dollar
valuation through when it
went public.
[NARRATOR] Lyft is now a global
ride-sharing company
worth more than six and a half
billion dollars as
of early twenty twenty-six.
Ann's venture capital firm, Floodgate Partners,
continues to make big
bets on small companies.
As their business has matured,
the way they choose
founders has evolved.
[ANN MIURA-KO] Early on, it would be looking at
their resume,
and I'd be looking at things
that they'd done,
but then a lot of times the
people who are really successful
hadn't done that much.
[NARRATOR] Ann makes an educated guess at what founders
might be capable of,
even if they're fresh out of high school.
[ANN MIURA-KO] You're really evaluating the
human
behind that idea and their
capacity for learning
and change and building things
quickly.
[NARRATOR] Founders know they need to learn
from their mistakes,
and Anne is not that concerned
when her investments fall short.
[ANN MIURA-KO] There's the kinds of mistakes
where you
invested in the wrong company,
but in venture,
you can only lose the dollars
that you put in.
You can't lose more than that.
Versus when you fail to make the right decision,
that's where you really lose out
on the hundred thousand X.
[NARRATOR] It's the big successes they
don't invest in
that keep VCs up at night.
So how do they learn in a way
that avoids
missing the unicorns?
[ANN MIURA-KO] When we think about learning,
we're always looking
at what are the hundred baggers,
which are the companies
that net 100x on your seed stage investment?
We'll look at other companies
outside of our
portfolio that net that.
We look at companies that are
anywhere from 25 to
100x within our portfolio,
And we're trying to seek to
figure
out what are the patterns within
those that are repeatable.
[NARRATOR] It's a hyper-competitive
industry that tries to discover
entire new categories before the
rest of the world catches on.
[ANN MIURA-KO] I'll give you one example that I
really love, which is, ah,
there's this philosophy book around scientific revolutions.
that Thomas Kuhn wrote.
And it was written
quite a while ago,
but the theory within it
can actually be quite
relevant to how inflections
happen in our world.
How do we identify
those things?
And then how do we map that
to the current world of AI?
[NARRATOR] It's more than
simple common sense.
Trying to tease out what exactly
we learn from experience is
an emerging research field known as correlated learning.
[STEVE CALLANDER] Here in Silicon Valley, the expression that you
learn from failure is very
widespread and very intuitive.
But the question is sort of what
do you learn?
How do you optimally learn
from that experience?
[KEVIN COOL] Today, we're going to talk
about correlated learning
and how it can help us
make better decisions.
We're speaking with Steve
Callander,
Professor of Public and
Private Management
at Stanford Graduate
School of Business.
This is If/Then
from Stanford GSB,
where we sit down with
faculty and explore how their research deepens
our understanding of business
and leadership.
I'm your host, Kevin Cool.
(upbeat music)
[KEVIN COOL] Steve is a self-described
theorist.
That sounds like pretty abstract
work,
but the models he develops
can be applied to very concrete matters, like
coming up with a business strategy,
choosing your next job, or negotiating
with your mechanic.
We talked to Steve about what we
can learn about learning and how
much we should trust experts.
But we started by asking him why
theorists are important.
[STEVE CALLANDER] So there's an enormous amount of
data in the world.
There's facts coming up at us
from left and right.
And so the theorist's role is to
make sense of that data,
make sense of those facts and put some structure
on our understanding of the world.
And the idea is that by putting this structure on these facts,
we can not only understand the
world a little better, right,
but we can make predictions and
suggestions about how we
can make the world work better.
That's the role of a theorist.
[KEVIN COOL] Mm-hmm.
And in a lot of your work, you
are trying to presumably
translate pretty sophisticated
and complicated, you know,
mathematical and statistical
models.
If you're doing that for a lay audience, how do you do that?
[STEVE CALLANDER] Well, that's one reason why I love being in a business
school where I am forced, I
force myself,
to stand up in front of an
audience of very smart
but lay people and explain to
them why this knowledge
is useful, how it helps us
understand the world better,
and what we can do with it.
And I love that challenge.
[KEVIN COOL] Well, I'm glad to hear that you
love doing that because that's
what we're going to do today.
And we're going to start with a
paper that you did,
the title of which is Learning in a Correlated World.
And it's really discussing the
concept of correlated learning, which is a term I'm
not familiar with.
What is correlated learning?
[STEVE CALLANDER] So correlated learning is all
around us.
It's in every aspect of life.
What it means is that the
outcomes of different
choices are correlated.
That's a fancy mathematical
statistical word,
but what it means in practice is
that what happens if you make
one choice is connected, related, correlated with the
outcome you get from other choices.
And so what that means is we can learn from our experience.
We can learn
across alternatives.
What you did today may have
worked, it may not have worked,
but it tells you something
about what other choices, what
other alternatives might work.
And so what I do is try
to study that connection,
those correlations, put some
mathematical structure on it
to both help us understand
correlated learning in practice
in a variety of domains,
but then help us figure out what we should do about it.
How can we learn better?
How can we structure our choices
better to make better choices?
How can we design markets?
How can we design political
institutions in a way that
allow them to learn better?
[KEVIN COOL] What are some real world
situations that this
research might apply to?
[STEVE CALLANDER] I'll give you two examples.
One is just an experience I
think all of us have had,
which is searching for a job
and learning from our experience
from our past jobs.
So an example I love to give is
a fresh graduate comes out
of college and takes a job at Goldman Sachs,
and they hate it.
They hate the long hours.
They don't like the work.
They don't like that their boss
yells at them occasionally,
and then they have to decide
what to do next.
If there was no correlation,
they would just pick another
job randomly and try that and
see if that works.
[KEVIN COOL] Now, when you say correlation, what are you referring to?
[STEVE CALLANDER] In this case, it's whether
this person likes these jobs or not,
whether these jobs
are a good fit for them.
[KEVIN COOL] Okay.
[STEVE CALLANDER] Instead of being a bit more
concrete about it,
if you don't like your job at
Goldman Sachs,
there's not much chance you're
going to like
your job down the street at
Morgan Stanley.
Sure, these financial
institutions are
a bit different,
maybe a little idiosyncratic,
but the job is going to
be largely similar.
[KEVIN COOL] The considerations that
make that person not like
the job aren't going to be
different.
[STEVE CALLANDER] They aren't going to be
radically different, no.
The hours are gonna be long, the
work's gonna be similar,
the culture of the institution,
the relationship with your boss
is gonna be pretty similar.
And so if you didn't
like Goldman Sachs,
it doesn't make much sense to go work at at Morgan Stanley.
All right, so maybe you branch out a little bit,
maybe you get a hedge fund.
It's going to be a bit
different,
[KEVIN COOL] right?
[STEVE CALLANDER] But still pretty similar.
So there the correlation isn't
as high, but it's
still very, very strong.
Versus taking a job as a
financial planner in Ohio,
that's still in finance,
but it's a very different job
(laughter)
from working on Wall Street.
And so there, the correlation is going to be a lot lower.
And so what my modeling is trying to do is to help
us understand that choice.
What would be the optimal second
job for
our college grad to take?
How do they think through these
choices,
and how do they strategize
long-term over those choices?
[KEVIN COOL] So what does the model do that
leads us to that
conclusion, if that's the right
word, or that insight?
[STEVE CALLANDER] Yeah, so the idea is to put some
mathematical structure on this.
And so the way we do it is
we represent the set of alternatives in a space.
And this is going to get very mathematical,
but then there's going to be
some function
or some mapping from
those alternatives to outcomes.
So how far apart these jobs are
in the space
indicates how correlated their
outcomes are going to be.
And so we can think, should you
search for a job
that's nearby or should you jump
a long way, do something
very different that gives you
the chance of maybe finding a
job you're going to like,
but it itself is sort of high
risk.
You really haven't learnt much
about the likely outcome
of that job, or about how well that job fits
to you and your characteristics.
[KEVIN COOL] Help us understand then how those
potential outcomes or
possibilities, opportunities are
expressed in the model
that would be useful for someone
to take that and say,
"Hmm, okay, I never thought
about it that way."
[STEVE CALLANDER] The mathematical answer to that
is that the way I model
this function or this mapping
from the space of jobs,
the space of alternatives to
outcomes is to use some
mathematics that's
very popular in finance, which is the Brownian motion.
[KEVIN COOL] Brownian motion.
Okay, what is that?
[STEVE CALLANDER] The Brownian motion goes all the way back to a botanist
a hundred plus years ago who
described the movement
of atoms as representing an
almost random process.
And then a hundred years ago,
Albert Einstein developed
the mathematical theory of
Brownian motion.
So what it really is is it's a
description of a
random walk, a process
that's just wandering through
the space.
So what it means is because it's
continuous,
that alternatives or things that
are close together in the space
have outcomes that are close by,
Whereas alternatives that are far apart in the
space are going to have outcomes
that are much further apart.
Doesn't mean they're the same,
but it does mean that in
expectation, things
that are close together are
going to produce nearby
outcomes.
I think this is a very intuitive
sort of notion that pops up
in a lot of places, the idea
that
nearby alternatives, nearby
choices should
produce nearby outcomes.
And by representing this function from alternatives
to outcomes, it captures that
this eternal truth or that
essence of decision-making under
uncertainty.
And it does it in a very elegant
mathematical way that allows us
to have some structure on the
problem that we can then analyze
the model with this structure
and say something concrete.
[KEVIN COOL] So does Brownian motion help us corral to some degree that
randomness and that uncertainty
and make some sense of it?
[STEVE CALLANDER] Absolutely. And to get, again,
mathematical here, the
fact that it's, again, a
continuous function
means that if you learn the
outcome of one alternative,
you learn one point in this
mapping,
then you know that this mapping
goes through that point.
And so it's going to tell you
that alternatives that
are nearby are going to have
outcomes that are nearby.
So if you think about this in
the example of our
college grad who worked at
Goldman Sachs, he learned
the outcome of that job.
He knows that value.
Morgan Stanley, which is very close to
Goldman Sachs in the space, is going to have an outcome
that's very similar or very close to Goldman Sachs.
It really isn't going to be that
different.
It's not exactly the same,
and that's the beauty of the
random walk.
Every alternative produces a
different outcome,
but this captures this sense
that nearby alternatives
produce nearby outcomes.
And so that allows our job
seeker to search.
If he loved Goldman Sachs,
then he'd expect a job at
Morgan Stanley, you know, might be better,
and he's going to love that as well.
But if he hated it, then taking the job at
Morgan Stanley isn't going to be
a very wise choice.
He needs to jump to a job that's
far apart in this
space so that he can expect or
hope for an outcome,
a fit of that job to him that is
very different,
and hopefully on the upside.
[KEVIN COOL] Steve, is this to some degree
also a mindset shift?
Like, what's different about
this?
[STEVE CALLANDER] I do agree it's a mindset issue.
So it's something we all do.
We all learn from our
experience.
Here in Silicon Valley, the
expression that you
learn from failure is very widespread and very intuitive.
And so it's a concept that's very familiar in that way.
But the question is sort of what
do you learn?
How do you optimally learn from
that experience?
And so what I'm trying to add
with my framework is by
formalizing this idea that you
can learn from your experience,
take something very intuitive,
something we all believe,
formalizing it through theory, so that we're taking this
sort of intuition that sort of exists in
the ether, but you know, we're all sort of doing it.
It formalizes it in a
mathematical,
in an economic structure.
And then by building that
structure,
we can begin to analyze what's
the
optimal strategy for an
individual or a firm to pursue.
How is market competition going
to play out in a world
where learning across products,
across strategies is correlated?
So that's what I think is new.
That's what I'm trying to add.
(clears throat) Mm-hmm.
And it turns out that this is very difficult
to capture formally.
It's not that I think
economists and theorists
weren't aware that correlated
learning was important,
but it's just very, very
difficult to capture it
formally.
[KEVIN COOL] Well, I actually loved your
very straightforward answer
about what did you learn,
because to some degree that's
an abstract notion, and it
reminds me of a conversation
we had with Deborah Gruenfeld,
one of the associate deans
at the GSB, and she said the
thing that she admires
about so much
research at the GSB is that it makes the invisible visible,
and this seems to me like one of
those examples.
Like you're taking something, to
use your term, that's in
the ether and trying to make it
concrete in some fashion, right?
[STEVE CALLANDER] Oh, yeah. I like that phrasing.
Yeah, exactly right.
I think that's what we do.
We make... The theorists make
the invisible visible.
[KEVIN COOL] Yeah.
[STEVE CALLANDER] And then once we can see
it clearly,
we can start to sort of extract actionable
insights from it.
[KEVIN COOL] We'll be back in a moment with more from my conversation
with Steve Callander.
We'll talk about how to evaluate
experts and
how correlated learning informs
business strategy.
(music playing)
[KEVIN COOL] So your paper
also talks about the trust that we extend to experts,
and that can be the examples you
use.
It could be on an executive
board of some kind.
It could be your local auto
mechanic.
Those are two very different
sort of situations.
What's common about them with
respect to your research?
[STEVE CALLANDER] Excellent.
Yeah. So this is another vein of
work that I've pushed this,
this model of correlated
learning.
What role experts play in
decision-making?
And they're everywhere in our
life.
You go see a doctor.
You're going to the doctor for
expert advice.
They have more information than
you have, and they're
providing you recommendations about what you should do.
You go to the mechanic.
The mechanic knows more than you do,
or at least she knows more than
I do now about cars,
that's for sure.
I can barely put air in the
tires of my car,
and I am trying to learn from
her expertise.
But at the same time, whether
it's the doctor,
whether it's the mechanic, I'm
not so sure I see it,
our interests as being perfectly
aligned.
And so there's an element of
trust or a doubt there
(mm-hmm) as to
whether they're giving advice
that's in my interest or whether
it's advice in their interests.
And so they're examples from everyday life,
but they come up in professional life as well.
You're a CEO of a firm,
you've got division managers.
Those division managers know
more about what's happening
in their division than you do.
You are trying to extract that
information when you ask them
for advice and recommendations
about what the firm should do,
but you have some doubts.
Are they acting in the firm's
interests,
or are they acting
in the interests of their
division or their own career?
The board has a similar problem with the CEO.
One thing I teach about is
crisis management,
and I'm yet to encounter a CEO
who has recommended
to the board that they be fired
as a result of
the crisis that erupts.
And so the board has a problem.
The CEO has better information
than they do,
but the CEO has his or her own
interests at heart.
And so this creates an enormous
sort of trust problem.
How can you as a decision-maker
get the information you need to
make a good decision when it's
possessed by an expert
who doesn't have exactly the same interests as you.
And so what we do is study this
problem in the context
of, of correlated learning.
So you're trying to make a
decision, you're trying to
find a good alternative, whether
it be medical
care, car repairs,
whether to acquire a new
division with your firm,
whether to fire the CEO in a crisis or not.
But the expert has their own interest.
And so what this sort of gets at
is,
where does the expert get their
power from?
How does the expert provide that
advice in a way that
sort of serves their interests,
but at the same
time reveals enough information for the decision maker to
make a better decision?
And what correlated learning adds to this problem is, well,
when they tell me something,
they're revealing
some information.
[KEVIN COOL] Okay, so let's just bring some
specificity to that, 'cause
I think I'm following here.
But so let's just unpack this
and say the mechanic
says you need to have an engine
overhaul, right?
This engine is shot.
You need an engine overhaul.
[STEVE CALLANDER] Mm-hmm.
[KEVIN COOL] So you can accept that that is
the repair that
needs to be done or not.
But even if you accept it,
right,
Then it's what's the price?
Is there somebody else who would do a better job?
There are all these other
variables, right,
that go into what your model is.
[STEVE CALLANDER] Yeah, absolutely.
So suppose your car
is creaking and it's
breaking down occasionally.
Generally, you know it needs
some repairs,
so you go to the mechanic.
The mechanic comes back and
says,
"You need a complete
engine overhaul or replacement.
That'll solve your problem,
and that will also give
you a very big bill."
[KEVIN COOL] Mm-hmm.
[STEVE CALLANDER] What do you do with that information?
Well, you share some common interests with the mechanic.
Both of you want the car to be
fixed.
But where you don't share a
common interest is in how
expensive the repair is.
The mechanic has financial
incentive to have a higher bill,
and you have an incentive to
not spend as much as you need
to.
So do you accept that set of
repairs?
So what do you do?
Well, what you have learned is
that you, one, don't need to
change the brakes.
You don't need to change the
tires.
The electrics are all working
fine.
So you have learnt something
from the fact that the mechanic
has told you what she thinks is the best repair for her.
And so then you've got some information.
You've narrowed down where the
problem is in your car.
So that tells me that maybe just
changing the pistons,
Yeah, maybe even changing the
oil,
that's about all I can do in a
car,
maybe that's enough of a repair.
It's gonna be a lot cheaper, and
it's enough of a repair
to make my car work.
[KEVIN COOL] Mm-hmm.
[STEVE CALLANDER] And so then I might choose that.
And so that's where this
correlated learning comes in.
The fact that the mechanic has
told me and revealed what
she thinks is the optimal
repair, given her interest,
tells me something about the
likely effectiveness
of other repairs.
And so that might mean I choose something else.
But of course, that feeds back into
the mechanic's advice.
She's thinking, "Well, if I tell
him this,"
"he's surely going to just
change the pistons."
And so her problem is what
advice or what recommendation
can I provide that will serve
her interests,
but at the same time, be a set
of recommendations
that the car owner will accept?
You might think this is
over-analysis of taking your
car to the mechanic, but the
idea is that this
problem is all around us.
It's in all aspects of our life.
[KEVIN COOL] We are at a business school.
And if we think about this in a business context or
someone who is a business
leader, an executive, say,
how does knowing something
about correlated learning
help them at some level with
decision-making, understanding
risk, whatever that might be?
[STEVE CALLANDER] Yeah, th- this correlated
learning is super relevant to,
to businesses and
business strategy.
Like, how should— which
markets should you enter?
What products should you
develop?
How should you structure your business and organize it?
This is a, a learning problem.
It's a search problem.
You're trying to find the
optimal mix of elements
that go into making a productive
business.
Learning is correlated.
You try one market, you try one
product, you try
one organizational structure,
that's gonna teach you something
about whether it works or not,
and it's gonna teach you about
what other structures
are most likely to work.
To put it in more concrete
terms,
a very popular phrase in, uh,
in startup land out here in
Silicon Valley,
but it's relevant to everyone in
business
around the world, is this idea
of product-market fit.
You know, what does product-market fit mean?
It means you're
searching for a product in the
space of products and a market
to compete
in the space of markets where
there's a real magic,
a real synergy between the
product you have and the
market you're competing in that
lead to magic happening. Mm-hmm.
And that's what you're looking
for.
And so you're searching over
both of these spaces.
You can't search forever.
Choosing randomly is unlikely to find anything good.
So you want to think about
that search
in a structured, systematic way.
And this is what uh correlated
learning and this framework and
these tools I'm developing is
intended to help people decide.
When should you listen
to the engineers?
When should you listen
to the sales team?
Like what is more important?
And how do you weigh up, balance
out the market and the product
considerations to find that fit?
And that's really the job
of a leader.
And they're doing it.
They're trying to solve and
coordinate this learning
problem in a correlated world.
[KEVIN COOL] To what degree do you think
this way of thinking is
understood or even known?
[STEVE CALLANDER] Yeah, not at all, really,
to be honest.
Uh, it's very intuitive,
the idea that you're,
you know, you're learning from
your experience,
but then that's the extent of
it.
There's no structured-
[KEVIN COOL] Right
tools.
What did I learn?
[STEVE CALLANDER] Yeah, what did I learn?
What exactly does it tell me?
How close are these
alternatives in the space?
And like, how does that affect
my level of uncertainty about
these o- other alternatives?
I think it's just not known.
Like, so it's intuitive,
and again, this is the value of
contribution of theory.
It's an intuitive notion that is
entirely believable,
and we all do to some degree,
but it's not structured.
We're not doing it well enough.
And so these tools help us
understand this theoretical
framework gives us the mindset
to
to do this systematically and in
a much better way.
Every firm I see in Silicon Valley
is talking about product market fit,
but are they doing it systematically?
I'm yet to hear of one.
[KEVIN COOL] Mm. Mm-hmm.
[STEVE CALLANDER] That does it in a systematic
way.
[KEVIN COOL] This research is what you're
spending most of
your time on these days.
Why this in particular compared
to other things that you have
done or could be doing?
[STEVE CALLANDER] Because it fascinates me
(laughter)
[STEVE CALLANDER] and I can't stop thinking about
it.
That's probably the true answer.
[KEVIN COOL] Mm-hmm. Mm-hmm.
[STEVE CALLANDER] But I think...
There, there are other things I
still work on, other papers
and projects I work on.
I don't think many academics are
super strategic and
deliberate about what they do.
We tend to follow our interests,
but I do think about where
is my marginal contribution gonna be the greatest?
[KEVIN COOL] Mm-hmm.
[STEVE CALLANDER] I have something unique, new,
and valuable to say, and I
feel like I'm making progress
And I'm loving doing it.
And, and this paper we're
talking about, this survey
of research that, uh, on this
framework I've
introduced and developed and
that I've done and
others have done, uh, has been a
lot of fun to write,
and it's really encouraging that
we're making progress.
(music playing)
[KEVIN COOL] If/Then is a podcast from Stanford Graduate
School of Business.
I'm your host, Kevin Cool.
Our show is written and produced
by Making Room and the content
and design team at the GSB.
Our managing producers are
Michael McDowell and
Elizabeth Wyleczuk-Stern.
Executive producers are Sorrel
Husbands Denholtz
and Jim Colgan.
Sound design and additional
production support by
Mumble Media and Aech Ashe.
And a special thanks to Ann Miura-Ko, partner
at Floodgate Ventures.
For more on our faculty and their research,
find Stanford GSB online at
gsb.stanford.edu or on
social media at Stanford GSB.
Thanks for listening.
We'll be back with another
episode soon.
(upbeat music playing)
